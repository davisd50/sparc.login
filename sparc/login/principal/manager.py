from zope import component
from zope import interface
from sparc.login.identification import IIdentified
from sparc.login.identification.exceptions import InvalidIdentification
from .interfaces import IPrincipalManager

@interface.implementer(IPrincipalManager)
class PrincipalManager(object):
    
    def __init__(self):
        self.counter = 0
        self.principals = set()
    
    def _get_token_from_identifier(self, identifier):
        return int(identifier.getId() if IIdentified.providedBy(identifier) else identifier)
    
    def generate(self, hint=None):
        self.counter += 1
        while self.counter in self.principals:
            self.counter += 1
        self.principals.add(self.counter)
        return component.createObject(u'sparc.login.principal', self.counter)
    
    def create(self, id_token):
        token = int(id_token)
        if token in self.principals:
            raise  InvalidIdentification("id_token already exists")
        self.principals.add(token)
        return component.createObject(u'sparc.login.principal', token)
    
    def get(self, identifier):
        token = self._get_token_from_identifier(identifier)
        if token in self.principals:
            return component.createObject(u'sparc.login.principal', token)
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
        self.principals.remove(token)
            
    
    def discard(self, identifier):
        token = self._get_token_from_identifier(identifier)
        self.principals.discard(token)
MemoryPrincipalManager = PrincipalManager()