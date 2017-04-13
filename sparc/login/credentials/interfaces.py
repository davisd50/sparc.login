from zope import interface
from sparc.login.identification import IIdentity, IIdentityManager


class ICredentialIdentity(IIdentity):
    """A credential identity (e.g. username)"""

class ICredentials(interface.Interface):
    """Information to validate identity"""
    identity = interface.Attribute('ICredentialIdentity provider')
    auth_tokens = interface.Attribute('Set of .authn.IAuthenticationToken providers to validate identity') 

class ICredentialIdentityManager(IIdentityManager):
    """A manager for ICredentialIdentity providers"""
    def update(identifier, id_token):
        """Update and return ICredentialIdentity provider with new id_token
        
        Args:
            identifier: String id_token, or IIdentified provider
            id_token: new unique identifier String
        
        Raises:
            InvalidIdentification if identifier or id_token is not valid
        
        Returns ICredentialIdentity provider
        """

class ICredentialsValidator(interface.Interface):
    def validate(credentials):
        """Validate given credentials
        
        Args:
            credentials: sparc.login.ICredentials provider
        
        Raises:
            Some form of CredentialValidationFailure if credentials can not be 
            validated
        """
    def check(credentials):
        """Return True if credentials can be validated
        
        Args:
            credentials: sparc.login.ICredentials provider
        """
