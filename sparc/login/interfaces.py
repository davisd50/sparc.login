from zope.interface import Interface
from zope.interface import Attribute

# LOCATION INFORMATION
class ILocation(Interface):
    """A location"""
    def __eq__(other):
        """True if equal to other"""
    def __ne__(other):
        """True if not equal to other"""
    
class INetworkLocation(ILocation):
    """A network location"""
    def address():
        """String network address"""
    def network():
        """String network"""

class IGeoLocation(ILocation):
    """A geographic location"""
    def latitude():
        """Float latitude of location"""
    def longitude():
        """Float longitude of location"""

# AUTHENTICATION INFORMATION
class IPrincipal(Interface):
    """An entity that can interact with a system."""
    def getId():
        """Return globally unique String identifier for principal"""
    def __str__():
        """Informal object string representation"""
    def __eq__(other):
        """True if equal to other"""
    def __ne__(other):
        """True if not equal to other"""
    def __hash__():
        """Hash based on Id"""
    def __cmp__(other):
        """Principal comparison based on string id."""

class IAuthenticationToken(Interface):
    """Identity validation token"""
    token = Attribute('Token that attempts to validate identity')

class IPasswordToken(IAuthenticationToken):
    """A password"""

class IPasswordHashToken(IAuthenticationToken):
    """A hashed password"""

class IOneTimeKeyToken(IAuthenticationToken):
    """A one time key for identity validation (i.e. 2-factor auth)"""

class ICredentials(Interface):
    """Information to validate identity"""
    identity = Attribute('String identity for authentication')
    tokens = Attribute('Set of IAuthenticationToken to validate identity') 

class IAuthenticationAttempt(Interface):
    """An attempt to authenticate"""
    def credentials():
        """ICredentials used in attempt"""
    def datetime():
        """Aware Python datetime object of event, None if not available"""
    def locations():
        """Set of ILocation objects associated with event"""
    def success():
        """True if attempt was successfull"""