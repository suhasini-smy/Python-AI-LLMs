
while True:
    user_input=input("Enter a number or type 'quit':")
    if user_input=="quit":
        break 
    elif user_input.isdigit():
        print("You Entered value:",user_input)
        break
    else:
        print('Invalid input, please try again')

