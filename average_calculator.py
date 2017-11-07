# Created by: Julie Nguyen
# Created on: Oct 2017
# Created for: ICS3U
# This program calculates the user's average mark

# variables
number_of_inputs = 0
answer = 0

# input
user_input = int(input("Enter your mark: "))

# process
while user_input != -1:
    if user_input >= 0 and user_input <= 100:
        answer = answer + user_input
        number_of_inputs = number_of_inputs + 1
        final_mark = answer / number_of_inputs
        
        # output
        print(final_mark)
        
        # input
        user_input = int(input("Enter next mark (for final mark, enter -1): "))
        
    else:
        # output
        print("Invalid.")
        user_input = int(input("Please enter a valid mark: "))
        
print("Your final mark is " + str(final_mark))
