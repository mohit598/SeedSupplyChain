// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.19;

contract Transaction {
    
    // Map to store the parent products for each product ID
    mapping(uint256 => uint256[]) private parentProducts;
    
    // Map to store the senders for each transaction
    mapping(uint256 => address) private senders;
    
    // Map to store the receivers for each transaction
    mapping(uint256 => address) private receivers;

    // Global map for returning lineage
    mapping(uint256 => uint256[]) public lineageMap;

    // Event to log the addition of a transaction
    event TransactionAdded(uint256 indexed productId, uint256 indexed parentId, address payable sender, address payable receiver);

    function addTransaction(uint256 _productId, uint256 _parentId, address payable _sender, address payable _receiver) public {
        // Update the parent products map
        parentProducts[_productId].push(_parentId);
        
        // Record the sender and receiver of the transaction
        senders[_productId] = _sender;
        receivers[_productId] = _receiver;

        emit TransactionAdded(_productId, _parentId, _sender, _receiver);
    }
    
    function getBalance(address payable _owner) public view returns(uint256){
        return _owner.balance;
    }

    function getTransactionSender(uint256 productId) public view returns (address) {
        // Return the sender for the given product ID
        return senders[productId];
    }
    
    function getTransactionReceiver(uint256 productId) public view returns (address) {
        // Return the receiver for the given product ID
        return receivers[productId];
    }

    function getParent(uint256 productId) public view returns (uint256[] memory){
        return parentProducts[productId];
    }
}
