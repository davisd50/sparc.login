from zope import interface
import hashlib
from .interfaces import ICrypter

@interface.implementer(ICrypter)
class Sha512Crypter(object):
    
    def hash(self, secret):
        m = hashlib.sha512()
        m.update(secret)
        return m.hexdigest()
    
    def verify(self, secret, secret_crypt):
        return self.hash(secret) == secret_crypt
