import os, time, random, sys
from colorium import *


uzunluk = 58
chars = "-abcdefghijklmnopq_rstu.vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"


def gen():
    os.system("clear")
    while True:
        print("N", end="")
        for i in range(uzunluk):
            token = random.choice(chars)
            print(token, end="")
        
        print("")
        time.sleep(0.5)





def genwin():
    os.system("cls")
    while True:
        print("N", end="")
        for i in range(uzunluk):
            token = random.choice(chars)
            print(token, end="")
        
        print("")
        time.sleep(0.5)



oscheck = os.name

if oscheck == "nt":
    genwin()
elif oscheck == "posix":
    gen()