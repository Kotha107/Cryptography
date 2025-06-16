def primitive_root(p):
    for g in range(2,p):  
        a = set()
        for i in range(p):
            value = (g**i)%p
            if value in a:
                break
            else:
                a.add(value)
        if(len(a)==p-1):
            break
    return g
x_a=int(input("Enter A's private key : "))
x_b=int(input("Enter B's private key : "))
p = int(input("enter a prime number "))
g=primitive_root(p)
y_a=g**x_a%p
y_b=g**x_b%p
k=y_b**x_a%p
print("A's secret key :",k)
k=y_a**x_b%p
print("B's secret key : ",k)