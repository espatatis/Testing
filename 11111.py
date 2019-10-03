a=input("")
length=len(a)//2
middle=8
position=8
i=0
j=1
while i<length+2:
     if i==0 or i==length+1:
        print("#"*19)
     else:
         
         while j<len(a)+1:
             if a[j-1]=="u":
                print("#"+" "*(position+int(a[j]))+"*"+" "*(17-position-int(a[j])-1)+"#")
                position=position+int(a[j])
                
             elif a[j-1]=="d":
                print("#"+" "*(position-int(a[j]))+"*"+" "*(17-position+int(a[j])-1)+"#")
                position=position-int(a[j])+1
             j=j+2
             break        
                        
     i=i+1
    
