for i in range(999):
    n=i
    d=0
    s=0
    while n!=0:
        d=n%10
        s=s+d*d*d
        n=n/10
    if s==i:
        print("The number",i," is armstrong")
    
