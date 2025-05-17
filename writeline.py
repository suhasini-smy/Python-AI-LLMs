line=['this is new line\n','this is second line\n']
file=open('example.txt','w')
file.writelines(line)
file.close()