// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";


contract SimpleCollectible is ERC721URIStorage{
    uint256 public tokenCounter;
    constructor() public ERC721 ("Doggie", "DOG"){
        tokenCounter = 0;
    }

    function createCollectible(string memory _tokenUri) public returns (uint256){
        uint256 newtokenid = tokenCounter;
        _safeMint(msg.sender, newtokenid);
        _setTokenURI(newtokenid, _tokenUri);
        tokenCounter = tokenCounter + 1;
        return newtokenid;
    }
}