from sparc.login.identification import  IIdentityManager
from sparc.login.identification import  IIdentity


class IPrincipal(IIdentity):
    """An identity that can interact with a system."""

class IPrincipalManager(IIdentityManager):
    """Manager for IPrincipal providers"""
        