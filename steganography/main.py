import numpy as np
import cv2

def changeBit(RGB1, kanal, zmienNa):

    if zmienNa == 0:
        if (RGB1[kanal] % 2) == 1:
            RGB1[kanal] -= 1
    elif zmienNa == 1:
        if (RGB1[kanal] % 2) == 0:
            RGB1[kanal] += 1



def encode_message(img, wiadomosc, wysokoscObrazu, szerokoscObrazu):
    for x in range(len(wiadomosc) + 1):
        if x != len(wiadomosc):
            #znak w wiadomości jest zamieniany na jego reprezentację binarną a potem przekształcany do posaci 9-bitowej
            szyfrowanyZnak = str(bin(int(ord(wiadomosc[x]))))[2:].zfill(9) 
        else:
            #Jeżeli wiadomość się skończyła, to jako znacznik końca jest używany ciąg "111111111".
            szyfrowanyZnak = "111111111"

        print(szyfrowanyZnak)

        for y in range(3):
            # wartości składowych koloru danego piksela
            RGB = img[int((x * 3 + y) / szerokoscObrazu), int((x * 3 + y) % szerokoscObrazu)] 
            print('Before',RGB)
            
            for rgb in range(3):
                # dlugosc=len(str(bin(int(ord(wiadomosc[4])))))-2
                # print("dlugosc: "+str(dlugosc))
                if szyfrowanyZnak[y * 3 + rgb] == "1":
                    changeBit(RGB, rgb, 1)
                elif szyfrowanyZnak[y * 3 + rgb] == "0":
                    changeBit(RGB, rgb, 0)
            RGB =img[int((x * 3 + y) / szerokoscObrazu), int((x * 3 + y) % szerokoscObrazu)] 
            print('After:', RGB)
            print()

def decode_message(img2, wysokoscObrazu, szerokoscObrazu):
    decode_text = ""
    for x in range(int(szerokoscObrazu * wysokoscObrazu / 3)):
        znak = ""
        for y in range(3):
            for rgb in range(3):
                if img2[int((x * 3 + y) / szerokoscObrazu)][int((x * 3 + y) % szerokoscObrazu)][rgb] % 2 == 1:
                    znak += "1"
                elif img2[int((x * 3 + y) / szerokoscObrazu)][int((x * 3 + y) % szerokoscObrazu)][rgb] % 2 == 0:
                    znak += "0"
                else:
                    print("Obraz zaszyfrowany zawiera błędne bity!!!")

        if znak == "111111111":
            break
        znakDec = int(znak, 2) # zank jestkonwertowany z postaci binarnej na dziesiętną 
        decode_text += chr(znakDec)
        print(znak)
        print(chr(znakDec))

    return decode_text


def main():
    img = cv2.imread('parrots.jpeg')  
    #print(img[0][2])
    wiadomosc = input("Podaj swoją wiadomość: ")

    wysokoscObrazu, szerokoscObrazu = img.shape[:2]

    print("Długość wiadomości: " + str(len(wiadomosc)))
    print("Wymiary wczytanego obrazu: " + str(wysokoscObrazu) + " " + str(szerokoscObrazu))

    
    if (len(wiadomosc) * 3 + 3) > (wysokoscObrazu * szerokoscObrazu):
        print("Obraz jest zbyt mały, aby pomieścić tak dużą wiadomość!")
    else:
        encode_message(img, wiadomosc, wysokoscObrazu, szerokoscObrazu)

    cv2.imwrite('output.png', img)
    img2 = cv2.imread('output.png')  

    print("\n\n")
    decode_text = decode_message(img2, wysokoscObrazu, szerokoscObrazu)

    print("\nTwoja wiadomość: " + wiadomosc)
    print("Twoja odszyfrowana wiadomość: " + decode_text)

   


if __name__ == "__main__":
    main()
