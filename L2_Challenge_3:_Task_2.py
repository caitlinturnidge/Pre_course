people = {"Jane Doe": {"Age": 42, "Employed": "yes"}, "Tom Smith": {"Age": 18, "Employed": "yes"},
          "Mariam Coulter": {"Age": 66, "Employed": "no"}, "Gregory Tims": {"Age": 8, "Employed": "no"}}


def print_dictionary(dictionary):
    print("List of people:")
    for i in dictionary:
        print('Name:', i)
        for j in dictionary[i]:
            print(j, ':', dictionary[i][j])


def add_to_dictionary(dictionary):
    name = input("What is their full name? ")
    age = input("What is their age? ")
    employed = input("Are they employed? ")
    dictionary[str(name)] = {}
    dictionary[str(name)]['Age'] = age
    dictionary[str(name)]['employed'] = employed


def delete_from_dictionary(dictionary):
    user_to_delete = input("Which user should be deleted? ")
    if user_to_delete in dictionary:
        del dictionary[user_to_delete]
    else:
        print("The name you entered is not in the list, next time make sure you enter their full name correctly.")


def people_manager():
    while True:
        print_dictionary(people)
        prompt = input("Would you like to Add or Remove a person? ")
        if prompt == "Add":
            add_to_dictionary(people)
        elif prompt == "Remove":
            delete_from_dictionary(people)
        else:
            print("Not a valid response")


people_manager()
