#GCD_calculation
def gcdCalculate(a,b):
    if(b>a):
        t=a
        a=b
        b=a
    while(b!=0):
        r=a%b
        a=b
        b=r
    return a
#Multiplicative_inverse_calculation
def mul_inverse ( phi_n , e):
    a1=1
    a2=0
    a3=phi_n
    b1=0
    b2=1
    b3=e
    while(True):
        q=int(a3/b3)
        t1=a1-q*b1
        t2=a2-q*b2
        t3=a3-q*b3
        a1=b1
        a2=b2
        a3=b3
        b1=t1
        b2=t2
        b3=t3
        if(b3==1):
            break
            
        elif(b3==0):
            break
    if(b2<0):
        b2=phi_n+b2
        return b2
    else:
        return b2
        
cypher_text=""
plain_text=""
file=open("RSA.txt")
f=file.read()
for z in f:
    m=ord(z)
    p=19
    q=17
    n=p*q
    e=1
    phi_n= (p-1)*(q-1)
    for x in range(2,phi_n):
        if(gcdCalculate(phi_n,x)==1):
            e=x
            break

    d = mul_inverse(phi_n,e)
    if(z!=" "): 
        c = (m**e)%n #Encryption
        encrypt=chr(c)
        m=c**d%n #decryption
        decrypt=chr(m)
    else:
        encrypt=" "
        decrypt=" "
    cypher_text=cypher_text+encrypt
    plain_text=plain_text+decrypt

print(cypher_text)
print(plain_text)