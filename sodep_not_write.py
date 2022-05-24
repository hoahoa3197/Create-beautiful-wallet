#%%
import os
import requests
import json
from web3 import Web3
from web3.auto import w3
from threading import Thread
from functools import partial
# from tqdm import tqdm

def append_new_line(file_name, text_to_append):
    with open(file_name, "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(text_to_append)

def create_wallet_sodep(amount,export_path):
    try:
        for i in range(amount):
            account = w3.eth.account.create('KEYSMASH FDHGDFGFDFVSDFGHUTY 1999')
            conditions = ['11111','22222','333333','55555','66666','88888','99999','00000','12345','56789','336699','686868']
            wallet_addr = str(account.address)
            valid_wallet = wallet_addr[-6:]
            valid_wallet = valid_wallet.lower()+'|'
            for condition in conditions:
                if condition+'|' in valid_wallet:
                    print(wallet_addr)
                    append_new_line(export_path,account.address+'|'+account.privateKey.hex())
                    break
        print('Create wallet done!')
        return True
    except:
        return False
curdir = os.path.dirname(__file__)
# Config
export_path = os.path.join(curdir,'wallets_sodep_checked_1.txt')
amount = 30
num_threads = 40000
# End Config
worker_task = partial(create_wallet_sodep,amount,export_path)
workers = []
# pbar = tqdm(total=amount,ncols=80)
# pbar.set_description(desc='Creating wallets')

for i in range(20):
    for i in range(num_threads):
        worker = Thread(target=worker_task)
        worker.start()
        print('Start thread '+str(i))
        workers.append(worker)
    for worker in workers:
        # pbar.update(1)
        worker.join()
# pbar.close()
print('Create wallets done!')


