from zope import interface
from zope.component.factory import Factory
from sparc.login.identification.identity import IdentityFromToken
from .interfaces import ICredentialIdentity

@interface.implementer(ICredentialIdentity)
class CredentialIdentityFromToken(IdentityFromToken):
    interface = ICredentialIdentity

CredentialIdentityFromTokenFactory = Factory(CredentialIdentityFromToken)