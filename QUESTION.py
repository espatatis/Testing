inp=0
wish='a'
product=1
sum=0
while wish!='q':
    wish=input("enter q to quit or any other key to continue>>")
    if wish=='q':
        break
    else:
        inp=int(input("enter value"))
        if inp%2==0:
            sum=sum+inp
        else:
            product=product*inp
print("the sum of even numbers is >>", sum)
print("the product of odd numbers is >>", product)
