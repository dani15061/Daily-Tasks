import os   
cwd = os.getcwd()  
print("Current working directory:", cwd)
'''
import os  
def current_path():  
    print("Current working directory before")  
    print(os.getcwd())  
    print()   
current_path()  
os.chdir('../')  
current_path()  


print(os.name) 

try: 
    filename = 'GFG.txt'
    f = open(filename, 'rU') 
    text = f.read() 
    f.close()   
except IOError: 
    print('Problem reading: ' + filename)

fd = "file.txt" 
file = open(fd, 'w') 
file.write("Hello") 
file.close() 
file = open(fd, 'r') 
text = file.read() 
print(text) 
file = os.popen(fd, 'w') 
file.write("Hello") 

fd = "file.txt"
os.rename(fd,'New.txt') 

fd = "file.txt"
file = open(fd, 'r') 
text = file.read() 
print(text) 
os.close(file) 
'''