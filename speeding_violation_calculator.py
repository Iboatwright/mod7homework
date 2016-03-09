# speeding_violation_calculator.py
# Exercise selected: Chapter 7 program 4
# Name of program: Speeding Violation Calculator
# Description of program: This program takes two inputs from the user; 
#   the speed limit and the driver's speed.  It validates the speed limit
#   is 20mph or higher and 70mph or lower.  Then it calculates how much
#   over the limit the driver was going, if at all, and displays an
#   appropriate message. 
#
# Ivan Boatwright
# March 9, 2016

# Global Constants for speed limit constraints 
MIN_SPEED = 20
MAX_SPEED = 70

def main():
    # Local variables
    speedLimit = 0
    driverSpeed = 0
    judgement = ''
    
    # Display intro to user.
    fluffy_intro()

    # Get the speed limit.
    speedLimit = validate_user_input("speed limit")

    # Get the driver's speed.
    driverSpeed = validate_user_input("driver's speed")

    # Calculate driver's speed in reference to the speed limit.
    judgement = pass_judgement_on_driver(speedLimit, driverSpeed)

    # Display results.
    display_results(judgement)    
    
    
# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    pass


# This requests the user to input the promptTerm and tests if their input
#   is valid.  It returns the validated input.
def validate_user_input(promptTerm):
    # Local variable
    userInput = 0

    # Returns a valid speed integer.
    userInput = test_input(promptTerm)

    # Test if the entered speed limit is within the constraints.
    if promptTerm == "speed limit":
        # This loop repeats until a valid speed limit is entered.
        while MAX_SPEED < userInput or MIN_SPEED > userInput:
            print("Invalid ", promptTerm,". The maximum speed limit")
            print("is 70mph and minimum is 20mph.")
            userInput = test_input(promptTerm)
    return userInput


def test_input(promptTerm):
    # Local variable
    userInput = 0

    # Loops until the user enters a valid integer then the break statement
    #   exits the loop and the input is returned to the calling module.
    while True:
        try:
            userInput = int(prompt_user_for_item(promptTerm))
            break
        except:
            print("Error: Invalid input.  Only integers are accepted.")
    return userInput


# prompt_user_for_item accepts a string as an argument and returns the input
# as a String.
def prompt_user_for_item(promptTerm):
    # The user input is returned in an anonymous variable
    return input("Please enter the " + promptTerm + ".\n   >>> ")


# This compares the driver's speed to the speed limit and returns the results
#   as a string.
def pass_judgement_on_driver(speedLimit, driverSpeed):
    # Local variables
    judgement = ''
    overSpeed = 0

    # Test if the driver was actually speeding.
    if driverSpeed <= speedLimit:
        judgement = "The driver was not speeding.  He is free to go."
    else:
        # The driver must have been speeding.
        overSpeed = driverSpeed - speedLimit
        judgement = "The driver was going {}mph ".format(overSpeed)
        judgement += "over the limit.\nBook 'em Danno!"
    return judgement


# Displays whether or not the driver was speeding and offers a suggestion
#   on how to handle the situation.
def display_results(judgement):
    print(judgement)


# Call main module
main()