class Action:
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def __call__(self, *args, **kwds):
        return self.func(*args, **kwds)

    def __repr__(self):
        return f"Action({self.name})"

    '''@staticmethod
    def class_action(name, instance, func):
        def wrapper(*args, **kwargs):
            print("XX", args, kwargs)
            return func(instance, *args, **kwargs)

        return Action(name, wrapper)'''
