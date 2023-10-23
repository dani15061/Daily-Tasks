def count():
    file = open("article.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word == 'is' or word =='the':
            count+=1
    print(count)
    file.close()

count()