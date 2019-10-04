n=int(input('enter a number between 5-10: '))
l=[]
for i in range(0,n):
    l.append(input())
#for k in range(0,n):
  #  print(l[k])
count=0
for j in range(0,n):
    if (l[j] == 5):
        count=count+1
print('The number 5 is',count,'times in the above list.')
        
    
