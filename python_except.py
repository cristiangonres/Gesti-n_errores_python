my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list")
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))



my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    for item in myList:
        assert type(item) == str, "Word list must be a list of strings"
    myList.sort()
    return myList
my_new_list = [6, 3, 8, "12", 42]
print(OrganizeList(my_new_list))
print(OrganizeList(my_new_list))


import random

participants = ['Jack','Jill','Larry','Tom']


# Revised Guess() function
def Guess(participants):
    my_participant_dict = {}
    
    try :
        for participant in participants:
            my_participant_dict[participant] = random.randint(1, 9)
        if my_participant_dict['Larry'] == 9:
            return True
        else:
            return False
    except: 
        return None


print(Guess(participants))

participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))