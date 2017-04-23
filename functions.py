def exampleFunction():
    pass

# not evaluated till interpreter gets to this line, can literalyl define in loops.
# executes at runtime

# global scope is in single file only

global exampleOfGlobal

# builtins also have their own scope
# minimize cross file changes

# factory functions

# arguments

# arguments are passed by automatically assigning objects to local varia le names
# assiging to argument names inside a function doesn't affect the caller
# chaning mutables do in fact thoughr

# argument matching

def func(name=value) #default argument value
def func(**name) #collect args in a dictionary
# pass in args as a dictionary

# lambdas

# lambdas are expressions

# generator functions

def gensquares(N):
    for in range(N):
        yield i ** 2

# basically retains enough state to resume the function operations

x = gensquares(4)

# returns a function

next(x)

# 0

next(x)

# 1

# benefit of generator expressions
# don't have to compute the entire object on the spot


# the timing module
