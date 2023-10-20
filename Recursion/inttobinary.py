def decToBinary(num):
    if (num == 0):
        return

    decToBinary(num // 2)
    print(num % 2,end="")


#calling the function
n = 45
print("Decimal equivalent of",n,"is ",end="")
decToBinary(n)