from contract import create_contract
from web3 import Web3
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

longitud_origen = 4.6959324
latitud_origen = -74.0851391
longitud_destino = 4.581333314734242
latitud_destino = -74.09451253775883
longitud_actual = 4.581333314734242
latitud_actual = -74.09451253775883
account_1 = "0xd4D0506cE301cA9474AE2038F381121D002A7633"
private_key = "81ab1b5507fdfda8e8cf59b9a144975ca44b00a1eabf55ef08e88c9fbbd035bd"
account_2 = "0x31f5B799c53B883639E5e40b7626F156380033b2"


if longitud_destino == longitud_actual:
    tx_hash = create_contract(account_1, account_2, private_key)
    print(tx_hash)


