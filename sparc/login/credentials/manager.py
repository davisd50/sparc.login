from zope import component
from zope import interface
from sparc.login.identification.manager import MemoryIdentityManager
from sparc.login.identification.exceptions import InvalidIdentification
from .interfaces import ICredentialIdentityManager

@interface.implementer(ICredentialIdentityManager)
class CredentialIdentityManager(MemoryIdentityManager):
    
    def factory(self, token_id):
        return component.createObject(u'sparc.login.credential_identity', token_id)
    
    def update(self, identifier, id_token):
        # This implementation is fairly poor...really just deletes old and adds
        # new without any relationship between the two.
        self.get(identifier) # validation check
        if self.contains(id_token):
            raise InvalidIdentification('id_token already in use')
        self.remove(identifier)
        return self.create(id_token)

MemoryCredentialIdentityManager = CredentialIdentityManager()