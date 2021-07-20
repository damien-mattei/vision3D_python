#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Overload.py
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






    
# Inside __init__()
# Inside __call__()
# After decoration
# Preparing to call sayHello()
# Inside wrapped_f()
# Decorator arguments: hello world 42
# sayHello arguments: say hello argument list
# After f(*args)
# after first sayHello() call
# Inside wrapped_f()
# Decorator arguments: hello world 42
# sayHello arguments: a different set of arguments
# After f(*args)
# after second sayHello() call 

class decoratorWithArguments(object):

        # this functions handle the parameters of decorator : (decorator(params))
        def __init__(self, arg1, arg2, arg3):
            """
            If there are decorator arguments, the function
            to be decorated is not passed to the constructor!
            """
            print ("Inside __init__()")
            self.arg1 = arg1
            self.arg2 = arg2
            self.arg3 = arg3

        # we define a function to be used like this : (decorator(params))(func_name)
        def __call__(self, f):
            """
            If there are decorator arguments, __call__() is only called
            once, as part of the decoration process! You can only give
            it a single argument, which is the function object.
            """
            print ("Inside __call__()")
            # this is the final used function
            def wrapped_f(*args):
                print ("Inside wrapped_f()")
                print ("Decorator arguments:", self.arg1, self.arg2, self.arg3)
                f(*args)
                print ("After f(*args)")

            return wrapped_f

@decoratorWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print ('sayHello arguments:', a1, a2, a3, a4)

print ("After decoration")

print ("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print ("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print ("after second sayHello() call")

###################################################################################



# Inside decoratorFunctionWithArguments()
# Leaving decoratorFunctionWithArguments()
# Inside wrap()
# After decoration
# Preparing to call sayHello()
# Inside wrapped_f()
# Decorator arguments: hello world 42
# sayHello arguments: say hello argument list
# After f(*args)
# after first sayHello() call
# Inside wrapped_f()
# Decorator arguments: hello world 42
# sayHello arguments: a different set of arguments
# After f(*args)
# after second sayHello() call

# this functions handle the parameters of decorator : (decorator(params))
def decoratorFunctionWithArguments(arg1, arg2, arg3):

    print ("Inside decoratorFunctionWithArguments()")
    # we define a function to be used like this : (decorator(params))(func_name)
    def wrap(f):
        
        print ("Inside wrap()")
        # this is the final used function
        def wrapped_f(*args): # we do not know how many arguments have the function f
            print ("Inside wrapped_f()")
            print ("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            print ("After f(*args)")
            
        return wrapped_f
    
    print ("Leaving decoratorFunctionWithArguments()")
    # return a clozure containing wrap and arg1,arg2,arg3
    return wrap


@decoratorFunctionWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print ('sayHello arguments:', a1, a2, a3, a4)

print ("After decoration")

print ("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print ("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print ("after second sayHello() call")


##########################################################################################



# static vars like in C++ using a decorator
def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


@static_vars(counter=0)
def foo():
    foo.counter += 1
    print ("Counter is %d" % foo.counter)


# registry will contains all the MultiMethod objects
# i dislike this solution because registry is a global variable
# which poluate the top-level environment 
registry = {}

# MultiMethod object instance for a given function name
# contains the multiple overloaded function
# so there is one MultiMethod instanciation for all the functions
#  having same name but different types of arguments
class MultiMethod(object):

    def __init__(self, name):

        # store the name and create an empty dictionary
        self.name = name
        self.typemap = {}

        
    def __call__(self, *args):

        # get the types from the arguments
        types = tuple(arg.__class__ for arg in args)
        # check that the function well exist for a given set type of arguments
        function = self.typemap.get(types)

        if function is None:
            raise TypeError("no match")

        # returning the evaluation of the previous found function on the arguments
        return function(*args)

    # store the overloaded function for those particular types
    def store(self, types, function):
        
        self.typemap[types] = function

        
def overload(*types):
    
    def register(function):

        # check first if it exists a previous MultiMethod instanciated
        # in the registry for this particular function name
        name = function.__name__
        mm = registry.get(name)
        
        if mm is None:
            mm = registry[name] = MultiMethod(name)

        # store the overloaded function for those particular types
        mm.store(types, function)
        # return the MultiMethod object
        return mm

    return register


@overload(int, int)
def area(length, breadth):
    calc = length * breadth
    print (calc)
    
###############################################################################

