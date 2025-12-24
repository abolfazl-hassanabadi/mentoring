"""

Write a separate program to accomplish each of these exercises. Save each pro-
gram with a filename that follows standard Python conventions, using lowercase
letters and underscores, such as simple_message.py and simple_messages.py.
2-1. Simple Message: Assign a message to a variable, and then print that
message.
2-2. Simple Messages: Assign a message to a variable, and print that message.
Then change the value of the variable to a new message, and print the new
message.
Save each of the following exercises as a separate file, with a name like name
_cases.py. If you get stuck, take a break or see the suggestions in Appendix C.
2-3. Personal Message: Use a variable to represent a person’s name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”
2-4. Name Cases: Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case.
2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never
tried anything new.”
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous
person’s name using a variable called famous_person. Then compose your mes-
sage and represent it with a new variable called message. Print your message.
2-7. Stripping Names: Use a variable to represent a person’s name, and
include some whitespace characters at the beginning and end of the name.
Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
2-8. File Extensions: Python has a removesuffix() method that works exactly
like removeprefix(). Assign the value 'python_notes.txt' to a variable called
filename. Then use the removesuffix() method to display the filename without
the file extension, like some file browsers do.
2-9. Number Eight: Write addition, subtraction, multiplication, and division
operations that each result in the number 8. Be sure to enclose your operations
in print() calls to see the results. You should create four lines that look like this:
print(5+3)
Your output should be four lines, with the number 8 appearing once on
each line.
2-10. Favorite Number: Use a variable to represent your favorite number. Then,
using that variable, create a message that reveals your favorite number. Print
that message.
2-11. Adding Comments: Choose two of the programs you’ve written, and
add at least one comment to each. If you don’t have anything specific to write
because your programs are too simple at this point, just add your name and the
current date at the top of each program file. Then write one sentence describing
what the program does.
2-12. Zen of Python: Enter import this into a Python terminal session and skim
through the additional principles.

"""
#2.1 / #2.2

message = 'Hello Python world!'
print(message)
message = 'Hello Python Crash Course world!'
print(message)

#2.3 / #2.11

name = input('please inter your name:') #abolfazl
message = print(f'Hello {name},''would you like to learn some Python today?')

#2.4

name = input('please inter your name:')
print(name.lower())
print(name.upper())
print(name.title())

#2.5 / #2.6

print('Peter Drucker once said, "The best way to predict your future is to create it."')
famous_person = 'Peter Drucker'
message = print(f'{famous_person} once said, "The best way to predict your future is to create it."')

#2.7

name = input('please inter your name:')
new_name = (f'{name}'.strip())
print(new_name)

#2.8

filename = 'python_notes.txt'
print(f'{filename}'.removesuffix('.txt'))

#2.9

print(5+3)
print(10-2)
print(4*2)
print(24/3)

#2.10 / #2.11

favorite_number = input('please inter your favorite_number:') #10
message = print(f'{favorite_number}''is a good number.')                                                                                                                                                                          
