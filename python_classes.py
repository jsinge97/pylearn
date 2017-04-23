# inheritance in python

class example(object):
    """docstring for example"""
    def __init__(self, arg):
        # inherit from a super class
        super(example, self).__init__()
        self.arg = arg
    class example2(object):
        """docstring for example2"""
        def __init__(self, arg):
            super(example2, self).__init__()
            self.arg = arg
            


# classes are attributes in modules

x = example.example2()

# use __X__ to overload things


class ThirdClass(SecondClass): # Inherit from SecondClass
def __init__(self, value): # On "ThirdClass(value)"
self.data = value
def __add__(self, other): # On "self + other"
return ThirdClass(self.data + other)
def __str__(self): # On "print(self)", "str()"
return '[ThirdClass: %s]' % self.data


# extensions

# use __name__ to extend builtin types