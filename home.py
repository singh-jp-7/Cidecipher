import math


def encrypt():
    plain_text = input("Enter the plain text:\n ")
    print("Which technique you want to use?\n")
    cipher = int(input("1. Addition Cipher\n2. Multiplicative Cipher\n"))

    if cipher == 1:
        def ac(plain_text):
            key = int(input("Enter the key: "))
            cip1 = []
            for char in plain_text.lower():
                if char == " ":
                    char1 = " "
                    cip1.append(char1)
                else:
                    char1 = ord(char) - 96
                    char1 = (char1 + key)%26
                    cip = chr(char1 + 96)
                    cip1.append(cip)
            cipher_text = ""
            cipher_text = cipher_text.join(cip1)   
            print("The cipher text is ", cipher_text)
        ac(plain_text)
        
    else:
        def mc(plain_text):
            key = int(input("Enter the key: "))
            cip1 = []
            for char in plain_text.lower():
                if char == " ":
                    char1 = " "
                    cip1.append(char1)
                else:
                    char1 = ord(char) - 96
                    char1 = (char1 * key)%26
                    cip = chr(char1 + 96)
                    cip1.append(cip)
            cipher_text = ""
            cipher_text = cipher_text.join(cip1)   
            print("The cipher text is ", cipher_text)
        mc(plain_text)


def decrypt():
    cipher_text = input("Enter the ciphered text:\n ")
    print("Enter the encryption technique used: \n")
    decipher = int(input("1. Addition Cipher\n2. Multiplicative Cipher\n"))
    if decipher == 1:
        def acd(cipher_text):
            key = int(input("Enter the decryption key: "))
            cip1 = []
            for char in cipher_text.lower():
                if char == " ":
                    char1 = " "
                    cip1.append(char1)
                else:
                    char1 = ord(char) - 96
                    char1 = (char1 - key)%26
                    cip = chr(char1 + 96)
                    cip1.append(cip)
            plain_text = ""
            plain_text = plain_text.join(cip1)   
            print("The deciphered text is: ", plain_text)
        acd(cipher_text)
    else:
        def mcd(cipher_text):
            key = int(input("Enter the decryption key: "))
            
            cip1 = []
            for char in cipher_text.lower():
                if char == " ":
                    char1 = " "
                    cip1.append(char1)
                else:
                    char1 = ord(char) - 96
                    def modInverse(char1): 
                        char1 = char1 % 26
                        for keyinv in range(1, 26): 
                            if ((char1 * keyinv) % 26 == 1): 
                                return keyinv 
                            else:
                                return 1
                    
                    char1 = (char1 * modInverse(char1))%26
                    cip = chr(char1 + 96)
                    cip1.append(cip)
            plain_text = ""
            plain_text = plain_text.join(cip1)   
            print("The deciphered text is: ", plain_text)
        mcd(cipher_text)

options = int(input("Enter what you want to do: \n1. Encrypt! \n2. Decrypt\n"))

if options == 1:
    encrypt()
else:
    decrypt()








