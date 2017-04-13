from zope import component
from zope import interface
from .exceptions import CredentialValidationFailure, CanNotProcessToken, InvalidToken
from .interfaces import ICredentialsValidator

from .authn import IPasswordToken, IPasswordHashToken
from .authn.crypt import ICrypter

@interface.implementer(ICredentialsValidator)
class PasswordValidator(object):
    """A Password validator
    
    This can only handle credtials that contain .authn.IPasswordToken type
    auth tokens.
    
    This validator has 2 dependencies:
     - ICrypter: this should be an un-named utility that is responsible for hashing and checking
     - IPasswordHashToken: This is an adapter for sparc.login.credentials.ICredentialIdentity.
    """
    def validate(self, credentials):
        crypter = component.getUtility(ICrypter)
        for auth_token in credentials.auth_tokens:
            if not IPasswordToken.providedBy(auth_token):
                raise CanNotProcessToken('implementation unable to process tokens not providing {}'.format(IPasswordToken))
            hashed_passwd_token = IPasswordHashToken(credentials.identity)
            if not crypter.verify(auth_token.token, hashed_passwd_token.token):
                raise InvalidToken('invalid password token')

    def check(self, credentials):
        try:
            self.validate(credentials)
            return True
        except CredentialValidationFailure:
            return False