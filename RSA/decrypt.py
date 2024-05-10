import sys

def decrypt():
    key = int(input("Key: "))
    n = int(input("n=(p*q)=: "))
    # encryptedMessageFilePath = input("Encrypted message file: ")

    encryptedMessageFile = open("encrypted_text.txt", 'r')

    numbers = encryptedMessageFile.read().split(' ')[:-1]

    message = ''
    for number in numbers:
        message += chr(int(number) ** key % n)

 
    with open("decrypted_text.txt", "w", encoding="utf-8") as messageFile:
        messageFile.write(message)

    encryptedMessageFile.close()



if __name__ == '__main__':
    decrypt()