num = int(input("Enter the value of n: "))

sum = 0

if num <= 0: 
   print("Enter a whole positive number!") 
else: 
   while num > 0:
        sum = sum + num
        num = num - 1;
    # displaying output
print("Sum of first", num, "natural numbers is: ", sum)
    

