def fact(n):
  if(n==1):
    return n
  else:
    return n*(fact(n-1))


num = int(input("Enter a number: "))

if num<0:
  print("Negative numbers are not allowed.")
elif num==0:
  print("Factorial is: 1")
else:
  print("Factorial is: ",fact(num))