from zope import component
from zope import interface
from sparc.login.identification import IIdentified
from sparc.login.identification.exceptions import InvalidIdentification
from .interfaces import IIdentityManager


@interface.implementer(IIdentityManager)
class IdentityManager(object):
    
    def __init__(self):
        self.counter = 0
        self.identities = set()
    
    def factory(self, token_id):
        """Factory to create a new IIdentified provider from given token_id
        
        Class extenders should override this method with their own implementation
        """
        return component.createObject(u'sparc.login.identity', token_id)
    
    def _get_token_from_identifier(self, identifier):
        return int(identifier.getId() if IIdentified.providedBy(identifier) else identifier)
    
    # IIdentificationManager
    def generate(self, hint=None):
        self.counter += 1
        while self.counter in self.identities:
            self.counter += 1
        self.identities.add(self.counter)
        return self.factory(self.counter)
    
    def create(self, id_token):
        token = int(id_token)
        if token in self.identities:
            raise  InvalidIdentification("id_token already exists")
        self.identities.add(token)
        return self.factory(token)
    
    def get(self, identifier):
        token = self._get_token_from_identifier(identifier)
        if token in self.identities:
            return self.factory(token)
        raise InvalidIdentification('identifier does not exist')
    
    def contains(self, identifier):
        try:
            self.get(identifier)
        except InvalidIdentification:
            return False
        return True
        
    def remove(self, identifier):
        token = self._get_token_from_identifier(identifier)
        self.get(token)
        self.identities.remove(token)
            
    
    def discard(self, identifier):
        token = self._get_token_from_identifier(identifier)
        self.identities.discard(token)
MemoryIdentityManager = IdentityManager()