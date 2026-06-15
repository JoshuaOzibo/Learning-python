# print("Hello World")
# print("*" * 10)
# print(10 < 5)
# print(5 > 10)
# print(10 == 5)
# print(10 != 5)


students_count = 1000
number = 5
# print(number == students_count)
my_name = "Joshua"

printName = len(my_name)


# print(my_name[0 : ])


first = "Joshua"
last = "Chinedu"
# print(f"{first.upper()} {last}")

name = "Joshua chinedu ozibo"

print(name.upper())
print(name.lower())
print(name.title())
print(name.endswith("o"))
# to remove white space .....
print(name.strip())
# to find the index of a string
print(name.find("Jo")) 
print(name.replace("J", " ")) 
# check if something exist
print("Josh" in name) 
# check if something does not exist
print("pro" not in name)

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
# return an integer instead of a float meaning 5.3 or 5.6 will be 5
print(10 // 6)
# returns a remainder
print(10 % 3)

print(10 ** 3)

temperature = 50

if temperature > 30:
    print('temp is greater than 30')
elif temperature < 30:
    print("temp is less than 30")
else:
    print("temp is not greater than 30")


# same way to do it using ternary operator
student_age = 22
if student_age > 18:
    print("eligable")
else:
    print("Not eligable")
    # same as 
message = "student is eligable" if student_age >= 18 else "student is not eligable"
print(message)

# logical operator like "and" "or" "not" 
max_age = 20 
lucy_age = 20

if max_age and lucy_age <= 5:
    print('they are teens')
else:
    print("they are youth")

# loops
for number in range(4):
    print("multiple times", number)


    # nested loop
# for x in range(5):
#     for y in range(3):
        # print(f"({x}, {y})")

print(type(range))

# while loop
# numberCount = 100
# while numberCount > 0:
#     print(numberCount)
#     numberCount //= 2

evenCount = 0
for fullNum in range(1, 10):
    if fullNum % 2 == 0:
        evenCount += 1
        print(fullNum)
    
print(f"the total num of even num is {evenCount}")

# functions
def greet(name):
    print(f"Hello {name}")

greet('Joshua')

def decrease(number, count = 5):
    return number - count
print(decrease(10))


def multiple_numbers(*numbers):
    totalNum = 1
    for number in numbers:
        totalNum *= number
    return totalNum

# print(multiple_numbers(1, 2, 3, 4, 5))
