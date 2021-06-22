calc_to_seconds = 24 * 60 * 60
calc_to_hours = 24
calc_to_minutes = 60 * 60
calc_to_miliseconds = 24 * 60 * 60 * 60
name_of_unit = "Hours"

def days_to_units(num_of_days):
    if num_of_days > 0:
     return f"{num_of_days} days are  {num_of_days * calc_to_hours} {name_of_unit}"
    elif num_of_days == 0:
     return "you enterned zero please enter number greater than zero"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)

        calculated_value = days_to_units(user_input_number)
        print(calculated_value)

    else:
        print("your input is not supported ! piss off")


user_input = input("hey user input days and this will convert to hours\n")
validate_and_execute()
