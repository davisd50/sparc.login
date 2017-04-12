from zope import interface
from zope.component.factory import Factory
from sparc.login.identification.identity import IdentityFromToken
from .interfaces import IPrincipal

@interface.implementer(IPrincipal)
class PrincipalFromToken(IdentityFromToken):
    interface = IPrincipal

PrincipalFromTokenFactory = Factory(PrincipalFromToken)