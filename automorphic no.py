n=int(input("enter any no.:"))
x=n
d=0
while n>0:
    d=d+1
    n=n//10
p=x%(10**(d-1))
if(p**p)==x:
    print(n," is authomorphic no.")
else:
    print(n,"is not a automorphic no.")
    
