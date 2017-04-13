from zope.interface import Interface
from .identification import IIdentified

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