import os.path
import unittest
from zope import component
import zope.testrunner
from sparc.testing.fixture import test_suite_mixin
from sparc.login.testing import SPARC_LOGIN_INTEGRATION_LAYER

from .. import IIdentity

class SparcIdentityTestCase(unittest.TestCase):
    layer = SPARC_LOGIN_INTEGRATION_LAYER
    
    def test_principal_interface(self):
        id_1 = component.createObject(u"sparc.login.identity", 1)
        self.assertTrue(IIdentity.providedBy(id_1))
        self.assertEqual(id_1.getId(), str(1))
        self.assertEqual(id_1.getId(), str(id_1))
        self.assertEqual(repr(id_1), '{} provider with token 1'.format(IIdentity))
        self.assertEqual(hash(id_1), hash('1'))
        id_1_b = component.createObject(u"sparc.login.identity", 1)
        self.assertEqual(id_1, id_1_b)
        id_2 = component.createObject(u"sparc.login.identity", 2)
        self.assertNotEqual(id_1, id_2)
        
        #test hashing
        test = {}
        test[id_1] = 'a'
        test[id_1_b] = 'b'
        self.assertEqual(test[id_1],'b')
        test[id_2] = 'c'
        self.assertIn(id_1, test)
        self.assertIn(id_2, test)
        
        s = set()
        s.add(id_1)
        s.add(id_1_b)
        self.assertEqual(len(s), 1)
        s.add(id_2)
        self.assertEqual(len(s), 2)
    
    
class test_suite(test_suite_mixin):
    layer = SPARC_LOGIN_INTEGRATION_LAYER
    package = 'sparc.login.identification'
    module = 'identity'
    
    def __new__(cls):
        suite = super(test_suite, cls).__new__(cls)
        suite.addTest(unittest.makeSuite(SparcIdentityTestCase))
        return suite

if __name__ == '__main__':
    zope.testrunner.run([
                         '--path', os.path.dirname(__file__),
                         '--tests-pattern', os.path.splitext(
                                                os.path.basename(__file__))[0]
                         ])