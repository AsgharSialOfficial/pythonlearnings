print(ord('A'))
print(chr(65))
def encryptmessage(message, shift):
    ciphermessage = ''
    for letter in message:
        if letter.isalpha():
            shifted = (ord(letter.upper())-ord('A')+ shift) %26
            ciphermessage+=chr(shifted+ord('A'))
        else:
            ciphermessage+=letter
    return ciphermessage

def deencryptmessage(message, shift):
    ciphermessage = ''
    for letter in message:
        if letter.isalpha():
            shifted = (ord(letter.upper())-ord('A')- shift) %26
            ciphermessage+=chr(shifted + ord('A'))
        else:
            ciphermessage+=letter
    return ciphermessage



message = input('Enter your message')
shift = int(input('Enter shift'))
encrypt = encryptmessage(message, shift)
decrypt = deencryptmessage('K CO CUIJCT HTQO QMCTC, NGCTPKPI ENQWF, EKUUR, EADGT UGEWTKVA',2)
print(encrypt)
print(decrypt)