from zope import interface


class ICrypter(interface.Interface):
    """A crypto hasher"""
    def hash(secret):
        """Return string hash of secret"""
    def verify(secret, secret_crypt):
        """True if hash of secret matches string secret_crypt"""