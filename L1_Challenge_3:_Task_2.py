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
    
n = ask_user_for_number()   
print("The sum of numbers from 1 to", n, "is" ,sum_numbers(n), "\n")
p = ask_user_for_number()   
print("The sum of numbers from 1 to", p, "which are a multiple of three or five is", sum_specific_numbers(p), "\n")
m = ask_user_for_number() 
print("The product of numbers from 1 to", m, "is", product_numbers(m), "\n")