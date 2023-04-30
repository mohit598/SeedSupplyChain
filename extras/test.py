from web3 import Web3
import json
import requests

# Connect to a local Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:9545'))

# Load the compiled contract ABI and bytecode
with open('build/contracts/Transaction.json', 'r') as abi_file:
    data = json.load(abi_file)

abi = data['abi']

# Get the default account from the local node
w3.eth.default_account = w3.eth.accounts[0]

# contract address
contract_address = '0xd11a96A98b65317C8Ab3e2EDD5aA88ecEafdfE3b'

contract = w3.eth.contract(address=contract_address, abi=abi)

print(contract)

# check that we're connected to the correct network
print('Connected to network:', w3.eth.chainId)
print("***********")

# Create some test data
parent_ids = [1, 2, 3, 4, 5]
product_ids = [0, 1, 1, 2, 2]
senders = [w3.eth.accounts[1], w3.eth.accounts[2], w3.eth.accounts[1], w3.eth.accounts[3], w3.eth.accounts[2]]
receivers = [w3.eth.accounts[2], w3.eth.accounts[3], w3.eth.accounts[3], w3.eth.accounts[2], w3.eth.accounts[1]]

###

url = 'http://127.0.0.1:5000/add-transaction'
headers = {'Content-type': 'application/json'}

# Create the request body as a dictionary
data = {
    'productId': 6,
    'parentId': 1,
    'sender': '0xd04b711be347f13ee67002c1b384d575b438f32d',
    'receiver': '0x2569f52fa4345039dc09031bb06987b9b4a38df9'
}

# Convert the dictionary to a JSON string
json_data = json.dumps(data)

# Send the POST request
response = requests.post(url, data=json_data, headers=headers)

# Print the response
print(response.json())

###

# Add the test transactions to the contract
# for i in range(len(product_ids)):
#     contract.functions.addTransaction(product_ids[i], parent_ids[i], senders[i], receivers[i]).transact({"from": w3.eth.accounts[1]})

# def getParentLineage (productId):
#     x = [productId]
#     result = {}
#     while len(x) > 0:
#         top = x[0]
#         x.pop(0)
#         result[top] = contract.functions.getParent(top).call()
#         for i in result[top]:
#             x.append(i)
#     return result

# res = getParentLineage(1)
# print(res)

# oneEth = 1000000000000000000

# balance = contract.functions.getBalance(w3.toChecksumAddress('0xd925ee32d3a9fee48e6f8423922860318c5d4364')).call()
# print(balance/oneEth)
# balance = contract.functions.getBalance(w3.toChecksumAddress('0xd04b711be347f13ee67002c1b384d575b438f32d')).call()
# print(balance/oneEth)

####
# contract.functions.transferMoney(w3.toChecksumAddress('0xd925ee32d3a9fee48e6f8423922860318c5d4364'),w3.toChecksumAddress('0xd04b711be347f13ee67002c1b384d575b438f32d'),2)
# balance = contract.functions.getBalance(w3.toChecksumAddress('0xd925ee32d3a9fee48e6f8423922860318c5d4364')).call()
# print(balance/oneEth)
# balance = contract.functions.getBalance(w3.toChecksumAddress('0xd04b711be347f13ee67002c1b384d575b438f32d')).call()
# print(balance/oneEth)

# print(contract.functions.getBalance(w3.eth.accounts[1]).call())

# print(type(contract.functions.getParent(0).call()))
# print(contract.functions.getParent(1).call())
# Test the contract functions
# assert contract.functions.getProductLineage(5).call() == [[0], [1], [2]]
# assert contract.functions.getTransactionSender(4).call() == senders[3]
# assert contract.functions.getTransactionReceiver(2).call() == receivers[1]
