from zope import interface
from zope.component.factory import Factory
from ..interfaces import IPrincipal

@interface.implementer(IPrincipal)
class PrincipalFromId(object):
    def __init__(self, principal_id):
        self._id = str(principal_id)
    
    def getId(self):
        return self._id
    
    def __str__(self):
        return self.getId()
    
    def __repr__(self):
        return "Principal with identifier {}".format(self.getId())
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        if not IPrincipal.providedBy(other):
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
PrincipalFromIdFactory = Factory(PrincipalFromId)