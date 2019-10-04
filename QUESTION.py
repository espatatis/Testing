input=0
wish='B'
product=1
sum=0
while wish!='q':
    wish=input("enter q to quit or any other key to continue>>")
    if wish=='q':
        break
    else:
        input=int(input("enter value"))
        if input%2==0:
            sum=sum+input
        else:
            product=product*input
print("the sum of even numbers is >>", sum)
print("the product of odd numbers is >>", product)
