import sys

def encrypt():
    key = int(input("Key: "))
    n = int(input("n=(p*q)=: "))
    messageFilePath = input("File for encryption: ")

    messageFile = open(messageFilePath, 'r')

    content = messageFile.read()

    encryptedContent = ''
    for letter in content:
        encryptedContent += str(ord(letter) ** key % n) + " "

    encryptedMessageFile = open("encrypted_text.txt", "w")
    encryptedMessageFile.write(encryptedContent)

    messageFile.close()
    encryptedMessageFile.close()

if __name__ == '__main__':
    encrypt()