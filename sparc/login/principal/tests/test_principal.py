import os.path
import unittest
from zope import component
import zope.testrunner
from sparc.testing.fixture import test_suite_mixin
from sparc.login.testing import SPARC_LOGIN_INTEGRATION_LAYER

from .. import IPrincipal

class SparcPrincipalTestCase(unittest.TestCase):
    layer = SPARC_LOGIN_INTEGRATION_LAYER
    
    def test_principal_interface(self):
        #mostly, implementation is already test in sparc.login.identification
        prcpl_1 = component.createObject(u"sparc.login.principal", 1)
        self.assertEqual(repr(prcpl_1), '{} provider with token 1'.format(IPrincipal))
    
    
class test_suite(test_suite_mixin):
    layer = SPARC_LOGIN_INTEGRATION_LAYER
    package = 'sparc.login.principal'
    module = 'principal'
    
    def __new__(cls):
        suite = super(test_suite, cls).__new__(cls)
        suite.addTest(unittest.makeSuite(SparcPrincipalTestCase))
        return suite

if __name__ == '__main__':
    zope.testrunner.run([
                         '--path', os.path.dirname(__file__),
                         '--tests-pattern', os.path.splitext(
                                                os.path.basename(__file__))[0]
                         ])