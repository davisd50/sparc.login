import os.path
import unittest
from zope import component
import zope.testrunner
from sparc.testing.fixture import test_suite_mixin
from sparc.login.testing import SPARC_LOGIN_INTEGRATION_LAYER

from .. import ICrypter

class SparcCryptTestCase(unittest.TestCase):
    layer = SPARC_LOGIN_INTEGRATION_LAYER
    
    def test_principal_interface(self):
        crypter = component.getUtility(ICrypter)
        hashed = crypter.hash('my secret'.encode('utf-8'))
        self.assertTrue(crypter.verify('my secret'.encode('utf-8'), hashed))
    
    
class test_suite(test_suite_mixin):
    layer = SPARC_LOGIN_INTEGRATION_LAYER
    package = 'sparc.login.credentials.authn.crypt'
    module = 'crypt'
    
    def __new__(cls):
        suite = super(test_suite, cls).__new__(cls)
        suite.addTest(unittest.makeSuite(SparcCryptTestCase))
        return suite

if __name__ == '__main__':
    zope.testrunner.run([
                         '--path', os.path.dirname(__file__),
                         '--tests-pattern', os.path.splitext(
                                                os.path.basename(__file__))[0]
                         ])