def encrypt(text,key):
    data = ''
    text = text[::-1]
    print(text)
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
           data += chr((ord(char)+key-65) %26 +65)
    
        else:
           data += chr((ord(char)+key-97)%26+97)
    return(data)
sample = input("Enter Plain text : ")
key1 = int(input("Enter key : "))
print("Ciper test is",encrypt(sample,key1))

