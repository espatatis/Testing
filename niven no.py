n=int(input("enter the no.:"))
x=n
s=0
while n>0:
    rem=n%10
    s=s+rem
    n=n//10
if((x%s)==0):
    print(x,"is niven no.")
else:
    print(x,"is not niven no.")
