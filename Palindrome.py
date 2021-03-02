print("***********************Palindrome or not*****************************")
n = input("Enter a String: ")
n = n.casefold()
r = reversed(n)
if list(n)==list(r):
    print(n ," is a palindrome")
else :
    print(n, " is not a palindrome")
