v=input("Enter the elemnets bt space")
v1=v.split()
print(v1)

a,*b=v1

for i in b:
    print(i)

for i in v1[::-1]:
    print(i)



"""

def Palindrome(Input_string):
    n=len(Input_string)
    r_str=Input_string[::-1]
    if Input_string==r_str:
        print(Input_string, ' is palindrome')
    else:
        print(Input_string,' is not palindrome')


Palindrome('muu')

# function to check string is  
# palindrome or not  
def isPalindrome(str): 
  
    # Run loop from 0 to len/2  
    for i in range(0, len(str)):  
        if str[i] != str[len(str)-i-1]: 
            return False
    return True
  
# main function 
s = "malayalam"
ans = isPalindrome(s) 
  
if (ans): 
    print("Yes") 
else: 
    print("No") 
"""
