"""
******
module name
******

Short module descritpion.

long
module
description
if
needed

@author:

"""

import xxx

__all__ = ['function1',
           'function2',
           'function3',
           'etc.']

def function1 (bla, bla bla):
    return ("beginning of the module")

	
	
	
class doc(object):  # long version 
    """
    doc(param1, param2=None, ...)
    
    A documentation.....
    For more information, refer to.....

    Parameters
    ----------
    param1 : description
    param2 : description

    Attributes
    ----------
    A1 : type object
        Description...
    attr2 : type
        Description...
    attr3 : type object
        Describes... the format of the elements in the array.
    

    See Also
    --------
    otherObject1 : Construct something....
    otherObject2 : construct something....

    Notes
    -----
    There are n mode(s) of using doc.....

    Examples
    --------
    First example :
    >>> 
    Second example :
    >>> 
    """
	def short_method(self, p1="aaa", p2=None):  # short version
        """
        r.short_method(p1="bbb", p2=True)
            Returns ............
        Examples
        --------
        >>> 
        """
        pass


def random_function(p1, p2=2, p3=1., p4=None):  # long version
    """
    What the function does, briefly.

    larger description and if needed.
    modules required if any

    Parameters
    ----------
    p1 : Type
       Description

    p2, p3, ... : Type, (optional)
       Description of parameters.

    Returns
    -------
    r1 : type
       Description

    Examples
    --------
    >>> p1 = foo
    >>> resu = random_function(p1)

    Notes
    -----
    Important notes if any.
    """
    import numpy as np  # modules can be imported in functions

    return r1

