import cv2
from pyzbar.pyzbar import decode
from datetime import datetime
from time import sleep
import numpy as np
import random
import pyqrcode
import json
from web3 import Web3
import tkinter as tk
from datetime import datetime
from datetime import timedelta
import geocoder

ganach_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganach_url))
web3.eth.defaultAccount = web3.eth.accounts[1]


abi = json.loads('[{"inputs":[],"name":"end","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"z","type":"string"}],"name":"erase","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_code","type":"string"},{"internalType":"string","name":"_date","type":"string"},{"internalType":"string","name":"_loc","type":"string"},{"internalType":"string","name":"_ex","type":"string"}],"name":"factory","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"z","type":"string"}],"name":"getindex","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_date","type":"string"},{"internalType":"string","name":"_loc","type":"string"}],"name":"pharmacy","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_date","type":"string"},{"internalType":"string","name":"_loc","type":"string"}],"name":"saller","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"show","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]')
address = web3.toChecksumAddress("0xBbAfc5183d69D53a32ac436Fd8Ee7EaFdB32aeE9")
contract = web3.eth.contract(address=address , abi= abi)


def scaner1():
    cn = 0

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    f = True
    nstr = 0
    while f and cn < 100:
        sleep(0.1)
        cn += 1
        success, img = cap.read()
        for barcode in decode(img):
            myData = barcode.data.decode('utf-8')
            print(myData)
            if len(myData) > 3:
                f = False
                nstr = 1

            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (255, 0, 255), 5)
            pts2 = barcode.rect
            cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (255, 0, 255), 2)

        cv2.imshow('Result', img)
        cv2.waitKey(1)
    cap.release()  #################
    cv2.destroyAllWindows()
    if nstr == 0:
        return '0'
    else:
        return myData

choices = list(range(52, 80))
random.shuffle(choices)
def getQR():
    
    x = choices.pop()
    y = choices.pop()
    code = x * y
    qr = pyqrcode.create(str(code))
    print(qr)
    qr.png(str(code) + '.png', scale=8)
    return str(code)


def try1():
    ganach_url = "http://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganach_url))
    web3.eth.defaultAccount = web3.eth.accounts[1]


    abi = json.loads('[{"inputs":[],"name":"end","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"z","type":"string"}],"name":"erase","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_code","type":"string"},{"internalType":"string","name":"_date","type":"string"},{"internalType":"string","name":"_loc","type":"string"},{"internalType":"string","name":"_ex","type":"string"}],"name":"factory","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"z","type":"string"}],"name":"getindex","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_date","type":"string"},{"internalType":"string","name":"_loc","type":"string"}],"name":"pharmacy","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_date","type":"string"},{"internalType":"string","name":"_loc","type":"string"}],"name":"saller","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"show","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]')
    address = web3.toChecksumAddress("0xBF818Fdd62C137c2f56d6a64FB782C640e1F5Dbc")
    contract = web3.eth.contract(address=address , abi= abi)

    #getQR()
    tx_hash = contract.functions.factory('zertic','1234','22/3/2020','mataria','expireDate').transact()
    tx_hash = contract.functions.getindex('1234').transact()
    print(contract.functions.show().call())
    #saller part
    tx_hash = contract.functions.saller('23/3/2020','helmia').transact()
    print(contract.functions.show().call())
    #pharmacy part
    tx_hash = contract.functions.pharmacy('24/3/2020','zaiton').transact()
    print(contract.functions.show().call())
    #final part
    tx_hash = contract.functions.getindex('2345').transact()
    print(contract.functions.show().call())
    #delete part
    tx_hash = contract.functions.getindex('1234').transact()
    print(contract.functions.show().call())
    tx_hash = contract.functions.end().transact()
    tx_hash = contract.functions.erase('1234').transact()
    print(contract.functions.show().call())
    tx_hash = contract.functions.end().transact()
    print(contract.functions.show().call())

def ui():
    def factoryx():
        n = entery.get()
        ex=datetime.today()+ timedelta(days=730)
        ex=ex.strftime('%Y-%m-%d')
        now=datetime.today().strftime('%Y-%m-%d')
        myloc = geocoder.ip('me')

        l=myloc.city
        tx_hash = contract.functions.factory(n,getQR(),now,l,ex).transact()
        print(now)

    def saller():
        qr=scaner1()
        print(qr)
        now=datetime.today().strftime('%Y-%m-%d')
        myloc = geocoder.ip('me')

        l=myloc.city
        tx_hash = contract.functions.getindex(qr).transact()
        tx_hash = contract.functions.saller(now,l).transact()
        print(contract.functions.show().call())
        lbl3.config(text='done')
        lbl3.grid(row=4, column=1)
    def pharmacy():
        qr=scaner1()
        print(qr)
        now=datetime.today().strftime('%Y-%m-%d')
        myloc = geocoder.ip('me')

        l=myloc.city
        tx_hash = contract.functions.getindex(qr).transact()
        tx_hash = contract.functions.pharmacy(now,l).transact()
        print(contract.functions.show().call())
        lbl31.config(text='done')
        lbl31.grid(row=6, column=2)
    
    def usr():
        qr=scaner1()
        print(qr)
        tx_hash = contract.functions.getindex(qr).transact()
       
        z = contract.functions.show().call()
        print(z)
        lb = tk.Label()
        lb.config(text="name:{}date:{}exp:{}".format(z[0],z[2],z[8]))
        lb.grid(row=10, column=3)
        
        




    root = tk.Tk()
    root.geometry("730x340")
    lbl0 = tk.Label()
    lbl0.config(text='factory part ')
    lbl0.grid(row=0, column=1)

    lbl1 = tk.Label()
    lbl1.config(text='add medicine')
    lbl1.grid(row=1, column=0)

    entery = tk.Entry(width=15)
    entery.grid(row=1, column=1)

    btn1 = tk.Button(text="add", command=factoryx)
    btn1.grid(row=1, column=2)
    
    lbl2 = tk.Label()
    lbl2.config(text='==========')
    lbl2.grid(row=2, column=0)
    lbl3 = tk.Label()
    lbl3.config(text='saller')
    lbl3.grid(row=3, column=1)
    btn1 = tk.Button(text="scane", command=saller)
    btn1.grid(row=4, column=0)
    lbl4 = tk.Label()

    lbl21 = tk.Label()
    lbl21.config(text='==========')
    lbl21.grid(row=5, column=0)
    lbl31 = tk.Label()
    lbl31.config(text='pharmacy')
    lbl31.grid(row=6, column=1)
    btn11 = tk.Button(text="scane", command=pharmacy)
    btn11.grid(row=6, column=0)
    lbl41 = tk.Label()

    lbl21 = tk.Label()
    lbl21.config(text='==========')
    lbl21.grid(row=7, column=0)
    lbl31 = tk.Label()
    lbl31.config(text='user ')
    lbl31.grid(row=8, column=1)
    btn11 = tk.Button(text="scane", command=usr)
    btn11.grid(row=9, column=0)
  
    



    root.mainloop()

ui()