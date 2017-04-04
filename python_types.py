import gc
import sys

def string_demo():
    example = "The quick brown fox jumped over the lazy dog"
    print example[1:]
    print example[-1]
    print example[:-1]
    print("top level copy: " + example[:])
    print("turning into list: " + str(list(example)))
    print """ multi line
    string
    """
    # strings are immutable in python
    print example.upper()

def list_demo():
    # list comprehensions
    m = [[1,2,3],[4,5,6],[7,8,9]]

    modified_m = [row[1] + 1 for row in m]
    print modified_m
    modified_m = [i for x in m for i in x if i % 2 == 0]
    print modified_m

def dynamic_typing_demo():
    a = 2
    # change of type
    a = "dog"
    # there are names and there are objects. each object 
    # has an internal type and reference counter for garbage collection
    # gc.collect() if circular reference

def shared_reference_demo():
    a = 3
    b = a
    a = a + 2
    print a
    print b
    l = [1,2]
    m = [1,2]
    print m == l
    print m is list_demo
    print sys.getrefcount(1)
    # weak reference, reference to memory that still can be 
    # garbage collected

def main():
    string_demo()
    list_demo()
    shared_reference_demo()

main()