# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Nujood"
my_age = 22
my_bio = "hi"
myself = Person(my_name, my_bio, my_age)


def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    user_input = input ("Would you like to: \n 1) Create a new club. \n or \n 2) Browse and join clubs. \n or \n 3) View existing clubs. \n or \n 4) Display members of a club. \n or \n -1) Close application. \n")
    return user_input

def create_club():
    # your code goes here!
    for i in population:
        print(" [%s]  %s" %( population.index(i) +1 ,i.name) ) 
        
def create_club():
    # your code goes here!
    clubName= input ("What would you like to name your club? ")
    clubDesc= input ("What is your club about? ")
    newClub=Club(clubName,clubDesc)
    
    
        
    user_input= input ("Enter the numbers of people you would like to recruit (-1 to stop)")
    for i in population:
        print(" [%s]  %s" %( population.index(i) +1 ,i.name) ) 
    
    while True:
        user_input = input()
        if int(user_input) >0 and int(user_input) < 16:
            user_input = input("enter # of the next member you want to add ") #number
            x = population[int(user_input)-1]
            newClub.recruit_member(x)
        
        elif user_input == "-1":
            break
        else:
            print("please enter a valid #")
            

    newClub.recruit_member(myself.name)
    newClub.assign_president(myself.name)
    clubs.append(newClub)
    
    print("Here is your new club: \n %s \n %s \n members: " %(newClub.name, newClub.description ))
    newClub.print_member_list()
    
    total = 0
    count = 0
    for i in newClub.members:
        total+=i.age
        count +=1
    average= total/count
    print ("Avg age in this club = %d" % average)
    
        

def view_clubs():
    # your code goes here!
    for i in clubs:
        print("NAME: %s \n DESCRIPTION: %s \n MEMBERS: %s)" %(i.name, i.description , len(i.members)))
    

def view_club_members():
              
    # your code goes here!
    club_members= input ("enter the name of the club to view its members")
    
    for i in clubs:
        if  i.name.lower() == club_members.lower():
            i.print_member_list()

    

def join_clubs():
    # your code goes here!
    club_join= input ("enter the name of the club you'd like to join: ")
    
    for i in clubs:
        if club_join.capitalize() == i.name:
            i.recruit_member(myself)
            print ("%s has joined %s"%(my_name,i.name))
    

def application():
    introduction()
    # your code goes here!
    user_input=options()
              
    while user_input != str(-1):
        if user_input == str(1):
            create_club()         
        elif user_input == str(2):
            view_clubs()
            join_clubs()
        elif user_input == str(3):
            view_clubs()
        elif user_input == str(4):
            view_clubs()
            view_club_members()
        else:
            options()