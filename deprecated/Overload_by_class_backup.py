#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OverloadByClass.py
various overload implementations and examples.
"""

from __future__ import annotations

# Syntax for decorators with parameters

# @decorator(params)
# def func_name():
#     ''' Function implementation'''

# The above code is equivalent to

# def func_name():
#     ''' Function implementation'''

# func_name = (decorator(params))(func_name)
# """



class Overload_by_class(object) :

    # class attribute (like static in C/C++)
    # will be common to all instanciations of this class
    function_dict = {}

    # this functions handle the parameters of decorator : (decorator(params))
    def __init__(self,*args_decorator):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print("OverloadByClass.py : Inside Overload_by_class : __init__()")
        # wraning: id is valid during the life of the class , it can change for each decorator call.... :-(
        # and even if it is the same it does not guarantee to be the same object as Python can reuse the same
        # memory area for the object type and in reality it is often the case
        print('OverloadByClass.py : Overload_by_class @ {}'.format(hex(id(self))))
        for arg in args_decorator:
            print("  arg = {}".format(arg))
        # store the decorator arguments for this instantiation
        # to use them later in the first __call__
        self.args_decorator = args_decorator 


    # this function do that: (decorator(params))(func_name)
    def __call__(self, function):
        """
        If there are decorator arguments, __call__() is only called
        once (one time), as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print("OverloadByClass.py : Inside Overload_by_class : __call__()")
        #function = getattr(self, "__lastreg__", function)
        name = function.__name__
        print("  name = {}".format(name))
        args_deco=self.args_decorator
        # x is a type or a string representing a type, result of lambda will always be a string in all case representing the type 
        f_stringify = lambda x : x if type(x) is str else x.__name__
        args_deco_string=tuple(map(f_stringify,args_deco))
        key = (name,args_deco_string)
        print("  key = {}".format(key))

        # store function and arguments types in the class attribute dictionary
        Overload_by_class.store(key,function)

        #self.__lastreg__ = function
        print()
        
        # this is the function that will be returned
        def wrapped_function(*args_function):

            # getting back the good function that match the argument types
            print("OverloadByClass.py : Inside wrapped_function()")
            types = tuple(arg.__class__.__name__ for arg in args_function)
            name = function.__name__
            print("OverloadByClass : wrapped_function :  name = {}".format(name))
            key = (name,types)
            print("OverloadByClass : wrapped_function :  key = {}".format(key))
            function_found = Overload_by_class.function_dict.get(key)

            if function_found is None:
                raise TypeError('OverloadByClass : wrapped_function : no match : {}'.format(key))

            # returning the evaluation of the previous found function on the arguments
            return function_found(*args_function)
            print("After function_found(*args_function)")

        # return a clozure where it is function_dict
        return wrapped_function


    # store function and arguments types in the class attribute dictionary
    @classmethod
    def store(cls,function_name__arg_types, function):

        if function_name__arg_types in Overload_by_class.function_dict:
            raise TypeError("OverloadByClass : store : duplicate registration : " + function_name__arg_types)
        Overload_by_class.function_dict[function_name__arg_types] = function


# now this is done: func_name = (decorator(params))(func_name)
        
@Overload_by_class(int, int)
def area(length, breadth):
    calc = length * breadth
    print (calc)


@Overload_by_class(int, float)
def area(length, breadth):
    calc = length * breadth
    print (calc)

@Overload_by_class(int)
def area(size):
    calc =  size * size
    print (calc)


# >>> area(2,3)
# Inside wrapped_function()
#   name = area
#   key = ('area', (<class 'int'>, <class 'int'>))
# 6
# >>> area(2,3.2)
# Inside wrapped_function()
#   name = area
#   key = ('area', (<class 'int'>, <class 'float'>))
# 6.4

# >>> area(2)
# Inside wrapped_function()
#   name = area
#   key = ('area', (<class 'int'>,))
# 4


# Inside Overload_by_class : __init__()
# Inside Overload_by_class : __call__()
#   name = area
#   key = ('area', (<class 'int'>, <class 'int'>))
# Inside Overload_by_class : __init__()
# Inside Overload_by_class : __call__()
#   name = area
#   key = ('area', (<class 'int'>, <class 'float'>))
# Inside Overload_by_class : __init__()
# Inside Overload_by_class : __call__()
#   name = area
#   key = ('area', (<class 'int'>,))
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
# >>> area(3)
# Inside wrapped_function()
#   name = area
#   key = ('area', (<class 'int'>,))
# 9
# >>> area(2,3)
# Inside wrapped_function()
#   name = area
#   key = ('area', (<class 'int'>, <class 'int'>))
# 6
# >>> volume(2,3,4)
# Inside wrapped_function()
#   name = volume
#   key = ('volume', (<class 'int'>, <class 'int'>, <class 'int'>))
# 24

@Overload_by_class(int)
def volume(size):
    calc =  size * size *  size
    print (calc)

@Overload_by_class(int,int,int)
def volume(length, breadth,depth):
    calc =  length * breadth *  depth
    print (calc)

########################################################################

