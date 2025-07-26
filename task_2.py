from random import randrange, randint


def get_numbers_ticket(min, max, quantity):
    tickets=set() # return unique values
    
    if min<1: 
        print("Min value must be greater than 1. Try again.")
        return tickets
    
    
    if max>1000: 
        print("Max value must be lower than 1000. Try again.")
        return tickets
    
    if min>max:
        print("Min value must be lower than max. Try again.")
        return tickets
    
    if quantity>(max-min):
        print(f"There is not enough values to return {quantity} numbers. Try again.")
        return tickets
         
    
    while len(tickets)<quantity:
        number=randint(min, max)
        tickets.add(number)
    
    sorted_tickets=sorted(tickets)   
    return sorted_tickets

print(get_numbers_ticket(1, 10, 5)) 
        
        
      
    

        
