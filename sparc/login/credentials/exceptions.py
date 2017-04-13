class CredentialValidationFailure(Exception):
    """An attempt to validate credentials did not succeed"""
    
class UnknownIdentity(CredentialValidationFailure):
    """Credential validation failure due to unknown identity"""
    
class InvalidToken(CredentialValidationFailure):
    """Credential validation failure due to invalid authentication token"""

class CanNotProcessToken(CredentialValidationFailure):
    """Credential validation failure due to token type"""
    