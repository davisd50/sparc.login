from zope import interface

class IIdentificationManager(interface.Interface):
    """Generic identification manager for identity systems"""
    def generate(hint=None):
        """Generates and returns a new sparc.login.IIdentified provider
        
        Args:
            hint: String hint to base new identity on.  Implementers may ignore
                  this argument.
        """
    def create(id_token):
        """Creates and returns a new sparc.login.IIdentified provider
        
        Args:
            id_token: Assign identifier String as principal's unique identifier.
        
        Raises:
            InvalidIdentification if identifier is not valid
        """
    
    def get(identifier):
        """Return sparc.login.IIdentified provider for given identifier
        
        Args:
            identifier: String id_token, or IIdentified provider
        
        Raises:
            InvalidIdentification if identifier is not valid
        """
    
    def contains(identifier):
        """True if identifier is assigned
        
        Args:
            identifier: String id_token, or IIdentified provider
        """
        
    def remove(identifier):
        """Remove identifier from manager
        
        Args:
            identifier: String id_token, or IIdentified provider
        
        Raises:
            InvalidIdentification if identifier is not valid
        """
    
    def discard(identifier):
        """Remove identifier from manager if available, otherwise does nothing
        
        Args:
            identifier: String id_token, or IIdentified provider
        """

        