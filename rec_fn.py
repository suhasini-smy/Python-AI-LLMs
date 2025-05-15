# def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n - 1)
# result = factorial(2)
# print(result)

def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)

r= fact(4)
print(r)
