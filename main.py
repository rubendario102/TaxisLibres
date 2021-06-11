from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())
print(web3.eth.blockNumber)

account_1 = "0xd4D0506cE301cA9474AE2038F381121D002A7633"
account_2 = "0x31f5B799c53B883639E5e40b7626F156380033b2"
private_key = "81ab1b5507fdfda8e8cf59b9a144975ca44b00a1eabf55ef08e88c9fbbd035bd"

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
print(web3.toHex(tx_hash))