from zope import component
from zope import interface
from zope.component.factory import Factory
from sparc.login.credentials import ICredentialIdentity
from .crypt import ICrypter
from .interfaces import IPasswordHashToken, IPasswordToken


MemoryPasswords = {}

@interface.implementer(IPasswordHashToken)
@component.adapter(ICredentialIdentity)
class MemoryPasswordHashToken(object):
    
    def __init__(self, context):
        self.context = context
        if context.getId() not in MemoryPasswords:
            MemoryPasswords[context.getId()] = ''
    
    @property
    def token(self):
        return MemoryPasswords[self.context.getId()]
    
    @token.setter
    def token(self, value):
        crypter = component.getUtility(ICrypter)
        MemoryPasswords[self.context.getId()] = crypter.hash(value.encode('utf-8'))

@interface.implementer(IPasswordToken)
class PasswordToken(object):
    def __init__(self, token=''):
        self.token = token
    
    @property
    def token(self):
        return self._token
    
    @token.setter
    def token(self, value):
        self._token = value.encode('utf-8')
PasswordTokenFactory = Factory(PasswordToken)