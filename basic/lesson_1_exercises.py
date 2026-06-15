# ---------------------------------------------------------
# LESSON 1: EXERCISES
# ---------------------------------------------------------
# Answer the questions below. Once you are done, let me know
# and I will review and mark your answers!

# TASK 1: Variables and Basic Math
# Create two variables, `length` and `width`, and assign them values. 
# Calculate the area of the rectangle and print the result.
# Your code here:
length = 10
width = 20
area = length * width
print(area)



# TASK 2: String Manipulation
# Given the string `text = "  python PROGRAMMING  "`, use string methods to 
# remove the extra spaces, make it title-cased, and print it.
# Expected output: "Python Programming"
text = "  python PROGRAMMING  "
# Your code here:
text = "  python PROGRAMMING  "
remove_empty_space = text.strip()
print(remove_empty_space.title())


# TASK 3: Conditional Statements
# Write an if/elif/else block that checks a variable `score = 85`.
# Print "Grade: A" if score is 90 or above.
# Print "Grade: B" if score is between 80 and 89.
# Print "Grade: C" if score is between 70 and 79.
# Print "Fail" for anything below 70.
score = 85
# Your code here:
if score >= 90:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif 80 <= score <= 89:
    print("C")
else:
    print("Fail")



# TASK 4: Ternary Operator
# Use a ternary operator to set the variable `status` to "Passed" if `exam_score` is >= 50, 
# otherwise set it to "Failed". Print the `status`.
exam_score = 45
# Your code here:
status = "Passed" if exam_score >= 50 else "Failed"
print(status)


# TASK 5: Modulo and Logical Operators
# Create a variable `num = 15`. Check if it is divisible by both 3 and 5. 
# Print True if it is, False otherwise.
num = 15
# Your code here:
if num % 3 == 0 and num % 5 == 0:
    print(True)
else:
    print(False)


# TASK 6: For Loops
# Use a `for` loop with `range()` to print numbers from 0 to 5.
# Your code here:
for loop_num in range(0, 6):
    print(loop_num)


# TASK 7: Loops and Conditions
# Use a `for` loop to iterate through numbers from 1 to 15.
# Count how many numbers are odd, and print the final count at the end.
# Your code here:
for loop_long_numbers in range(1, 15):
    count_of_odd = 0
    if loop_long_numbers % 3 == 0:
        count_of_odd += 1
        print(count_of_odd)
else:
    print(loop_long_numbers)


# TASK 8: Functions
# Write a function called `welcome_message` that takes a `name` as an argument.
# It should print "Welcome aboard, [name]!". 
# Call the function with your own name.
# Your code here:
def welcome_message(name):
    print(f"Welcome aboard, {name}!")
welcome_message('Joshua')


# TASK 9: Functions with Default Parameters
# Write a function `calculate_discount(price, discount=10)` that returns the price after subtracting the discount.
# Call it once providing both arguments, and once providing only the price.
# Your code here:
def calculate_discount(price, discount=10):
    return price - discount
print(calculate_discount(50))


# TASK 10: Functions with Variable Arguments
# Write a function called `sum_numbers(*args)` that takes any number of arguments,
# adds them all together, and returns the total sum.
# Call it with (5, 10, 15) and print the result.
# Your code here:
def sum_numbers(*args):
    total_sum = 0
    for number in args:
        total_sum += number
    return total_sum

print(sum_numbers(5, 10, 15))
