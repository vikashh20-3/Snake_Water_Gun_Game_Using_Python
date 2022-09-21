import random

comp_input=random.randint(1,3)
if comp_input==1:
    comp_value='stone'
elif comp_input==2:
    comp_value='paper'
elif comp_input==3:
    comp_value='scissor'
    
    

user_value=input("Choose your value from stone(stone),paper(paper) and scissor(scissor)?-")
user_value=str(user_value)
comp_value=str(comp_value)
print("Computer choice is "+ comp_value)
print("Your choice is "+ user_value)
if comp_value==user_value:
        print("Match Tie!!")
elif  (comp_value=='stone'and user_value=='scissor')or(comp_value=='paper'and user_value=='stone')or(comp_value=='scissor'and user_value=='paper'):
    print("computer win! ")
else:
    print("You win!")        
    


