def pattern(x):

    num = 65

    for i in range (0, x):

        for j in range (0, i+1):
            
            ch = chr(num)
            
            print(ch ,end = " ")
            
            num += 1

        print(" ")


n = 7

pattern(n)
