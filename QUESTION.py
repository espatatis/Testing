inp=0
wish='B'
product=1      ## used to store product of values
total_sum=0    ## used to store sum value 
while wish!='q':
    wish=input("enter q to quit or any other key to continue>>")
    if wish=='q':
        break
    else:
        inp=int(input("Please enter a valid value"))
        if inp%2==0:
            total_sum=total_sum+inp
        else:
            product=product*inp
print("the sum of even numbers is >>", total_sum)
print("the product of odd numbers is >>", product)
