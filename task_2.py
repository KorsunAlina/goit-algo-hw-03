from random import randrange, randint


def get_numbers_ticket(min, max, quantity):
    if min<1: 
        print("Min value must be greater than 1. Try again.")
        return
    
    
    if max>1000: 
        print("Max value must be lower than 1000. Try again: ")
        return
     
    if quantity<min:
        quantity=print(f"Quantity must be greater than {min}. Try again")
        return
        
    if quantity>max: 
       print(f"Quantity must be lower than {max}. Try again")
       return
       
    
    tickets=[]  
    for i in range (quantity):
        number=randint(min, max)
        tickets.append(number)
    
    sorted_tickets=sorted(tickets)   
    return sorted_tickets

print(get_numbers_ticket(4, 128, 10))
        
        
      
    

        
