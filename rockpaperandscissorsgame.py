import random 

#input user
user1_input = input ('Choose rock, paper ou scissors: \n')

#input computer
a = ['rock','paper', 'scissors']
comp_input = a[random.randint (0,2)]

#index calculation
u1_index = a.index (user1_input)
comp_index = a.index (comp_input)

#compare answers using index numbers
def compare (x1,x2):
    if x1==x2:
        print ("It´s a drawn, the computer choosed " + comp_input + ' also.')
    elif (x1-x2) == 2 or (x1-x2) == -1:
        print ("You lost, the computer choosed " + comp_input + '.')
    elif x1-x2 == -2 or (x1-x2) == 1:
        print ("You won, the computer choosed " + comp_input + '.')
    else:
        print ("Wrong input.")

print (compare(u1_index,comp_index))

while True:
    usr_command = input("Do you want to play again? (Yes/No) ")
    if usr_command == "Yes":
        user1_input = input ('Choose rock, paper ou scissors: \n')
        a = ['rock','paper', 'scissors']
        comp_input = a[random.randint (0,2)]
        u1_index = a.index (user1_input)
        comp_index = a.index (comp_input)    
        print (compare(u1_index,comp_index))
    elif usr_command == "No":
        print("Thanks for playing. Goodbye.")
        break
    else: 
        print("Your input is not matching the options. Goodbye.")
        break
