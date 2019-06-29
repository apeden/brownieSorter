import random

class Brownie(object):
    def __init__(self, name):
        self.name = name
        self.friends =[]
        self.popularity = 0
    def getPopularity(self):
        return self.popularity
    def addFriend(self, friend):
        self.friends += friend 
    def dimensionality(self):
        return len(self.friends)
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
        return self.name + str(self.friends)
    def __str__(self):
        return self.name + " has frients "+ str(self.friends)

class Tent(object):
    def __init__(self, num, capacity = 6):
        self.num = num
        self.capacity = capacity
        self.brownies = []
        self.brownie_names = ()
        self.happiness = 0
    def getNum(self):
        return self.num
    def getCapacity(self):
        return self.capacity 
    def addBrownie(self, brownie):
        if len(self.brownies) < 6:
            self.brownies.append(brownie)
        else:
            print("Tent full, can't add "+ str(brownie))
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
                if b1.getName() in b2.getFriends():
                    self.happiness += 1
                if b2.getName() in b1.getFriends():
                    self.happiness += 1
    def getHappiness(self):
        return self.happiness
    def __str__(self):
        for brownie in self.brownies:
            self.brownie_names += (brownie.getName(),)
        return str(self.num) + ": "+ str(self.brownie_names)\
               + " Happiness: "+ str(self.getHappiness()) 

class Camp(object):
    def __init__(self, camp_name,  num_tents =4):
        self.name = camp_name
        self.num_tents = num_tents
        self.tents = []
        self.allBrownies = []
        self.availBrownies = []
        self.happiness = 0    
    def getName(self):
        return self.name
    def getNumTents(self):
        return self.num_tents
    def setTents(self, tent):
        if len(self.tents) < self.num_tents:
            self.tents.append(tent)
    def resetTents(self):
        self.tents = []
    def getTents(self):
        return self.tents
    def addBrownie(self,brownie):
        self.allBrownies.append(brownie)
        self.availBrownies = self.allBrownies[:]
    def resetAvailBrownies(self):
        self.availBrownies = self.allBrownies[:]
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
    def seedTents(self):       
        self.availBrownies.sort(key = self.returnPopularity,
                                reverse = True)
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
            tentNum = (i%4)
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
            tentNum = (i%4)
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

#first_camp  = Camp ("first")
#print (first_camp.getTents())
#print (first_camp )
#brownie_list = []

def addNamesFrom(brownie_list, camp):
    for name in brownie_list:
        b = Brownie(name)
        list_copy = BROWNIES[:]
        list_copy = list_copy + [None,None,None]
        list_copy.remove(name)
        b.addFriend (random.sample(list_copy, 2))
        camp.addBrownie(b)
    
def test0(numClusters = 4, printSteps = False,
          printHistory = True):
    cS = BrownieClusterSet()
    for p in brownie_list:
        cS.add(BrownieCluster([p]))
    history = cS.mergeN(BrownieCluster.maxBond, numClusters, toPrint = printSteps)
    if printHistory:
        print ('')
        for i in range(len(history)):
            names1 = []
            for p in history[i][0].members():
                names1.append(p.getName())
            names2 = []
            for p in history[i][1].members():
                names2.append(p.getName())
            print ('Step', i, 'Merged', names1, 'with', names2)
            print ('')
    clusters = cS.getBrownieClusters()
    print ('Final set of clusters:')
    index = 0
    for c in clusters:
        print ('  C' + str(index) + ':', c)
        index += 1



#calculate popularities
##for b in first_camp.getBrownies():
##    b.popularityWith(first_camp.getBrownies())
##for b in first_camp.getBrownies():
##    print(b.getPopularity())

#first_camp.setPopularities()
#first_camp.seedTents()
#first_camp.completeTents()


first_camp  = Camp ("first")
addNamesFrom(BROWNIES, first_camp)

def happTrial(numTrials, camp, method):
    happList = []
    for x in range(numTrials):
        camp.resetTents()
        camp.resetAvailBrownies()
        camp.setPopularities()
        method()   
        camp.setHappiness()
        #for tent in camp.getTents():print(tent)
        happList.append(first_camp.getHappiness())
        sumHapp = 0
        for happ in happList:
            sumHapp += happ
    print(happList, "Mean ", str(sumHapp/len(happList)))

print("Random: ")
happTrial(10, first_camp, first_camp.randomTents)

print("Seed tents with most popular, then vote: ")
happTrial(10, first_camp, first_camp.seedTents)

print("Seed tents with random, then vote: ")
happTrial(10, first_camp, first_camp.randSeedTents)
