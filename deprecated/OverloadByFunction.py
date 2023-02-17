#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Overload.py
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





###########################################################################################
    
    
# this functions handle the parameters of decorator : (decorator(params))
def overload_by_Function(*args_decorator):
    # here we are in incapsulated clozure, so we should have access
    # to *args* deeper and deeper we go incapsulated
    # so code should be shorter than with classes and compartimented function/clozure
    # set side by side without having acess to *args* of others

    # here we do not need to store the *args_decorator
    # as it was done in class decorator

    # store function and arguments types in the function static dictionary
    def store(function_name__arg_types, function):
        
        overload_by_Function.function_dict[function_name__arg_types] = function

    
    # we define a function to be used like this : (decorator(params))(function)
    def wrap(function):

        # wrap knows *args_decorator
        print ("Inside wrap()")

        name = function.__name__
        print("  name = {}".format(name))
        key = (name,args_decorator)
        print("  key = {}".format(key))

        # store function and arguments types in the function static dictionary
        store(key,function)

        # this is the final used function
        def wrapped_function(*args_function,**kwargs):

            # getting back the good function that match the argument types
            print("Inside wrapped_function()")
            types = tuple(arg.__class__ for arg in args_function)
            name = function.__name__
            print("  name = {}".format(name))
            key = (name,types)
            print("  key = {}".format(key))
            function_found = overload_by_Function.function_dict.get(key)

            if function_found is None:
                raise TypeError("no match")

            # returning the evaluation of the previous found function on the arguments
            return function_found(*args_function,**kwargs)
            print("After function_found(*args_function)")

        return wrapped_function
    
    return wrap



overload_by_Function.function_dict = {}



@overload_by_Function(int)
def area3(size):
    calc =  size * size
    print (calc)


@overload_by_Function(int, int)
def area3(length, breadth):
    calc = length * breadth
    print (calc)






# Inside wrap()
#   name = area3
#   key = ('area3', (<class 'int'>, <class 'int'>))
# Inside wrap()
#   name = area3
#   key = ('area3', (<class 'int'>,))
# >>> area3(2)
# Inside wrapped_function()
#   name = area3
#   key = ('area3', (<class 'int'>,))
# 4
# >>> area3(3,4)
# Inside wrapped_function()
#   name = area3
#   key = ('area3', (<class 'int'>, <class 'int'>))
# 12

###########################################################################################
