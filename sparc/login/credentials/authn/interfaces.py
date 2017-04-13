from zope import interface

class IAuthenticationToken(interface.Interface):
    """Identity validation token"""
    token = interface.Attribute('Token that attempts to validate identity')

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