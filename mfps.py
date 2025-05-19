import datetime
def calculate_year_of_birth(age):
    current_year=datetime.date.today().year 
    return current_year - age
def check_voting_eligiblity(age):
    return age>=18
def main():
    name = input("write your name?")

    while True:
        try:
            age  = int(input("write your age?"))
            break  # valid input, break the loop
        except ValueError:
            print("❌ Invalid age. Please enter a number (e.g., 25).")

    year_of_birth    = calculate_year_of_birth(age)    
    eligible_to_vote = check_voting_eligiblity(age)
    with open('user_info.txt',"w") as file:
        file.write(f"this is your age : {age}\n")
        file.write(f"this is your name : {name}\n")
        file.write(f"Year of birth: {year_of_birth}\n")
        if eligible_to_vote:
            file.write(f"Eligible to vote: Yes\n")
        else:
            file.write(f"Not eligible to vote: No\n")
if __name__=="__main__":
    main()