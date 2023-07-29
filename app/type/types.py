from enum import Enum

class BlockchainEnum(str, Enum):
    BSC = "bsc"
    ETHEREUM = "Ethereum"
    LITECOIN = "Litecoin"
    POLYGON  = "Polygon"
    MUMBAI   = "Mumbai"

class UserTypeEnum(Enum):
    USER = "user"
    ADMIN = "ADMIN"
    GOD = "GOD"
