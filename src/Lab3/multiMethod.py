registry = {}


class MultiMethod(object):
    # creates a MultiMethod object with a given name and an empty typemap.
    def __init__(self, name):
        self.name = name
        self.typemap = {}

    # Make the object itself callable
    def __call__(self, *args, **kwargs):
        function = self.check_type(args, kwargs)
        return function(*args, **kwargs)

    def check_type(self, args, kwargs):
        type_list = list(self.typemap.keys())
        input_list = [arg for arg in args]
        for value in kwargs.values():
            input_list.append(value)
        for a in type_list:
            if len(a) == len(input_list):
                flag = 1
                for i in range(len(a)):
                    if isinstance(input_list[i], a[i]) is False:
                        flag = 0
                if flag == 1:
                    return self.typemap.get(a)
        raise TypeError("no match")

    # adds a new function to the typemap
    def register(self, types, function):
        if types in self.typemap:
            raise TypeError("duplicate registration")
        self.typemap[types] = function


# Returns a multimethod object and calls the register method
def multimethod(*types):
    def register(function):
        function = getattr(function, "__lastreg__", function)
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = MultiMethod(name)
        mm.register(types, function)
        mm.__lastreg__ = function
        return mm
    return register