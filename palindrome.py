print("palindrome number ")
n=int(input("Enter a number "))
k=str(n)
m=int(k[::-1])
if(n==m):
    print("palindrome",n)
else:
    print("not a palindrome",n)

