file=open('text.txt', 'r')
print(file.read())
file.close()
print('-------------------------------')

file=open('text.txt', 'r')
print(file.read(7))
file.close()

print('-------------------------------')
file=open('text.txt', 'r')
print('reading the first line..........')
print(file.readline())
file.close()

print('-------------------------------')
file=open('text.txt', 'r')
print('reading the first three line..........')
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

print('-------------------------------')
file=open('text.txt', 'r')
for i in file:
    print(i)
file.close()