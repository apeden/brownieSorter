class Brownie(object):
    """A participant in a camp who has to share a tent
    (or be in a group) with other brownies. The happiness
    of this participant depends on whether the other participants
    she is grouped with are friends, mutual friends, or (non-
    reciprocated) admirers.
    """
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.happiness = 0
    def addFriend(self, friend):
        """Add friend to friend list of this brownie."""
        self.friends.append(friend)
    def setHappiness(self, deltaHapp):
        """Increase happiness of this brownie by 'deltaHapp'."""
        self.happiness += deltaHapp
    def getHappiness(self):
        """Return happiness score of this brownie"""
        return self.happiness
    def getFriends(self):
        """Return names of brownies this brownie says she likes"""
        return self.friends
    def bonding(self, other):
        """Determine bond of this brownie with another.
        If brownie likes other brownie, bond is 1.
        If other brownie also likes this brownie, bond is 2.
        If only other brownie likes this brownie, bond is 1.
        """
        bond = 0
        if self.name in other.friends:
           bond += 1
        if other.name in self.friends:
           bond += 1
        return bond
    def getName(self):
        """Return name of brownie."""
        return self.name
    def __str__(self):
        """Print brownie name and friends."""
        return self.name + " has friends "+ str(self.friends)
