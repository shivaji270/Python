print("prime number")
n=int(input("Enter a number"))
#n=3
for i in range(2,n):
    if(n%i==0):
        print("prime number")
        break
else:
    print("prime number")
