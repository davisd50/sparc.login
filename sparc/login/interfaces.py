from zope.interface import Interface
from zope.interface import Attribute
from .identification import IIdentified

class IAuthenticationToken(Interface):
    """Identity validation token"""
    token = Attribute('Token that attempts to validate identity')

class IPasswordToken(IAuthenticationToken):
    """A password"""

class IPasswordHashToken(IAuthenticationToken):
    """A hashed password"""

class IPersistentKeyToken(IAuthenticationToken):
    """A identifier used as an authentication token (i.e. browser cookie)
    
    Carefull: this is not a session id (which would be considered an identity).
    This is intended for the case of when a site realizes your logging in from a
    new asset and asks if it can 'remember' you on that asset.
    """

class IOneTimeKeyToken(IAuthenticationToken):
    """A one time key for identity validation (i.e. 2-factor auth)"""

class IAnsweredQuestionToken(IAuthenticationToken):
    """A token representing an answered question"""

class IIdentity(Interface):
    """Identity token"""
    identity = Attribute('String identity for authentication')

class ICredentials(IIdentity):
    """Information to validate identity"""
    tokens = Attribute('Set of IAuthenticationToken to validate identity') 

class IAuthenticationAttempt(IIdentified):
    """An attempt to authenticate"""
    def system():
        """Returns sparc.asset.system.ISystem being logged into"""
    def datetime():
        """Aware Python datetime object of event, None if not available"""
    def host():
        """Returns sparc.asset.IAsset for system that logged event"""
    def credentials():
        """ICredentials used in attempt"""
    def locations():
        """Set of sparc.asset.location.ILocation objects associated with event"""
    def result():
        """IAuthenticationResult of authentication attempt"""

class IAuthenticationAttempts(Interface):
    """A generator of ordered authentication attempts"""
    def __iter__():
        """Iterator of ordered IAuthenticationAttempt"""

class IAuthenticationResult(Interface):
    """A result related to an authentication attempt"""
    def message():
        """A string message for the result"""

class IAttemptSucceeded(IAuthenticationResult):
    """Authentication was successfull"""

class IAttemptSucceededAuthorized(IAttemptSucceeded):
    """Successfull authentication attempt for authorized user"""

class IAttemptSucceededUnauthorized(IAttemptSucceeded):
    """Successfull authentication attempt for unauthorized user"""

class IAttemptFailed(IAuthenticationResult):
    """Authentication failed"""

class IAttemptFailedUnknownIdentity(IAttemptFailed):
    """Failed authentication attempt due to an unknown identity"""

class IAttemptFailedInvalidAuthenticationToken(IAttemptFailed):
    """Failed authentication attempt due to invalid authentication token"""

class IAttemptFailedInvalidCrendentials(IAttemptFailed):
    """Failed authentication attempt with invalid credentials"""