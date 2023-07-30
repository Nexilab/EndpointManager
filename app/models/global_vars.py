import random

endpointUrl = {}

def addNewRpcUrl(blockchain: str, rpcUrl: str):
    if blockchain in endpointUrl:
        if not isinstance(endpointUrl[blockchain], list):
            endpointUrl[blockchain] = [endpointUrl[blockchain]]
        endpointUrl[blockchain].append(rpcUrl)
    else:
        endpointUrl[blockchain] = [rpcUrl]

def getRandomRpcUrl(blockchain: str):
    blockchain = blockchain.upper()
    if blockchain in endpointUrl and len(endpointUrl[blockchain]) > 0:
        return random.choice(endpointUrl[blockchain])
    else:
        return None
