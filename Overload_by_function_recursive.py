#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Overload_by_function_recursive.py
various overload implementations and examples.
"""

#from __future__ import annotations

# Syntax for decorators with parameters

# @decorator(params)
# def function():
#     ''' Function implementation'''

# The above code is equivalent to

# def function():
#     ''' Function implementation'''

# function = (decorator(params))(function)
# """


import sys


###########################################################################################
    
    
# this functions handle the parameters of decorator : (decorator(params))
def Overload_by_function_recursive(*args_decorator): # this is an iterable of Python types or string representing Python types
    # here we are in incapsulated clozure, so we should have access
    # to *args* deeper and deeper we go incapsulated
    # so code should be shorter than with classes and compartimented function/clozure
    # set side by side without having acess to *args* of others

    # here we do not need to store the *args_decorator
    # as it was done in class decorator

    # >>> create_check_typ([int,float])
    # <function create_check_typ.<locals>.check_typ at 0x7fa6004c0430>
    # >>> foo=create_check_typ([int,float])
    # >>> foo([3,2.5])
    # True
    # >>> foo([3,2])
    # False
    def create_check_typ(Ltyp):

        # x is a type or a string representing a type, result of lambda will always be a string in all case representing the type 
        f_stringify = lambda x : x if type(x) is str else x.__name__

        Ltyp_str = tuple(map(f_stringify,Ltyp))
        
        def check_typ(Lval):

            print("check_typ : Ltyp = {}".format(Ltyp))
            print("check_typ : Ltyp_str = {}".format(Ltyp_str))
            print("check_typ : Lval = {}".format(Lval))

           
            if len(Ltyp) != len(Lval):
                return False
            
            equality = lambda val,typ : val.__class__.__name__ == typ
            
            val_equal_typ = all(map(equality,Lval,Ltyp_str))

            print("check_typ : val_equal_typ = {}".format(val_equal_typ))
            return val_equal_typ
        
        return check_typ

    
    def backup_funct(*dummy_args,**dummy_kwargs):
        print("Overload_by_function_recursive : args = {}".format(dummy_args))
        raise TypeError("Overload_recursive : no method found for the given argument types.")

    
    # we define a function to be used like this : (decorator(params))(function)
    def wrap(function):
        
        # wrap knows *args_decorator
        print ("Inside wrap()")

        print("wrap:  args_decorator = {}".format(args_decorator))

        check_typ_func = create_check_typ(args_decorator)

        name = function.__name__
        print("wrap:  name = {}".format(name))

        module = sys.modules[__name__] # function.__module__ return a string?!
        print("wrap:  module = {}".format(module))

        try:
            function_save = getattr(module, name)

        # in case no function already exist to overload we use backup_funct
        except AttributeError:
            function_save = backup_funct
            

        # this is the final used function
        def wrapped_function(*args_function,**kwargs):

            print("Inside wrapped_function()")
            types = tuple(arg.__class__ for arg in args_function)
            name = function.__name__
            print("  name = {}".format(name))
            print("  types = {}".format(types))
            
            # getting back the good function that match the argument

            if (check_typ_func(args_function)):
                print("  check_typ_func True")
                return function(*args_function,**kwargs)
            else:
                print("  check_typ_func False")
                return function_save(*args_function,**kwargs)

        return wrapped_function
    
    return wrap



# >>> area3(3,4)
# Inside wrapped_function()
#   name = area3
#   types = (<class 'int'>, <class 'int'>)
# check_typ : Ltyp = (<class 'int'>, <class 'int'>)
# check_typ : Lval = (3, 4)
# check_typ : val_equal_typ = True
#   check_typ_func True
# 12
# >>> area3(4)
# Inside wrapped_function()
#   name = area3
#   types = (<class 'int'>,)
# check_typ : Ltyp = (<class 'int'>, <class 'int'>)
# check_typ : Lval = (4,)
#   check_typ_func False
# Inside wrapped_function()
#   name = area3
#   types = (<class 'int'>,)
# check_typ : Ltyp = (<class 'int'>,)
# check_typ : Lval = (4,)
# check_typ : val_equal_typ = True
#   check_typ_func True
# 16
# >>> area3(3,4.3)
# Inside wrapped_function()
#   name = area3
#   types = (<class 'int'>, <class 'float'>)
# check_typ : Ltyp = (<class 'int'>, <class 'int'>)
# check_typ : Lval = (3, 4.3)
# check_typ : val_equal_typ = False
#   check_typ_func False
# Inside wrapped_function()
#   name = area3
#   types = (<class 'int'>, <class 'float'>)
# check_typ : Ltyp = (<class 'int'>,)
# check_typ : Lval = (3, 4.3)
#   check_typ_func False
# Overload_by_function_recursive : args = (3, 4.3)
# Traceback (most recent call last):
#   File "<pyshell#117>", line 1, in <module>
#     area3(3,4.3)
#   File "/Users/mattei/Library/CloudStorage/Dropbox/git/vision3D_python/Overload_by_function_recursive.py", line 110, in wrapped_function
#     return function_save(*args_function,**kwargs)
#   File "/Users/mattei/Library/CloudStorage/Dropbox/git/vision3D_python/Overload_by_function_recursive.py", line 110, in wrapped_function
#     return function_save(*args_function,**kwargs)
#   File "/Users/mattei/Library/CloudStorage/Dropbox/git/vision3D_python/Overload_by_function_recursive.py", line 71, in backup_funct
#     raise TypeError("Overload_recursive : no method found for the given argument types.")
# TypeError: Overload_recursive : no method found for the given argument types.
# >>> 


#@Overload_by_function_recursive(int)
def area_tst(size):
    calc =  size * size
    print (calc)



@Overload_by_function_recursive(int, int)
def area_tst(length, breadth):
    calc = length * breadth
    print (calc)




###########################################################################################
