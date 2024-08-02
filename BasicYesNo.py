# Basic code that takes the user's input and provides a response based on whether the input is positive, negative, or zero.
# This simple demonstration showcases basic computer decision-making, which forms the foundation of more complex logic in programming.
# In our daily lives, we encounter many decisions that can be boiled down to simple yes or no answers, though often more complex.
# Similarly, in AI, we begin with simple decisions and gradually introduce more complex logic.
# The goal is to build on this foundation and develop more sophisticated decision-making capabilities in our code.

def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Get user input
num = float(input("Enter a number to review if it is positive or negative: "))

# Check the number
result = check_number(num)

# Display the result
print(f"The number {num} is {result}.")
