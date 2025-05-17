file = open('example.txt', 'r')
line = file.readline()

# while line != '':
#    print(line)
#    line = file.readline()
# file.close()

while line !='':
    print(line)
    line=file.readline()
file.close()
