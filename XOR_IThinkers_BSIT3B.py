# XOR Cipher
import math
import os
from tqdm import tqdm
from joblib import Parallel, delayed


def xor_hash_key(key):

    key_bytes = bytes(key, 'utf-8')
    hashed_key = bytearray()

    for i in range(len(key_bytes)):
        hashed_key.append(key_bytes[i] ^ 0xff)

    return hashed_key.hex()


def encrypt():
    file = open("myfile.txt", "r")
    msg = file.readlines()
    file.close()

    msg = msg[0]
    key = input("         Key: ")
    print("||============================||")
    # msg = input("         Plaintext: ")
    # print("||============================||")

    encryptHex = ""
    keyItr = 0

    for i in range(len(msg)):
        temp = ord(msg[i]) ^ ord(key[keyItr])
        encryptHex += hex(temp)[2:].zfill(2)
        keyItr += 1

        if keyItr >= len(key):
            keyItr = 0
    filename = "myfile.txt"
    os.rename(filename, filename + ".crypt")

    file = open("myfile.txt.crypt", 'w')

    file.write(xor_hash_key(key)+' ')
    file.write(format(encryptHex))
    file.close()

    results = [math.factorial(x) for x in tqdm(range(8000))]
    results = Parallel(n_jobs=2)(delayed(math.factorial)(x) for x in tqdm(range(8000)))

    print("||============================||")
    print("      Encrypted!")
    print("||============================||")


def decrypt():
    file = open("myfile.txt.crypt", 'r')
    pub = file.read()
    encryptkey, msgEncrypt = pub.split(' ')
    file.close()


    key = input("         Key: ")
    print("||============================||")

    if xor_hash_key(key) == encryptkey:

        hexToUni = ""
        for i in range(0, len(msgEncrypt), 2):
            hexToUni += bytes.fromhex(msgEncrypt[i:i + 2]).decode('utf-8')

        msgDecrypt = ""
        keyItr = 0
        for i in range(len(hexToUni)):
            temp = ord(hexToUni[i]) ^ ord(key[keyItr])
            msgDecrypt += chr(temp)
            keyItr += 1

            if keyItr >= len(key):
             keyItr = 0

            msgDecrypt = msgDecrypt

        filename = "myfile.txt.crypt"
        base = os.path.splitext(filename)[0]
        os.rename(filename, base)

        file = open("myfile.txt", 'w')
        file.write(format(msgDecrypt))
        file.close()

        results = [math.factorial(x) for x in tqdm(range(8000))]
        results = Parallel(n_jobs=2)(delayed(math.factorial)(x) for x in tqdm(range(8000)))
        print("||============================||")
        print("        Decrypted!")
        print("||============================||")
    else:
        print("Invalid Key entered!")

if __name__ == '__main__':

    print("||============================||")
    print("||            XOR             ||")
    print("||============================||")
    print("||       1 - Encrypt          ||")
    print("||       2 - Decrypt          ||")
    print("||============================||")

    choice = input("         Chose: ")
    print("||============================||")

    if choice.__eq__("1"):

        encrypt()

    elif choice.__eq__("2"):

        decrypt()

    else:
        print("Error: Invalid input.")
