# @app.route('/add-transaction', methods=['POST'])
# def add_transaction():
#     # Get input parameters from POST request
#     data = request.json
#     productId = data['productId']
#     parentId = data['parentId']
#     sender = Web3.toChecksumAddress(data['sender'])
#     receiver = Web3.toChecksumAddress(data['receiver'])

#     # Call addTransaction function in Solidity contract
#     tx_hash = contract_instance.functions.addTransaction(productId, parentId, sender, receiver).transact({"from": w3.eth.accounts[1]})

#     return jsonify({'txHash': tx_hash.hex()})