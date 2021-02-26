import subprocess
import json
from dotenv import load_dotenv
from web3 import Web3 
import os
from eth_account import Account 
from bit import wif_to_key
from bit.network import NetworkAPI

load_dotenv()

mnemonic = os.getenv('MNEMONIC')
conn = Web3(Web3.HTTPProvider("http://127.0.0.1:8545")))
print(mnemonic)

def der_wallet(coin):
    command = 'php derive -g --mnemonic --cols=path,address,privkey,pubkey --coin={coin} --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return. json.loads(output)

keys = json.loads(output)
print(keys)

coins = {'eth':derive_wallets(ETH), 'btc-test':derive_wallets(BTCTEST)}

def priv_key_to_account (coin, priv_key):
    if coin == ETH:
        return Account.privateKeytoAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

def create_tx(coin,account,to,amount):
    if coin == ETH:
        gasEstimate = conn.eth.estimateGas({
            "from":account.address,
            "to":to,
            "from":account.address,
            "value":amount
        })

        return {
            "to": to,
            "from": account.address,
            "value": amount,
            "gas": gasEstimate,
            "gasPrice": conn.eth.gasPrice,
            "nonce": conn.eth.getTransaction
            "chainID": conn.net.chainId
        }
        elif  coin == BTCTEST:
            result = PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTCTEST)])
        else:
            result = "Coin type not ETH or BTCTEST"
        return result
    
 def send_tx (coin, account, to, amount):
    if coin == 'ETH':
        tx_eth = create_tx(coin,account, to, amount)
        sign_tx = account.sign_transaction(tx_eth)
        result = conn.eth.sendRawTransaction(sign_tx.rawTransaction)
        print(result.hex())
        return result.hex()
    else:
        tx_btctest= create_tx(coin,account,to,amount)
        sign_tx = account.sign_transaction(tx_btctest)
        NetworkAPI.broadcast_tx_testnet(sign_tx)       
        return tx_hex
    

