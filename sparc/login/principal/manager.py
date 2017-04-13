from zope import component
from zope import interface
from sparc.login.identification.manager import MemoryIdentityManager
from .interfaces import IPrincipalManager

@interface.implementer(IPrincipalManager)
class MemoryPrincipalManager(MemoryIdentityManager):
    
    def factory(self, token_id):
        return component.createObject(u'sparc.login.principal', token_id)
