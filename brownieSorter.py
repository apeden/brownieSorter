import random
import pylab

class Brownie(object):
    def __init__(self, name):
        self.name = name
        self.friends =[]
        self.popularity = 0
        self.happiness = 0
    def getPopularity(self):
        return self.popularity
    def addFriend(self, friend):
        self.friends.append(friend)
    def setHappiness(self, deltaHapp):
        self.happiness += deltaHapp
    def getHappiness(self):
        return self.happiness
    def getFriends(self):
        return self.friends
    def bonding(self, other):
        bond = 0
        if self.name in other.friends:
           bond += 1
        if other.name in self.friends:
           bond += 1
        return bond
    def getName(self):
        return self.name
    def popularityWith(self, otherBrownies):
        self.popularity = 0
        for otherBrownie in otherBrownies:
            if self.name == otherBrownie.getName():
                continue
            self.popularity += self.bonding(otherBrownie)
    def toStr(self):
        return self.name + str(self.happiness)
    def __str__(self):
        return self.name + " has friends "+ str(self.friends)

class Tent(object):
    def __init__(self, num):
        self.num = num
        self.brownies = []
        self.brownie_profiles = ()
        self.happiness = 0
    def getNum(self):
        return self.num
    def getCapacity(self):
        return self.capacity 
    def addBrownie(self, brownie):
        self.brownies.append(brownie)
    def favIndex(self, otherBrownies):
        favIndex, topBond = 0,0
        for i in range(len(otherBrownies)):
            tentBond = 0
            for brownie in self.brownies:
                tentBond += brownie.bonding(otherBrownies[i])
            if tentBond > topBond:
                topBond = tentBond
                favIndex = i
        return favIndex
    def setHappiness(self):
        self.happiness = 0
        for b1 in self.brownies:
            for b2 in self.brownies:
                if b1 == b2:
                    continue
                if b1.getName() in b2.getFriends():
                    b1.setHappiness(1)
                    self.happiness += 1
                for friend in b1.getFriends():
                    if friend == b2.getName():
                        b1.setHappiness(1)
                        self.happiness += 1
    def getHappiness(self):
        return self.happiness
    def getBrownies(self):
        return self.brownies
    def __str__(self):
        for brownie in self.brownies:
            self.brownie_profiles += (brownie.getName()\
                                      +": "+str(brownie.happiness),)
        return str(self.num) + ": "+ str(self.brownie_profiles)\
               + " Happiness: "+ str(self.getHappiness()) 

class Camp(object):
    def __init__(self, camp_name,  num_tents =4):
        self.name = camp_name
        self.num_tents = num_tents
        self.tents = []
        self.allBrownies = []
        self.availBrownies = []
        self.happiness = 0
        self.minHapp = 0
    def getName(self):
        return self.name
    def getNumTents(self):
        return self.num_tents
    def setTents(self, tent):
        if len(self.tents) < self.num_tents:
            self.tents.append(tent)
    def getTents(self):
        return self.tents
    def addBrownie(self,brownie):
        self.allBrownies.append(brownie)
        self.availBrownies = self.allBrownies[:]
    def getAllBrownies(self):
        return self.allBrownies
    def getAvailBrownies(self):
        return self.availBrownies
    def getBrownie(self,brownie):
        for elem in self.availBrownies:
            if elem.getName() == brownie:
                return elem
            else: print ("No Brownie with that name")
    def setPopularities(self):
        for b1 in self.availBrownies:
            b1.popularityWith(self.availBrownies)
    def returnPopularity(self, brownie):
        return brownie.getPopularity()
    def seedByPop(self, reverse = True):
        if reverse == True:
            self.availBrownies.sort(key = self.returnPopularity,
                                    reverse = True)
        else:
            self.availBrownies.sort(key = self.returnPopularity,
                                    reverse = False)
        for i in range(self.num_tents):
            t = Tent(i)
            t.addBrownie(self.availBrownies.pop(0))
            self.setTents(t)
        self.voteFill()
    def randSeedTents(self):       
        for i in range(self.num_tents):
            t = Tent(i)
            numBrownies = len(self.availBrownies)
            randIndex = random.choice(range(numBrownies))
            randBrownie = self.availBrownies.pop(randIndex) 
            t.addBrownie(randBrownie)
            self.setTents(t)
        self.voteFill()
    def voteFill(self):
        i = 0
        while len(self.availBrownies)> 0:
            tentNum = (i%self.num_tents)
            tent =self.tents[tentNum]
            favIndex = tent.favIndex(self.availBrownies)
            tent.addBrownie(self.availBrownies.pop(favIndex))
            i += 1
    def randomTents(self):
        self.tents =[]
        for i in range(self.num_tents):
            t = Tent(i)
            self.setTents(t)
        i = 0
        while len(self.availBrownies)> 0:
            tentNum = (i%self.num_tents)
            tent = self.tents[tentNum]
            randomIndex = random.choice(range(len(self.availBrownies)))
            tent.addBrownie(self.availBrownies.pop(randomIndex))
            i += 1
    def setHappiness(self):
        self.happiness = 0
        for tent in self.tents:
            tent.setHappiness()
            self.happiness += tent.getHappiness()
    def getHappiness(self):
        return self.happiness
    def getRangeHapp(self):
        max = self.tents[0].getHappiness()
        min = self.tents[0].getHappiness()
        for tent in self.tents:
            if tent.getHappiness() > max:
                max == tent.getHappiness()
            elif tent.getHappiness() < min:
                min == tent.getHappiness()
        return max-min
    def setMinHapp(self):
        minHapp = self.tents[0].brownies[0].getHappiness()
        for tent in self.tents:
            for brownie in tent.getBrownies():
                if brownie.getHappiness() < minHapp:
                    minHapp = brownie.getHappiness()
        self.minHapp = minHapp
    def getMinHapp(self):
        return self.minHapp
    def getTents(self):
        return self.tents
    def __str__(self):
        return self.name + " has " + str(self.num_tents) + " tents."
        
BROWNIES = ["Anna",
"Babs",
"Carol",
"Danni",
"Ellie",
"Freddie",
"Gerri",
"Hanna",
"Iona",
"Jessi",
"Kelly",
"Linda",
"Molly",
"Nellie",
"Olivia",
"Peppa",
"Queenie",
"Rosie",
"Sasha",
"Trinni",
"Uma",
"Vanessa",
"Winnie",
"Xa"]
class Organiser(object):
    def __init__(self, file = None, numTents = 4, capacity = 6):
        if not file == None:
            self.file = file
        self.brownies = []
        self.friendlist = []
        self.brownieObjs = []
        self.camps = []
        self.numTents = numTents
        self.capacity = capacity
    def readFile(self):
        try:
            f = open(self.file)
        except:
            print("Error opening brownie file")
        inFile = open(self.file)
        for l in inFile:
            try:              
                brownieAndFriends = l.rstrip('\n').split(',')
                self.friendlist.append(brownieAndFriends)
            except:
                print("Error reading line")
    def addNamesFrom(self, brownie_list):
        self.brownieObjs = []
        for name in brownie_list:
            list_copy = brownie_list[:]
            list_copy = list_copy + [None,None,None]
            list_copy.remove(name)
            b = Brownie(name)
            b.addFriend (random.sample(list_copy, 1))
            b.addFriend (random.sample(list_copy, 1))
            self.brownieObjs.append(b)
    def are_brownies(self, friend_list):
        for friend in friend_list:
            if not friend in self.brownies:
                print (friend + " is not a named brownie")
                return False
        return True
    def addBrownies(self):
        self.brownieObjs = []
        self.brownies = []
        for brownieAndFriends in self.friendlist:
            self.brownies.append(brownieAndFriends[0])
        for brownieAndFriends in self.friendlist:
            b = Brownie(brownieAndFriends[0])
            if self.are_brownies(brownieAndFriends[1:]):
                for friend in brownieAndFriends[1:]:
                    b.addFriend(friend)
            else:
                print ("A friend of "+ brownieAndFriends[0] \
                       + " is not listed as brownie: " \
                       + str(brownieAndFriends[1:]))
                raise
            self.brownieObjs.append(b)
    def happTrial(self, numTrials):
        self.camps = []    
        for x in range(numTrials):
            self.addBrownies()
            camp  = Camp (str(x), self.numTents)
            for brownie in self.brownieObjs:
                camp.addBrownie(brownie)
            #seed tents with random brownies
            #tents filled by voting of tent occupants
            camp.randSeedTents()
            #calc brownie, tent and camp happiness
            camp.setHappiness()
            #calc min happiness of brownie in camp
            camp.setMinHapp()
            self.camps.append(camp)
        
        def filt(camp_list, method, standard):
            filt_list = []
            for camp in camp_list:
                if method(camp) == standard:
                    filt_list.append(camp)
            return filt_list        
        #filter alternative camps to maximise camp happiness
        print("Number of camps before filtering: ", len(self.camps))
        maxHappCamp = max(self.camps,
                              key =lambda x:x.getHappiness())
        maxHapp =  maxHappCamp.getHappiness()
        filtered_camps = filt(self.camps, Camp.getHappiness, maxHapp)
        print("filtered for camp happiness: ", len(filtered_camps))
        #filter to minimize individual brownie unhappiness
        maxMinBrownHappCamp = max(self.camps,
                              key = lambda x:x.getMinHapp())      
        maxMinBrownHapp = maxMinBrownHappCamp.getMinHapp()
        filtered_camps = filt(filtered_camps,
                              camp.getMinHapp,
                              maxMinBrownHapp)
        #filter to minimize variation in tent happiness
        minRangeHappCamp = min(self.camps,
                              key = lambda x:x.getRangeHapp())
        minRangeHapp = minRangeHappCamp.getRangeHapp()
        filtered_camps = filt(filtered_camps,
                              camp.getRangeHapp,
                              minRangeHapp)
        print ("Maximum minimum brownie happiness: ",
               str(maxMinBrownHapp))
        print("Number of optimal camps: ",
              len(filtered_camps))
        print("NumTrials = ", str(numTrial),
              " Max: ", str(maxHapp))
        n = 0
        while n < 5:
            try:
                for tent in filtered_camps[n].getTents():
                    print(tent)
                n += 1
            except:
                break

    def __str__(self):
        return str(self.friendlist)

print("Seed tents with random brownies, then vote: ")
o = Organiser("real_brownies.txt", numTents = 3)
o.readFile()
print(o)
for numTrial in 1000,:
    o.happTrial(numTrial)

