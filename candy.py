#to smash candies
def to_smash(total_candies,number_of_friends):
    """ the candies need to smash for equal dividing"""
    return total_candies % number_of_friends
print("Candies to be smashed = ",(to_smash(10,3)))
#to distribute candies
def to_distribute_candies(total_candies,number_of_friends):
    """ the candies distributing to each child"""
    return total_candies//number_of_friends
print("Candies to be distributed to each =",(to_distribute_candies(10,3)))
#greeting friends
name = input()
def greeting_friends(name):
    """greeting friends"""
    return "Welcome, " + name + "!"
print(greeting_friends(name))
