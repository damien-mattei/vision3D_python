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
        print("Overload.py : Inside Overload_by_class : __init__()")
        # store the decorator arguments for this instantiation
        # to use them later in the first __call__
        self.args_decorator = args_decorator 


    # this function do that: (decorator(params))(func_name)
    def __call__(self, function):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print("Overload.py : Inside Overload_by_class : __call__()")
        name = function.__name__
        print("  name = {}".format(name))
        args_deco=self.args_decorator
        f_stringify = lambda x : x if type(x) is str else x.__name__
        args_deco_string=tuple(map(f_stringify,args_deco))
        key = (name,args_deco_string)
        print("  key = {}".format(key))

        # store function and arguments types in the class attribute dictionary
        Overload_by_class.store(key,function)

        # this is the function that will be returned
        def wrapped_function(*args_function):

            # getting back the good function that match the argument types
            print("Overload.py : Inside wrapped_function()")
            types = tuple(arg.__class__.__name__ for arg in args_function)
            name = function.__name__
            print("  name = {}".format(name))
            key = (name,types)
            print("  key = {}".format(key))
            function_found = Overload_by_class.function_dict.get(key)

            if function_found is None:
                raise TypeError("no match")

            # returning the evaluation of the previous found function on the arguments
            return function_found(*args_function)
            print("After function_found(*args_function)")

        # return a clozure where it is function_dict
        return wrapped_function


    # store function and arguments types in the class attribute dictionary
    @classmethod
    def store(cls,function_name__arg_types, function):
        
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

    
    # we define a function to be used like this : (decorator(params))(func_name)
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
        def wrapped_function(*args_function):

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
            return function_found(*args_function)
            print("After function_found(*args_function)")

        return wrapped_function
    
    return wrap

overload_by_Function.function_dict = {}

@overload_by_Function(int, int)
def area3(length, breadth):
    calc = length * breadth
    print (calc)



@overload_by_Function(int)
def area3(size):
    calc =  size * size
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
