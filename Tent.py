class Tent(object):
    """A kind of grouping (which may actually be a tent)
    which will contain brownies. It will have a happiness,
    set according to the friendship statuses of the occupant
    brownies.
    """
    def __init__(self, num):
        self.num = num
        self.brownies = []
        self.brownie_profiles = ()# brownie names and happinesses
        self.happiness = 0
    def getNum(self):
        """Returning the identifying  number of this tent"""
        return self.num
    def getCapacity(self):
        """Return the capacity of this tent."""
        return self.capacity 
    def addBrownie(self, brownie):
        """Add a brownie to this tent.
        """
        self.brownies.append(brownie)
    def favIndex(self, otherBrownies):
        """Return the index of the brownie in a list
        of brownies that is most favoured by the
        occupants of this tent.
        """
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
        """Determine happiness of this tent
        on the basis of declared friendships
        amungst the brownies.
        For example, if a brownie in the
        tent likes another brownie in the tent,
        this increases tent happiness by 1. If
        the other brownie likes them back, happiness is
        increased by not 1, but 2 etc. 
        """
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
        "Return happiness of the tent."""
        return self.happiness
    def getBrownies(self):
        """Return all brownies in the tent."""
        return self.brownies
    def __str__(self):
        """Print tent occupants and their happinesses"""
        for brownie in self.brownies:
            self.brownie_profiles += (brownie.getName().ljust(12, " ")\
                                      +": "+str(brownie.happiness),)

        summary = "Tent " + str(self.num + 1)+": "
        summary += " Happiness: "+ str(self.getHappiness()) +"\n"
        for profile in self.brownie_profiles:
            summary += profile + "\n"
        return summary
