import numpy as np
import string
#5*5 matrix format
array = np.full((5,5),None)
string="monarchy"
st=""
cypher=""
st=st+string
index=0
c=96
for i in range(97,123):
    if chr(i) in st:
        continue
    if chr(i)=='j':
        continue
    st=st+chr(i)
for i in range(5):
    for j in range(5):
        array[i][j]=st[index]
        index=index+1
print(array)
def index_finding(a):
    for i in range(5):
        for j in range(5):
            if(array[i][j]==a):
                return i,j
             
             
plain_text=input("Enter your word : ").lower()
plain_text=''.join(c for c in plain_text if c.isalpha())
print(plain_text)
#pairing
new_plain=""
i=0
bogus='x'
while i<len(plain_text):
    a=plain_text[i]
    b=plain_text[i+1] if i+1<len(plain_text) else ' '
    if b==' ':
        new_plain+=a+'z'
        break
    elif a==b:
        new_plain+=a+bogus
        i+=1
    else:
        new_plain+=a+b
        i+=2
print(new_plain)

#encryption
for i in range(0,len(new_plain),2):
    i1,j1=index_finding(new_plain[i])
    i2,j2=index_finding(new_plain[i+1])
    if(j1==j2):
        a1=array[(i1+1)%5][j1]
        a2=array[(i2+1)%5][j2]
    elif(i1==i2):
        a1=array[i1][(j1+1)%5]
        a2=array[i2][(j2+1)%5]
    else:
        a1=array[i1][j2]
        a2=array[i2][j1]
    cypher=cypher+a1+a2
print(cypher)