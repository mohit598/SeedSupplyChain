// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.19;

contract fyp {
    
    // Map to store the parent products for each product ID
    mapping(uint256 => uint256[]) private parentProducts;
    
    // Map to store the senders for each transaction
    mapping(uint256 => address) private senders;
    
    // Map to store the receivers for each transaction
    mapping(uint256 => address) private receivers;

    // Event to log the addition of a transaction
    event TransactionAdded(uint256 indexed productId, uint256 indexed parentId, address sender, address receiver);

    function addTransaction(uint256 _productId, uint256 _parentId, address _sender, address _receiver) public {
        // Add the transaction and update the parent products map
        parentProducts[_productId] = parentProducts[_parentId];
        parentProducts[_productId].push(_parentId);
        
        // Record the sender and receiver of the transaction
        senders[_productId] = _sender;
        receivers[_productId] = _receiver;
        
        emit TransactionAdded(_productId, _parentId, _sender, _receiver);
    }

    function getProductLineage(uint256 productId) public view returns (uint256[][] memory) {
        // Return the parent products for the given product ID as a 2D array
        uint256[][] memory lineage = new uint256[][](parentProducts[productId].length);
        for (uint i = 0; i < parentProducts[productId].length; i++) {
            lineage[i] = parentProducts[productId];
        }
        return lineage;
    }
    
    function getTransactionSender(uint256 productId) public view returns (address) {
        // Return the sender for the given product ID
        return senders[productId];
    }
    
    function getTransactionReceiver(uint256 productId) public view returns (address) {
        // Return the receiver for the given product ID
        return receivers[productId];
    }
}
