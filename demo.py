from flask import Flask, request, jsonify
from web3 import Web3, HTTPProvider
import json
import MySQLdb

wei = 10**18

###

app = Flask(__name__)
w3 = Web3(HTTPProvider('http://localhost:9545')) # initialize web3 instance with your RPC endpoint
contract_address = '0xd11a96A98b65317C8Ab3e2EDD5aA88ecEafdfE3b' # the address of your deployed smart contract
compiled_contract_path = 'build/contracts/Transaction.json'
with open(compiled_contract_path) as file:
    contract_json = json.load(file) 
     
    # fetch contract's abi - necessary to call its functions
    contract_abi = contract_json['abi']
 
# Fetching deployed contract reference
contract_instance = w3.eth.contract(
    address = contract_address, abi = contract_abi) # create an instance of your contract using web3

###Blockchain apis

def getParentLineage (productId):
    x = [productId]
    result = {}
    while len(x) > 0:
        top = x[0]
        x.pop(0)
        result[top] = contract_instance.functions.getParent(top).call()
        for i in result[top]:
            x.append(i)
    return result

@app.route('/add-transaction/<int:productId>/<int:parentId>/<string:sender>/<string:receiver>')
def add_transaction(productId, parentId, sender, receiver):
    # Convert sender and receiver to their checksum addresses
    sender_address = Web3.toChecksumAddress(sender)
    receiver_address = Web3.toChecksumAddress(receiver)

    # Call addTransaction function in Solidity contract
    tx_hash = contract_instance.functions.addTransaction(productId, parentId, sender_address, receiver_address).transact({"from": w3.eth.accounts[1]})

    return jsonify({'txHash': tx_hash.hex()})


@app.route('/get-balance/<string:owner>', methods=['GET'])
def get_balance(owner):
    owner = Web3.toChecksumAddress(owner)

    # Call getBalance function in Solidity contract
    balance = contract_instance.functions.getBalance(owner).call()

    return jsonify({'balance': balance/wei})

@app.route('/get-transaction-sender/<int:productId>', methods=['GET'])
def get_transaction_sender(productId):
    # Call getTransactionSender function in Solidity contract
    sender = contract_instance.functions.getTransactionSender(productId).call()

    return jsonify({'sender': sender})

@app.route('/get-transaction-receiver/<int:productId>', methods=['GET'])
def get_transaction_receiver(productId):
    # Call getTransactionReceiver function in Solidity contract
    receiver = contract_instance.functions.getTransactionReceiver(productId).call()

    return jsonify({'receiver': receiver})

@app.route('/get-parent/<int:productId>', methods=['GET'])
def get_parent(productId):
    # Call getParent function in Solidity contract
    parent = contract_instance.functions.getParent(productId).call()

    return jsonify({'parent': parent})

@app.route('/get-parent-lineage/<int:productId>', methods=['GET'])
def get_parent_lineage(productId):
    # Get the parent lineage of the given product ID
    parent_lineage = getParentLineage(productId)

    return jsonify({'parentLineage': parent_lineage})


### Sql apis

# MySQL database connection settings
db_host = 'localhost'
db_user = 'root'
db_password = '123123'
db_name = 'fypbackend'

# Create a connection
db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)

app = Flask(__name__)

# define your get_product_list API route
@app.route('/product_list/<string:product_name>', methods=['GET'])
def get_product_list(product_name):
    cursor = db.cursor()
    query = ("SELECT * FROM product WHERE product_name LIKE %s")
    cursor.execute(query, (f"%{product_name}%",))
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')