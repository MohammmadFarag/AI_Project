import random as rdm

#this function check if all ants are fulfilled and don't need to acquire any more food but the global array that contains all discovered food mustn't be empty
def isneedempty(ants):
    if (global_array == []):
        return False
    for i in range(len(ants)):
        if (ants[i].ant_need == [] and ants[i].ant_array ):
            continue
        else:
            return False
    return True

#this array contains all discovered food in the map in that formula [[food1 weight , food1 value],[food2 weight , food2 value],...]
global_array = []
#this array contains all the food that will be in the map
food_array = [[25, 99], [75, 50], [16, 9], [43, 6], [80, 1], [99, 17], [25, 52], [19, 67], [74, 2], [1, 1]]
#this is the width of the map and represents the max weight for a food that can be positioned in the map
global_x = 100
#this is the height of the map and represents the max value for a food that can be positioned in the map
global_y = 100

#this class represent an agent that will try to acquire food
class ant:
    def __init__(self, antid, maxweight):#constructor that put the ant a random position in the map and for initialization
        self.antid = antid
        self.x_pos = rdm.randrange(0, global_x, 1)#random position less than the max x
        self.y_pos = rdm.randrange(0, global_y, 1)#random position less than the max y
        self.ant_array = []#an array that will contain all acquired food
        self.ant_need = []#an array that will contain all the food that this ant is searching for and hadn't acquired yet
        self.maxweight = maxweight#maximum weight of food that this ant can carry

    #this function moves an ant from one position to another position
    def move(self):
        #this if condition gets the best value/weight food object from the global array and puts it in the need array for the current ant
        if (len(global_array) > 0):
            greaterboundedvalue = [1, 0]
            for i in range(len(global_array)):
                if (global_array[i][1] / global_array[i][0] > greaterboundedvalue[1] / greaterboundedvalue[0]):
                    greaterboundedvalue = global_array[i]
            if(greaterboundedvalue not in self.ant_need and greaterboundedvalue not in self.ant_array):
                self.ant_array.clear()
                self.ant_need = greaterboundedvalue

        #in this condition the ant will move randomely when it don't have any food to look for
        if (self.ant_need == [] and self.ant_array == []):
            randomdirection = rdm.randrange(1, 5, 1)#create a random number for the random direction that this ant will go to
            if (randomdirection == 1):# number 1 is for up
                if (self.y_pos == global_y - 1):#if we are at the top of the map then we can't go up any more so we will reverse the direction of moving
                    self.y_pos -= 1
                else:
                    self.y_pos += 1
            elif (randomdirection == 2):# number 2 is for down
                if (self.y_pos == 0):#if we are at the bottom of the map then we can't go down any more so we will reverse the direction of moving
                    self.y_pos += 1
                else:
                    self.y_pos -= 1
            elif (randomdirection == 3):#number 3 is for right
                if (self.x_pos == global_x - 1):
                    self.x_pos -= 1
                else:
                    self.x_pos += 1
            else:#number 4 is for the left direction
                if (self.x_pos == 0):
                    self.x_pos += 1
                else:
                    self.x_pos -= 1
        #this condition will move the ant to the position of the required food
        elif (len(self.ant_need) > 0):
            targetX = self.ant_need[0]#required food x
            targetY = self.ant_need[1]#required food y
            if(self.x_pos < targetX and self.y_pos < targetY):#move one step to 45 degree
                self.x_pos += 1
                self.y_pos += 1
            elif(self.x_pos > targetX and self.y_pos > targetY):#move one step to 225 degree
                self.x_pos -= 1
                self.y_pos -= 1
            elif (self.x_pos > targetX and self.y_pos < targetY):#move one step to 135 degree
                self.x_pos -= 1
                self.y_pos += 1
            elif (self.x_pos < targetX and self.y_pos > targetY):#move one step to 315 degree
                self.x_pos += 1
                self.y_pos -= 1
            elif (self.x_pos < targetX):#move one step to 0 degree
                self.x_pos += 1
            elif (self.x_pos > targetX):#move one step to 180 degree
                self.x_pos -= 1
            elif (self.y_pos < targetY):#move one step to 90 degree
                self.y_pos += 1
            elif (self.y_pos > targetY):#move one step to 270 degree
                self.y_pos -= 1
            else:#this condition is activated when the ant is already at the position of the food that it wants to acquire
                self.ant_array.insert(0 , self.ant_need.copy())
                self.ant_need.clear()
                self.ant_array.insert(1,self.maxweight/self.ant_array[0][0])
        else:#this condition will be activated when the ant don't need any more food and the ant will stop moving
            print(str(self.antid) + " Stopped")

        #this condition will be activated when the ant is currently on a food position and  this food isn't in the global array so it add the food to the global array so all ants can see it's position
        if ([self.x_pos, self.y_pos] in food_array and [self.x_pos, self.y_pos] not in global_array):
            global_array.append([self.x_pos, self.y_pos])
            if([] in global_array):#this is an error fixer as the global array will have an empty array in it so it won't be empty ever so we search for that array and remove it so the global array won't be like that [[]]
                global_array.remove([])

#main function
def main():
    ants = []#create an array of ants
    antsnumber = 1000#number of ants that will be created
    for i in range(antsnumber):#creating ants objects and add them to the ants array
        ants.append(ant(i, 100))

    roundscounter = 0#variable to calculate the number of steps for all ants so if it's 100 then the most exhausted ant moved 100 step and all other ants moved <= 100 step

    #this loop will loop until all ants don't need any more food but they must have at least one food object acquired
    while (not isneedempty(ants)):
        for i in range(len(ants)):
            ants[i].move()
            # printing the current ant data
            print("ant id " + str(ants[i].antid) + ", x = " + str(ants[i].x_pos) + ", y = " + str(ants[i].y_pos) + ", need " + str(ants[i].ant_need) + ", have " + str(ants[i].ant_array))
        roundscounter += 1


    print("number of steps is " + str(roundscounter))
    print("global array is ", global_array)
    print("final result is ", ants[0].ant_array , "total value is " , (ants[0].ant_array[0][1] * ants[0].ant_array[1]))

main()