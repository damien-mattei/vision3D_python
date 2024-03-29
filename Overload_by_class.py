#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# modified by D.MATTEI

"""
OverloadByClass.py
various overload implementations and examples.
"""

from __future__ import annotations

# Syntax for decorators with parameters

# @decorator(params)
# def function():
#     ''' Function implementation'''

# The above code is equivalent to

# def function():
#     ''' Function implementation'''

# function = (decorator(params))(function)
# """

# OverloadByClass.py : Inside Overload_by_class : __init__()
# OverloadByClass.py : Inside Overload_by_class : __init__  : Overload_by_class.nb_deco = 1 
# OverloadByClass.py : Overload_by_class @ 0x7ff4bd41d0a0
#   arg = Vector3D
#   arg = <class 'float'>
# OverloadByClass.py : Inside Overload_by_class : __init__()
# OverloadByClass.py : Inside Overload_by_class : __init__  : Overload_by_class.nb_deco = 2 
# OverloadByClass.py : Overload_by_class @ 0x7ff4bd41da90
#   arg = Vector3D
#   arg = <class 'int'>
# OverloadByClass.py : Inside Overload_by_class : __call__()
#   name = __mul__
#   key = ('__mul__', ('Vector3D', 'int'))
# OverloadByClass.py : Inside Overload_by_class : __call__ : Overload_by_class.nb_deco = 1 

# OverloadByClass.py : Inside Overload_by_class : __call__()
#   name = __mul__
#   key = ('__mul__', ('Vector3D', 'float'))
# OverloadByClass.py : Inside Overload_by_class : __call__ : Overload_by_class.nb_deco = 0 


# >>> v=Vector3D(1,2,3)
# OverloadByClass.py : Inside wrapped_function()
# OverloadByClass : wrapped_function :  name = __init__
# OverloadByClass : wrapped_function :  key = ('__init__', ('Vector3D', 'int', 'int', 'int'))
# # Vector3D constructor #
# >>> v*3
# OverloadByClass.py : Inside wrapped_function()
# OverloadByClass : wrapped_function :  name = __mul__
# OverloadByClass : wrapped_function :  key = ('__mul__', ('Vector3D', 'int'))
# Vector3D.py : __mul__ ('Vector3D', float)
# OverloadByClass.py : Inside wrapped_function()
# OverloadByClass : wrapped_function :  name = __init__
# OverloadByClass : wrapped_function :  key = ('__init__', ('Vector3D', 'int', 'int', 'int'))
# # Vector3D constructor #
# Vector3D @ 0x7fa80941d7c0 [3,6,9]
# >>> v*3.0
# OverloadByClass.py : Inside wrapped_function()
# OverloadByClass : wrapped_function :  name = __mul__
# OverloadByClass : wrapped_function :  key = ('__mul__', ('Vector3D', 'float'))
# Vector3D.py : __mul__ ('Vector3D', float)
# OverloadByClass.py : Inside wrapped_function()
# OverloadByClass : wrapped_function :  name = __init__
# OverloadByClass : wrapped_function :  key = ('__init__', ('Vector3D', 'float', 'float', 'float'))
# # Vector3D constructor #
# Vector3D @ 0x7fa80941db20 [3.0,6.0,9.0]



class Overload_by_class(object) :

    # class attribute (like static in C/C++)
    # will be common to all instanciations of this class
    function_dict = {}
    nb_deco = 0 # number of current decorator for same function overload (in case they are multiple)
    #function_save = None # saved function to be used by all decorator overload in __call__ (in case there is multiple overload for the same function code, example: x + x with x float or int) DEPRECATED

    # this functions handle the parameters of decorator : (decorator(params))
    def __init__(self,*args_decorator):
        
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor but to the __call__ just after
        """
        
        print("OverloadByClass.py : Inside Overload_by_class : __init__()")
        Overload_by_class.nb_deco += 1
        print("OverloadByClass.py : Inside Overload_by_class : __init__  : Overload_by_class.nb_deco = {} ".format(Overload_by_class.nb_deco))
        # wraning: id is valid during the life of the class , it can change for each decorator call.... :-(
        # and even if it is the same it does not guarantee to be the same object as Python can reuse the same
        # memory area for the object type and in reality it is often the case
        print('OverloadByClass.py : Overload_by_class @ {}'.format(hex(id(self))))
        for arg in args_decorator:
            print("  arg = {}".format(arg))
        # store the decorator arguments for this instantiation
        # to use them later in __call__
        self.args_decorator = args_decorator 


    # this function do that: (decorator(params))(function)
    def __call__(self, function):
        
        """
        If there are decorator arguments, __call__() is only called
        once (one time), as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        
        print("OverloadByClass.py : Inside Overload_by_class : __call__()")
        #Overload_by_class.function_save=function # backup the function for other decorator DEPRECATED
        name = function.__name__
        print("  name = {}".format(name))
        
        args_deco=self.args_decorator

        len_args_deco = len(args_deco)
        
        # x is a type or a string representing a type, result of lambda will always be a string in all case representing the type 
        f_stringify = lambda x : x if type(x) is str else x.__name__
        args_deco_string=tuple(map(f_stringify,args_deco))
        
        key = (name,args_deco_string)
        print("  key = {}".format(key))

        default_key = (name,len_args_deco)
        print("  default_key = {}".format(default_key))

        # store function and arguments types in the class attribute dictionary
        Overload_by_class.store(key,function)

        # store function and number of arguments in the class attribute dictionary for the default fallback function to call
        # in case no type match but function name and number of arguments match
        Overload_by_class.store(default_key,function)
        
        
        Overload_by_class.nb_deco -= 1
        print("OverloadByClass.py : Inside Overload_by_class : __call__ : Overload_by_class.nb_deco = {} ".format(Overload_by_class.nb_deco))
        
        print()

        if Overload_by_class.nb_deco == 0:
        
            # this is the function that will be returned
            def wrapped_function(*args_function,**kwargs):

                # getting back the good function that match the argument types
                print("OverloadByClass.py : Inside wrapped_function()")
                types = tuple(arg.__class__.__name__ for arg in args_function)
                name = function.__name__
                print("OverloadByClass : wrapped_function :  name = {}".format(name))
                key = (name,types)
                print("OverloadByClass : wrapped_function :  key = {}".format(key))
                function_found = Overload_by_class.function_dict.get(key)

                if function_found is None:
                    # search by same number of arguments
                    len_args_function = len(args_function)
                    default_key = (name,len_args_function)
                    print("OverloadByClass : wrapped_function :  default_key = {}".format(default_key))
                    function_found = Overload_by_class.function_dict.get(default_key)
                    if function_found is None:
                        raise TypeError('OverloadByClass : wrapped_function : no match : {}'.format(key))

                # returning the evaluation of the previous found function on the arguments
                return function_found(*args_function,**kwargs)
            
            #print("After function_found(*args_function)")

            # return a clozure where it is function_dict
            return wrapped_function # function is wrapped at last step

        else:
            return function # the function remains unchanged for all step (of reading and initializing decorator when many) but last (until the "stack" is empty (nb_deco return to zero)


    # store function and arguments types in the class attribute dictionary
    @classmethod
    def store(cls,key, function):

        print("OverloadByClass : store :")
        print(key)

        # if key in Overload_by_class.function_dict:
        #       raise TypeError("OverloadByClass : store : duplicate registration")
        
        Overload_by_class.function_dict[key] = function

# now this is done: function = (decorator(params))(function)





# example with area:


# = RESTART: /Users/mattei/Library/CloudStorage/Dropbox/git/vision3D_python/Overload_by_class.py =
# OverloadByClass.py : Inside Overload_by_class : __init__()
# OverloadByClass.py : Inside Overload_by_class : __init__  : Overload_by_class.nb_deco = 1 
# OverloadByClass.py : Overload_by_class @ 0x7f81782ace20
#   arg = <class 'int'>
#   arg = <class 'int'>
# OverloadByClass.py : Inside Overload_by_class : __init__()
# OverloadByClass.py : Inside Overload_by_class : __init__  : Overload_by_class.nb_deco = 2 
# OverloadByClass.py : Overload_by_class @ 0x7f81782ac850
#   arg = <class 'int'>
#   arg = <class 'float'>
# OverloadByClass.py : Inside Overload_by_class : __call__()
#   name = area
#   key = ('area', ('int', 'float'))
# OverloadByClass.py : Inside Overload_by_class : __call__ : Overload_by_class.nb_deco = 1 

# OverloadByClass.py : Inside Overload_by_class : __call__()
#   name = area
#   key = ('area', ('int', 'int'))
# OverloadByClass.py : Inside Overload_by_class : __call__ : Overload_by_class.nb_deco = 0 

# OverloadByClass.py : Inside Overload_by_class : __init__()
# OverloadByClass.py : Inside Overload_by_class : __init__  : Overload_by_class.nb_deco = 1 
# OverloadByClass.py : Overload_by_class @ 0x7f81782ace20
#   arg = <class 'int'>
# OverloadByClass.py : Inside Overload_by_class : __call__()
#   name = area
#   key = ('area', ('int',))
# OverloadByClass.py : Inside Overload_by_class : __call__ : Overload_by_class.nb_deco = 0 

@Overload_by_class(int, int)
# def area(length, breadth):
#     calc = length * breadth
#     print (calc)

@Overload_by_class(int, float)
def area(length, breadth):
    calc = length * breadth
    print (calc)


# >>> area(3)
# OverloadByClass.py : Inside wrapped_function()
# OverloadByClass : wrapped_function :  name = area
# OverloadByClass : wrapped_function :  key = ('area', ('int',))
# 9
@Overload_by_class(int)
def area(size):
    calc =  size * size
    print (calc)



    
    
# example with volume:

# Inside Overload_by_class : __init__()
# Inside Overload_by_class : __call__()
#   name = volume
#   key = ('volume', (<class 'int'>,))
# Inside Overload_by_class : __init__()
# Inside Overload_by_class : __call__()
#   name = volume
#   key = ('volume', (<class 'int'>, <class 'int'>, <class 'int'>))

# >>> volume(3)
# Inside wrapped_function()
#   name = volume
#   key = ('volume', (<class 'int'>,))
# 27
# >>> volume(2,3,4)
# Inside wrapped_function()
#   name = volume
#   key = ('volume', (<class 'int'>, <class 'int'>, <class 'int'>))
# 24

# @Overload_by_class(int)
# def volume(size):
#     calc =  size * size *  size
#     print (calc)

# @Overload_by_class(int,int,int)
# def volume(length, breadth,depth):
#     calc =  length * breadth *  depth
#     print (calc)

########################################################################

