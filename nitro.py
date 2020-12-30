import os, time, random, sys
from colorium import *

uzunluk = 24

def genwin():
    os.system("cls")
    while True:
        print("https://discord.gift/", end="")
        for i in range(uzunluk):
            nitro = random.choice(chars)
            print(nitro, end="")
        
        print("")
        time.sleep(0.5)

def gen():
    os.system("clear")
    while True:
        print("https://discord.gift/", end="")
        for i in range(uzunluk):
            nitro = random.choice(chars)
            print(nitro, end="")
        
        print("")
        time.sleep(0.5)

            

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

oscheck = os.name

if oscheck == "nt":
    genwin()
elif oscheck == "posix":
    gen()



