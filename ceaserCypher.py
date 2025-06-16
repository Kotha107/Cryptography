x="heloo its kotha"
str=""
#encryption
for i in x:
    if(i!=" "):
        z=chr((ord(i)+3)%256)
    else:
        z=" "
    str=str+z
print(str)
#decryption
original=""
for i in str:
    if(i!=" "):
        z=chr((ord(i)-3)%256)
    else:
        z=" "
    original=original+z
print(original)
    