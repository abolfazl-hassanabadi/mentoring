"""

8-1. Message: Write a function called display_message() that prints one sen-
tence telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.
8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print a
sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the values
that are returned.
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
8-9. Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the func-
tion send_messages() with a copy of the list of messages. After calling the func-
tion, print both of your lists to show that the original list has retained its messages.
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sand-
wich that’s being ordered. Call the function three times, using a different num-
ber of arguments each time.
8-13. User Profile: Start with a copy of user_profile.py from page 148. Build a
profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
8-14. Cars: Write a function that stores information about a car in a diction-
ary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the func-
tion with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.
8-15. Printing Models: Put the functions for the example printing_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of printing_models.py, and modify the file to use the imported functions.
8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
8-17. Styling Functions: Choose any three programs you wrote for this chapter,
and make sure they follow the styling guidelines described in this section.

"""
#8.1

def display_message(username):
    print(f'hello {username}, in this chapter,you learned about functions.')

display_message('abolfazl')

#8.2

def favorite_book(book_title):
    print(f'one of my favorite_books is {book_title}.')

favorite_book('the power of your subconscious mind')

#8.3 / #8.4

def make_shirt(size,message):
    print(f'shirt size: {size}, message:{message}')

make_shirt('m','python rocks')
make_shirt(size='l',message='i love coding')

#8.5

def describe_city(city,country='iceland'):
    print(f'{city} is in {country}.')

describe_city('reykjavik')
describe_city('akureyri')
describe_city('paris','france')

#8.6

def city_country(city,country):
    return f'{city},{country}'

print(city_country('santiago','chile'))
print(city_country('tokyo','japan'))
print(city_country('paris','france'))

#8.7

def make_album(artist,title,num_songs=None):
    album = {'artist': artist,'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

album1 = make_album('the beatles','abbey road')
album2 = make_album('pink floyd','the dark side of the moon')
album3 = make_album('michael jackson','thriller',9)

print(album1)
print(album2)
print(album3)

#8.8

def make_album(artist,title,num_songs=None):
    album = {'artist': artist,'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

print("enter album details (or 'q' to quit):")
while True:
    artist = input('\nArtist:')
    if artist == 'q':
        break
    title = input('album title:')
    if title == 'q':
        break
    num_songs = input('number of songs (optional, press Enter to skip):')
    if num_songs == 'q':
        break
    if num_songs:
        album = make_album(artist,title,int(num_songs))
    else:
        album = make_album(artist, title)
    
    print(album)

#8.9

def show_messages(messages):
    for message in messages:
        print(message)
text_messages = [
    'Hey,how are you?',
    'Thanks for your help!'
]

show_messages(text_messages)

#8.10 / #8.11

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages,sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)

messages = [
    'Hey,how are you?',
    'Thanks for your help!'
]

sent_messages = []
print("Original messages:")
show_messages(messages)
print("\n")

send_messages(messages,sent_messages)

#8.12

def make_sandwich(*items):
    print('\nMaking a sandwich with the following items:')
    for item in items:
        print(f'-{item}')

make_sandwich('ham','cheese','lettuce')
make_sandwich('turkey','avocado')
make_sandwich('peanut butter','jelly')

#8.13

def build_profile(first, last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile(
    'abolfazl', 
    'hassanabadi',
    age=19,
    occupation='engineer'
)

print(my_profile)

#8.14

def make_car(manufacturer, model,**car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car(
    'subaru',
    'outback',
    color='blue',
    tow_package=True
)

print(car)

