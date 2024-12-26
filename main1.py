print('-------------------------------')
file=open('text.txt', 'r')
for i in file.readlines():
    if(i.startswith('It')):
        print(i)
    
file.close()