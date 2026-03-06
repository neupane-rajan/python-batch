"""# a number is palindrome if it is same form front and back
 121
 111
 1331
 321 not a palindrome number
 step to check palindrome:
 #first take a number
 reverse the number
 comapre orginal number and reverse number
 if same then number is palindrome
"""

num = int(input("Enter a number: "))
orginal = num
reverse = 0

while num>0:
    digit  = num%10
    reverse = reverse*10+digit
    num = num//10
if orginal == reverse:
    print("number is palindrome")
else:
    print("number is not a palidrome")