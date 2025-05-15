
def fn_d(name):
  return print(f"my name is  {name}")

def add_num(a,b):
  result=a+b
  return result

#fn_d('jeya')
# res = add_num(1,3)
# print(f"the sum of two number{res}")

def say_hello1(name="hello world"):
  print(f"output:{name}")

# say_hello1()
# say_hello1('suhas')

def pr_arg(*args):
  for arg in args:
    print(arg)

# pr_arg(1,2,3,6)

def pr_args(**args):
  for key,value in args.items():
    print("--key:",key,",--value:",value)

pr_args(name="suhas",age="25")


