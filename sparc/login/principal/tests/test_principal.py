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
        prcpl_1 = component.createObject(u"sparc.login.principal", 1)
        self.assertTrue(IPrincipal.providedBy(prcpl_1))
        self.assertEqual(prcpl_1.getId(), str(1))
        self.assertEqual(prcpl_1.getId(), str(prcpl_1))
        self.assertEqual(repr(prcpl_1), 'Principal with identifier 1')
        self.assertEqual(hash(prcpl_1), hash('1'))
        prcpl_1_b = component.createObject(u"sparc.login.principal", 1)
        self.assertEqual(prcpl_1, prcpl_1_b)
        prcpl_2 = component.createObject(u"sparc.login.principal", 2)
        self.assertNotEqual(prcpl_1, prcpl_2)
        
        #test hashing
        test = {}
        test[prcpl_1] = 'a'
        test[prcpl_1_b] = 'b'
        self.assertEqual(test[prcpl_1],'b')
        test[prcpl_2] = 'c'
        self.assertIn(prcpl_1, test)
        self.assertIn(prcpl_2, test)
        
        s = set()
        s.add(prcpl_1)
        s.add(prcpl_1_b)
        self.assertEqual(len(s), 1)
        s.add(prcpl_2)
        self.assertEqual(len(s), 2)
    
    
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