class Camp(object):
    """A camp of brownies that will comprise tents (
    groupings of brownies) each with 'happiness' scores
    that will depend on who they are sharing a tent with.
    """
    def __init__(self, camp_name,  num_tents =4):
        self.name = camp_name
        self.num_tents = num_tents
        self.tents = []
        self.allBrownies = []
        self.availBrownies = []
        self.happiness = 0
        self.minHapp = 0
    def getName(self):
        """Return name of camp."""
        return self.name
    def setTents(self, tent):
        """Add a tent to the camp if the total will
        be less then or equal to that allowed.
        """
        if len(self.tents) < self.num_tents:
            self.tents.append(tent)
    def getTents(self):
        """Return the tents in this camp."""
        return self.tents
    def addBrownie(self,brownie):
        """Add this brownie to the camp"""
        self.allBrownies.append(brownie)
        self.availBrownies = self.allBrownies[:]
    def randSeedTents(self):       
        """Place one brownie at random in each of the
        empty tents. Then call voteFill() to fully
        populate the tents with brownies.
        """
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
        """Sequentially (tent by tent) get brownie(s) in each
        tent to vote on which of the remaining brownies they
        would (collectively) most like to join them. The chosen
        brownie is added to the tent.
        """
        while len(self.availBrownies)> 0:
            tentNum = (i%self.num_tents)
            tent =self.tents[tentNum]
            favIndex = tent.favIndex(self.availBrownies)
            tent.addBrownie(self.availBrownies.pop(favIndex))
            i += 1
    def setHappiness(self):
        """Determine happiness of the camp on basis of collective
        happinesses of the tents (in turn dependent on the
        happinesses of the brownies therein).
        """
        self.happiness = 0
        for tent in self.tents:
            tent.setHappiness()
            self.happiness += tent.getHappiness()
    def getHappiness(self):
        """Return camp happiness."""
        return self.happiness
    def getRangeHapp(self):
        """Determine difference between most happy
        and least happy tent in the camp.
        """
        max = self.tents[0].getHappiness()
        min = self.tents[0].getHappiness()
        for tent in self.tents:
            if tent.getHappiness() > max:
                max = tent.getHappiness()
            elif tent.getHappiness() < min:
                min = tent.getHappiness()
        return max-min
    def setMinHapp(self):
        "Determine happiness of least happy brownie in the camp."""
        minHapp = self.tents[0].brownies[0].getHappiness()
        for tent in self.tents:
            for brownie in tent.getBrownies():
                if brownie.getHappiness() < minHapp:
                    minHapp = brownie.getHappiness()
        self.minHapp = minHapp
    def getMinHapp(self):
        "Return happiness of least happy brownie in the camp."""
        return self.minHapp
    def getTents(self):
        """Return tents"""
        return self.tents
    def __str__(self):
        """Print camp name and number of groups."""
        return "Hypothetical camp " \
               + self.name \
               + " has " + str(self.num_tents) + " tents."
