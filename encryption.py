def encrypt(text,s):
    result=" "
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
            result+=chr((ord(chor)+s-65)%26+65)
        else:
            result+=chr((ord(char)+s-97)%26+97)
    return result
text=input("enter the text:")
s=4
print("plain ext:",text)
print("shift pattern:",str(s))
print("cipher:",encrypt(text,s))
