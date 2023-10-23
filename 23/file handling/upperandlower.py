try:
    #Counter for characters...
    upper = 0
    lower = 0

    F=open("file.txt","r")
    while(True):
        data=F.read(1)
        if(data==""):
            break
        if (data.isupper()): 
                upper = upper + 1
        elif (data.islower()): 
                lower = lower + 1
                
    print(data,end='')
        
    print("Total Upper Case:",upper)
    print("Total lower Case:",lower)
except FileNotFoundError as e:
    print(e)
finally:
    F.close()