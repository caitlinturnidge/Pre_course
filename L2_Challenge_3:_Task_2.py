people = {"Jane Doe": {"Age": 42, "Employed": "yes"}, "Tom Smith": {"Age": 18, "Employed": "yes"}, "Mariam Coulter": {"Age": 66, "Employed": "no"}, "Gregory Tims": {"Age": 8, "Employed": "no"}}

def print_dictionary(dictionary):
    print("List of people:")
    for i in people:
       print('Name:', i)
       for j in people[i]:
          print(j, ':' , people[i][j])
          
def add_to_dictionary():
    name = input("What is their full name? ")
    age = input("What is their age? ")
    employed = input("Are they employed? ")
    people[str(name)] = {}
    people[str(name)]['Age'] = age
    people[str(name)]['employed'] = employed
    
def delete_from_dictionary():
    delete = input("Which user should be deleted? ")
    if delete in people:
       del people[delete]
       print_dictionary(people)
    else:
       print("The name you entered is not in the list, next time make sure you enter their full name correctly.")

def prompt():
   prompt = ''
   while True:
      prompt = input("Would you like to Add or Remove a person? ")
      if prompt == "Add":
         add_to_dictionary()
         print_dictionary(people)
      elif prompt == "Remove":
         delete_from_dictionary()
      else:
         print("Not a valid response")

print_dictionary(people)   
prompt()