def ask_user_for_number():
    n = ''
    while True:
        n = input('Choose an Integer: ')
        if n.isdigit() == True:
           n = int(n)
           return n
        else:
           print('Not a valid input')
        
def sum_numbers(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum

def sum_specific_numbers(n):
    sum = 0
    for i in range(n+1):
       if i % 3 == 0 or i % 5 == 0:
           sum = sum + i
    return sum

def product_numbers(n):
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
    return sum


def which_calculation(n):
      while True:    
          m = input('Would you like to work out the product or sum of numbers from 1 to ' +  str(n) +  ' ? ')
          if m == "sum":       
             print("\nThe sum of numbers from 1 to", n, "is" ,sum_numbers(n), "\n")
             break 
          elif m == "product":
             print("The product of numbers from 1 to", n, "is", product_numbers(n), "\n")    
             break 
          else:
              print("Not a valid input")   

n = ask_user_for_number()                
              
m = which_calculation(n)        


