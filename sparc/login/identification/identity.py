from zope import interface
from zope.component.factory import Factory
from .interfaces import IIdentity

@interface.implementer(IIdentity)
class IdentityFromToken(object):
    
    #extenders can override this with their own IIdentity based interface
    interface = IIdentity
    
    def __init__(self, token):
        self._id = str(token)
    
    def getId(self):
        return self._id
    
    def __str__(self):
        return self.getId()
    
    def __repr__(self):
        return "{} provider with token {}".format(self.interface, self.getId())
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        if not self.interface.providedBy(other):
            return False
        return str(self) == str(other)
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        return str(self) < other
    
    def __le__(self, other):
        return str(self) <= other
    
    def __gt__(self, other):
        return str(self) > other
    
    def __ge__(self, other):
        return str(self) >= other
IdentityFromTokenFactory = Factory(IdentityFromToken)