import random
import string

option = input('Welcome to the username creator...\nPlease choose one of the following options: \n1. Create a username based on your name \n2. Generate a random username \nEnter your choice: ')

def reverse_name(name):
    reversed_name = ''
    for i in range(len(name)):
        reversed_name += name[len(name)-i-1]
    return reversed_name

def interspace_name(reversed_name, surname):
    interspaced_name = ''
    
    if len(reversed_name) <= len(surname):
       for i in range(len(reversed_name)):
           interspaced_name += reversed_name[i] 
           interspaced_name += surname[i] 
       interspaced_name += surname[len(reversed_name):len(surname)]
       
    else:
       for i in range(len(surname)):
           interspaced_name += reversed_name[i] 
           interspaced_name += surname[i] 
       interspaced_name += reversed_name[len(surname):len(reversed_name)]
    return interspaced_name 

def format_name(interspaced_name):
    name_one = interspaced_name[0:round((len(interspaced_name))/2)]
    name_two = interspaced_name[round((len(interspaced_name))/2): len(interspaced_name)]
    name_one = name_one.capitalize()
    name_two = name_two.capitalize()
   
    formatted_name = name_one + " " + name_two
    return formatted_name

def random_name():
    characters = string.ascii_lowercase + string.digits
    random_first_name = ''
    random_last_name = ''
    for i in range(5):
       random_first_name += random.choice(characters)
    for i in range(5):
       random_last_name += random.choice(characters)
    random_first_name = random_first_name.capitalize()
    random_last_name = random_last_name.capitalize()
    randomised_name = random_first_name + " " + random_last_name
    return randomised_name
    
if option == '1':
   name = input('Enter Your First Name here: ')
   surname = input('Enter your surname here: ') 
   print ('Your Username is: ' + format_name(interspace_name(reverse_name(name), surname)))
   
elif option == '2':
   print ('Your Random Username is: ' + random_name())
   
else:
    print ('Not a valid option choice')