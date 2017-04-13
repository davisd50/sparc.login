import os.path
import unittest
from zope import component
import zope.testrunner
from sparc.testing.fixture import test_suite_mixin
from sparc.login.testing import SPARC_LOGIN_INTEGRATION_LAYER

from ..crypt import ICrypter
from ..interfaces import IPasswordHashToken

class SparcPasswordTestCase(unittest.TestCase):
    layer = SPARC_LOGIN_INTEGRATION_LAYER
    
    def test_password_adaptation(self):
        cred_identity = component.createObject(u'sparc.login.credential_identity', 'user_1')
        password = IPasswordHashToken(cred_identity)
        
        password.token = 'some secret'
        crypter = component.getUtility(ICrypter)
        self.assertEqual(password.token, crypter.hash('some secret'.encode('utf-8')))
    
class test_suite(test_suite_mixin):
    layer = SPARC_LOGIN_INTEGRATION_LAYER
    package = 'sparc.login.credentials.authn'
    module = 'password'
    
    def __new__(cls):
        suite = super(test_suite, cls).__new__(cls)
        suite.addTest(unittest.makeSuite(SparcPasswordTestCase))
        return suite

if __name__ == '__main__':
    zope.testrunner.run([
                         '--path', os.path.dirname(__file__),
                         '--tests-pattern', os.path.splitext(
                                                os.path.basename(__file__))[0]
                         ])