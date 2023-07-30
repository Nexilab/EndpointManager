from enum import StrEnum, verify, UNIQUE, auto

class BlockchainEnum(StrEnum):
    BSC = "BSC"
    ETHEREUM  = "ETHEREUM"
    LITECOIN  = "LITECOIN"
    POLYGON   = "POLYGON"
    MUMBAI    = "MUMBAI"

class UserTypeEnum(StrEnum):
    USER = auto()
    ADMIN = auto()
    GOD = auto()


def getBlockchainEnum(blockchain: str) -> BlockchainEnum:
    blockchain = blockchain.upper()

    if blockchain in [item.value for item in BlockchainEnum]:
        return BlockchainEnum(blockchain)

    return None
