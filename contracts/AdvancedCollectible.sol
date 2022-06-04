// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

contract AdvancedCollectible is ERC721URIStorage, VRFConsumerBase{
    uint256 public tokenCounter;
    bytes32 public keyhash;
    uint256 public fee;
    enum Breed{PUG, PUG1, PUG2}
    mapping(uint256=>Breed) public tokenIdToBreed;
    mapping(bytes32=>address) public requestIdToSender;
    event requestedCollectible(bytes32 indexed requestId, address requester);
    event breedAssigned(uint256 indexed tokenId, Breed breed);
    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyhash, uint256 _fee) public VRFConsumerBase(_vrfCoordinator, _linkToken) ERC721("Doggies", "DOG"){
        tokenCounter = 0;
        keyhash = _keyhash;
        fee = _fee;
    }

    function createCollectible() public returns(bytes32){
        bytes32 requestId = requestRandomness(keyhash,fee);
        requestIdToSender[requestId] = msg.sender;
        emit requestedCollectible(requestId, msg.sender);

    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber) internal override {
        Breed breed = Breed(randomNumber % 3);
        uint256 newtokenId = tokenCounter;
        tokenIdToBreed[newtokenId] = breed;
        emit breedAssigned(newtokenId, breed);
        address owner = requestIdToSender[requestId];
        _safeMint(owner, newtokenId);
        tokenCounter = tokenCounter + 1;
    }

    function setTokenURI(uint256 tokenId, string memory tokenURI) public {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: Caller is not owner nor approved");
        _setTokenURI(tokenId,tokenURI);
    }
}