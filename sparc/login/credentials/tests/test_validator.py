import os.path
import unittest
from zope import component
import zope.testrunner
from sparc.testing.fixture import test_suite_mixin
from sparc.login.testing import SPARC_LOGIN_INTEGRATION_LAYER

from ..interfaces import ICredentialsValidator
from ..authn import IPasswordHashToken
from ..exceptions import InvalidToken

class SparcValidatorTestCase(unittest.TestCase):
    layer = SPARC_LOGIN_INTEGRATION_LAYER
    
    def test_password_validator(self):
        id1 = component.createObject(u'sparc.login.credential_identity', '1')
        hash_ = IPasswordHashToken(id1)
        hash_.token = 'some secret'
        
        password_good = component.createObject(u'sparc.login.password', 'some secret')
        password_bad = component.createObject(u'sparc.login.password', 'some bad secret')
        
        validator = component.getUtility(ICredentialsValidator, name="sparc.login.password_validator")
        
        creds = component.createObject(u'sparc.login.credentials', identity=id1)
        
        creds.auth_tokens = set([password_good])
        
        validator.validate(creds) #no exception thrown
        self.assertTrue(validator.check(creds))
        with self.assertRaises(InvalidToken):
            creds.auth_tokens = set([password_bad])
            validator.validate(creds)
        self.assertFalse(validator.check(creds))
            
    
class test_suite(test_suite_mixin):
    layer = SPARC_LOGIN_INTEGRATION_LAYER
    package = 'sparc.login.credentials'
    module = 'validator'
    
    def __new__(cls):
        suite = super(test_suite, cls).__new__(cls)
        suite.addTest(unittest.makeSuite(SparcValidatorTestCase))
        return suite

if __name__ == '__main__':
    zope.testrunner.run([
                         '--path', os.path.dirname(__file__),
                         '--tests-pattern', os.path.splitext(
                                                os.path.basename(__file__))[0]
                         ])