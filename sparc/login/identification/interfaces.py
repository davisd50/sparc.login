from zope import interface

class IIdentified(interface.Interface):
    """An entity that can be uniquely identified among peers"""
    def getId():
        """Return unique String identifier"""

class IIdentity(IIdentified):
    """An entity that can be uniquely identified among peers"""
    def __str__():
        """Informal object string representation"""
    def __repr__():
        """Formal object string representation"""
    def __hash__():
        """Hash based on Identity"""
    # The following are required to support hashing in PY 2, 3
    def __eq__(other):
        """True if equal to other"""
    def __ne__(other):
        """True if not equal to other"""
    def __lt__(other):
        """True if less than other."""
    def __le__(other):
        """True if less than or equal to other."""
    def __gt__(other):
        """True if greater than other."""
    def __ge__(other):
        """True if greater than or equal to other."""

class IIdentityManager(interface.Interface):
    """Generic identity manager for identity systems"""
    def generate(hint=None):
        """Generates and returns a new IIdentity provider
        
        Args:
            hint: String hint to base new identity on.  Implementers may ignore
                  this argument.
        """
    def create(id_token):
        """Creates and returns a new IIdentity provider
        
        Args:
            id_token: Assign identifier String as unique identifier.
        
        Raises:
            InvalidIdentification if identifier is not valid
        """
    
    def get(identifier):
        """Return IIdentity provider for given identifier
        
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

        