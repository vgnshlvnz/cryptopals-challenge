import base64

hexStr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
answer = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

print(base64.b64encode(bytes.fromhex(hexStr)).decode('utf-8'))

def hex2base64BaselineCalc():
    return base64.b64encode(bytes.fromhex(hexStr))


def hex2base64(inputStr):
    ''' The program will convert predefined hex string to base64 string
    if no input is given'''
    if inputStr == None:
        hex2base64BaselineCalc()
    else:
        tempBytes = bytes.fromhex(inputStr)
        base64Str = base64.b64encode(tempBytes)
        return base64Str
