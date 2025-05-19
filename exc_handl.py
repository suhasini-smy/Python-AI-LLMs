
try:
   # f = open('example.txt','w')
    with open('example.txt','w') as f:
       f.write('hello dear 11\n')
except FileNotFoundError:
 print('file npt found')
finally:
    f.close()
