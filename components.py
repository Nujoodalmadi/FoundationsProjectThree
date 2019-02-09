# CLASSES AND METHODS
class Person():

    def __init__(self, name, bio, age):
        self.name=name
        self.bio=bio
        self.age=age
        self.president=False
        # your code goes here!


class Club():
    def __init__(self, name, description):
        self.name=name
        self.description=description
        self.president=""
        self.members=[]
        # your code goes here!


    def assign_president(self, person):
        # your code goes here!
        self.president=person


    def recruit_member(self, person):
        # your code goes here!
        self.members.append(person)



    def print_member_list(self):
        # your code goes here!
        for i in self.members:
            
            if i.president == False:
                print ("%s (%d years old) - %s" % (member.name, member.age, member.bio))
            else:
                print ("%s (%d years old, President) - %s" % (member.name, member.age, member.bio))



