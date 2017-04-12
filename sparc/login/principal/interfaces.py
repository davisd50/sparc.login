from sparc.login.identification import  IIdentificationManager
from sparc.login.identification import  IIdentified


class IPrincipal(IIdentified):
    """An entity that can interact with a system."""
    def __str__():
        """Informal object string representation"""
    def __repr__():
        """Formal object string representation"""
    def __hash__():
        """Hash based on Id"""
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

class IPrincipalManager(IIdentificationManager):
    """Manager for principal tokens"""
        