from grobot import*
from random import randint, randrange
from math import sqrt

def is_inside(x,y):
    found = False
    i = 0
    while i < len (y):
        if x == y [i]:
            found = True
            break
        i += 1         
    return found

class Sonic():
    def __init__(self, name, x, y, colour, goal = (0,0)):
        self._sonic = NewRobot(name,x,y,colour)
        self.orientation = "N" #The Robot is facing the North Direction
        self.x = x
        self.y = y
        self.memory = [(x,y)]
        self.goal = goal

    def look(self):
        return self._sonic.look()

    def turn_right(self):
        if self.orientation == "N":
            self.orientation = "E"
            
        elif self.orientation == "E":
            self.orientation = "S"
            
        elif self.orientation == "S":
            self.orienation = "W"
            
        elif self.orientation == "W":
            self.orientation = "N"               


    def turn_left(self):
        if self.orientation == "N":
            self.orientation = "W"
        elif self.orientation == "W":
            self.orientation = "S"
        elif self.orientation == "S":
            self.orientation = "E"
        elif self.orientation == "E":
            self.orientation = "N"

            print("turning left!")
            
    def forward(self):
           self._sonic.forward()
           self.change_position()
           self.remember(self.get_position())
        
    def right(self):
           self._sonic.right()
           self.turn_right()
           print("RIGHT!")
           
    def left(self):
           self._sonic.left()
           self.turn_left()
           
    def get_position(self):
        return (self.x, self.y)

    def remember(self, data):
        if not is_inside(data,self.memory):
            self.memory.append(data)
        
    def change_position(self):
        if self.orientation == "N":
            self.y = self.y + 1
        elif self.orientation == "E":
            self.x = self.x + 1
        elif self.orientation == "S":
            self.y = self.y - 1
        elif self.orientation == "W":
            self.x = self.x - 1


    def intergrate(self):
        stuff = self.look()
        choice = randint(0,4)
        if choice == 0 and stuff[choice] == None:
            self.left()
            self.forward()
        elif choice == 2 and stuff[choice] == None:
            self.forward()
        elif choice == 4 and stuff[choice] == None:
            self.right()
            self.forward()

    def intergrate_2(self):
        number_option, options = how_many(None,self.look())
        if number_option > 0:
            check = []
            detailed_options = detail_options(self, options)
            for e in detailed_options: #position, coordinates
                if is_inside(e,self.memory):
                    check.append(False)
                else:
                    check.append(True)
            option = pick_2(zip(options, check))
            choose (self,option)
        else:
            self.right()
            self.right()

    def intergrate_3(self):
    #Purpose is to move robot closer to the goal
        n_options,options = how_many(None,self.look())
        if n_options > 0:
            check = []
            d_option = detail_options(self,options)
            distances = get_distances(self.goal, d_option)
            #print(d_option)

            print(self.orientation)

            for e in d_option:
                if is_inside(e,self.memory):
                    check.append(False)
                else:
                    check.append(True)

            #print(zip_3(distances,check,options))
            option = pick_3(zip_3(distances,check,options))
            #print(option)
            choose(self,option)
        else:
            self.right()
            self.right()

def how_many(x,y):
    number = 0
    pos = 0
    indexes = []
    for elem in y:
        if x == elem:
            number = number + 1
            indexes.append(pos)
        pos = pos + 1
    return (number,indexes)

def detail_options(r,option):
#Depending on where you are facing, get coordinates
    new_options = []
    if r.orientation == "N":
        for e in option:
            new_options.append(new_pos_north(e, r.get_position()))
    elif r.orientation == "E":
        for e in option:
            new_options.append(new_pos_east(e, r.get_position()))
    elif r.orientation == "S":
        for e in option:
            new_options.append(new_pos_south(e, r.get_position()))
    elif r.orientation == "W":
        for e in option:
            new_options.append(new_pos_west(e, r.get_position()))
    return new_options



def new_pos_north(option,pos):
    new_pos = (0,0)
    x,y = pos
    if option == 0:
        new_pos = (x -1, y)
    elif option == 1:
         new_pos = (x - 1, y + 1)
    elif option == 2:
         new_pos = (x, y + 1)
    elif option == 3:
         new_pos = (x + 1, y + 1)
    elif option == 4:
         new_pos = (x + 1, y)
    return new_pos
                                   
def new_pos_east(option,pos):
    new_pos = (0,0)
    x,y = pos
    if option == 0:
        new_pos = (x, y + 1)
    elif option == 1:
        new_pos = (x + 1, y + 1)
    elif option == 2:
        new_pos = (x + 1, y)
    elif option == 3:
        new_pos = (x + 1, y - 1)
    elif option == 4:
        new_pos = (x, y - 1)
    return new_pos
            
def  new_pos_south(option,pos):
    new_pos = (0,0)
    x,y = pos
    if option == 0:
        new_pos = (x + 1, y)
    elif option == 1:
         new_pos = (x + 1, y - 1)
    elif option == 2:
         new_pos = (x, y - 1)
    elif option == 3:
         new_pos = (x - 1, y - 1)
    elif option == 4:
         new_pos = (x - 1, y)
    return new_pos

def new_pos_west(option,pos):
    new_pos = (0,0)
    x,y = pos
    if option == 0:
        new_pos = (x , y - 1)
    elif option == 1:
         new_pos = (x - 1, y - 1)
    elif option == 2:
         new_pos = (x - 1, y)
    elif option == 3:
         new_pos = (x - 1, y + 1)
    elif option == 4:
         new_pos = (x, y + 1)
    return new_pos

def zip(x,y):
    index = 0
    data = []
    while index < len(y):
        data.append((x[index], y[index]))
        index = index + 1
    return data

def pick_2(options):
    index = 0
    new_options = []
    while index < len(options):
         tuple_value, tuple_value2 = options[index]
         if tuple_value % 2 == 0 and tuple_value2 == True:
             new_options.append(options[index])
         index = index + 1
    value = 0
    if len(new_options) > 0:
        number = randrange(0, len(new_options),1)
        value,_ = new_options[number]
    else:
        number = randrange(0, len(options), 1)
        value,_ = options[number]
    return value

def choose(robot,choice):
    if choice == 0:
       robot.left()
       robot.forward()
       
    elif choice == 2:
       robot.forward()
       
    elif choice == 4:
       robot.right()
       robot.forward()
       
    elif choice == 5:
        robot.right()
        robot.right()

        
def get_distances(r_pos,points):
    distances = []
    r_x, r_y = r_pos
    
    for x, y in points:
        distance = sqrt((abs(x-r_x)**2) + (abs(y - r_y)**2))
        distances.append(distance)
    return distances

def zip_3(x,y,z):
#Get Closest distance and option
#Use Previous logic and branch
#pick an option that is closest to end goal
    i = 0
    data = []
    while i < len(y):
        if z[i]%2 == 0:
            data.append((x[i], y[i], z[i]))
        i+=1
    return data
    

def pick_3(options):
    option = 5
    if len(options) > 0:
        _,unseen, option = min(options)
        if unseen == False or option % 2 != 0:
            n = randrange(0,len(options), 1)
            _,_,option = options[n]
    return option

def main():
    s = Sonic("Sanic", 2, 2, "blue", (29,29))
    i = 0
    while s.get_position() != s.goal:
        s.intergrate_3()
        i += 1

    print("Sonic finished in", i, "moves")

main()
