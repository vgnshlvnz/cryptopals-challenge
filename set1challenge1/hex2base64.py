#!/usr/bin/env python3
''' Import base64 encoding function from base64 module 
'''
from base64 import b64encode as ncode2base64
from sys import argv as argument

hexStr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
answer = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

#print(base64Encode(bytes.fromhex(hexStr)).decode('utf-8'))

def hex2base64BaselineCalc():
    tempBytes = bytes.fromhex(hexStr)
    base64ResultStr = ncode2base64(tempBytes).decode('utf-8')
    if base64ResultStr != answer:
        return print('String Compare Failed')
    else:
        return print('String Compare Successful')



def hex2base64(inputStr):
    ''' The program will convert predefined hex string to base64 string
    if no input is given'''
    if inputStr == None:
        hex2base64BaselineCalc()
    else:
        tempBytes = bytes.fromhex(inputStr)
        base64Str = ncode2base64(tempBytes)
        return base64Str


def main():
    if len(argument) >= 3:
        print("argument more than 3, unable to process further.")
    else:
        output = hex2base64(str(argument[1]))
        print(output)


if __name__ == '__main__':
    main()
