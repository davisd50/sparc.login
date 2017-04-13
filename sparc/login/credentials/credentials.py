from zope import interface
from zope.component.factory import Factory
from .interfaces import ICredentials

@interface.implementer(ICredentials)
class Credentials(object):
    
    def __init__(self, identity=None, auth_tokens=None):
        self.identity = identity
        self.auth_tokens = auth_tokens
CredentialsFactory = Factory(Credentials)