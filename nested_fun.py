
def outer_fun():
    def inner_fun():
        print("This is Inner Function")
    inner_fun()
outer_fun()