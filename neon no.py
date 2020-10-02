
n=int(input("enter the no.:"))
x=n
s=0
sqr=n*n
while sqr>0:
    rem=sqr%10
    s=s+rem
    sqr=sqr//10
if(x==s):
    print(x,"is a neon no.")
else:
    print(x,"is not a neon no.")
