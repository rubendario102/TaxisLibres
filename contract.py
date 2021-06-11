from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())
print(web3.eth.blockNumber)



def create_contract(account_1, account_2, private_key):

    #Get the nonce
    nonce = web3.eth.getTransactionCount(account_1)
    #Build a tx
    tx = {
        'nonce': nonce,
        'to': account_2,
        'value': web3.toWei(1, 'ether'),
        'gas' :  2000000,
        'gasPrice' : web3.toWei('50', 'gwei')
    }
    #Signd a tx
    signed_tx = web3.eth.account.signTransaction(tx, private_key)
    # send tx
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    # get tx hash
    return web3.toHex(tx_hash)
