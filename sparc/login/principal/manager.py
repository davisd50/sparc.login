from zope import component
from zope import interface
from sparc.login.identification.manager import IdentityManager
from .interfaces import IPrincipalManager

@interface.implementer(IPrincipalManager)
class PrincipalManager(IdentityManager):
    
    def factory(self, token_id):
        return component.createObject(u'sparc.login.principal', token_id)

MemoryPrincipalManager = PrincipalManager()