a=input("")
length=len(a)//2
middle=8
position=9
i=0
j=1
while i<length+2:
     if i==0 or i==length+1:
        print("#"*19)
     else:
         
         while j<len(a)+1:
             t=int(a[j])
             if a[j-1]=="u":
                 for k in range(19):
                     if k==0:
                         print("#",end='')
                     elif k==(position+t):
                         print("*",end='')
                     elif k==18:
                         print("#")
                     else:
                         print(" ",end='')
                 position=position+t
             elif a[j-1]=="d":
                 for k in range(19):
                     if k==0:
                         print("#",end='')
                     elif k==position-t:
                         print("*",end='')
                     elif k==18:
                         print("#")
                     else:
                         print(" ",end='')
                 position=position-t
             j=j+2
             
     i=i+1
    
