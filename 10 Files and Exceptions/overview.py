# Reading an Entire File
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
'''using with is advantageous than using open() and close(), beacause with closes file 
automatically once the access to file is no longer needed.'''

# Reading Line by Line
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

# Making a List of Lines from a File
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()     # readlines() reads line by line and stores them in a list
    for line in lines:
        print(line.rstrip())


# Writing to a File
# Writing to an Empty File
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

'''You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows
you to read and write to the file ('r+'). If you omit the mode argument, Python opens the file in 
read-only mode by default.'''

# Writing Multiple Lines
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# Appending to a File
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# Exceptions
# Using try-except Blocks
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# The else Block
'''---snip---'''
while True:
    '''---snip---'''
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# Handling the FileNotFoundError Exception
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# Failing Silently
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        '''---snip---'''
    except FileNotFoundError:
        pass                    # pass keyword simply tells nothing to do in this block
    else:
        '''---snip---'''

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

# Storing Data
# Using json.dump() and json.load()
'''writing to .json file'''
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)           # in json file stored data format would look same like python, [2, 3, 5, 7, 11, 13]

'''reading from .json file'''
import json
filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)