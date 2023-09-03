
print("Welcme to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")

def encryption():
    print("Encrypting...")
    message = input("Enter your message: ")
    key = int(input("Enter your key between 1 - 94: "))
    encryptedText = ""
    for i in range(0,len(message)):
        temp = ord(message[i])+key
        if temp > 126:
            temp = temp-127+32
        encryptedText += chr(temp)
    print("Encrypted:", encryptedText)
    main()
    
def decryption():
    print("Decrypting...")
    message = input("Enter encrypted text: ")
    key = int(input("Enter your key between 1 - 94: "))
    decryptedText = ""
    for i in range(0,len(message)):
        temp = ord(message[i])-key
        if temp <32:
            temp = temp+127-32
        decryptedText += chr(temp)
    print("Decrypted:", decryptedText)
    main()
        
if __name__ == "__main__":
    main()
