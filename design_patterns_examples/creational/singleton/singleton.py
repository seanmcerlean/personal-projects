import design_patterns_examples.creational.singleton.SingletonModule as SingletonModule

# NB basically impossible to create a true singleton in python
# You can always get at the internals and modify them if you are determined enough

def singleton_decorator(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

class BaseSingleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton1(BaseSingleton):
    y = 0

    def increase(self):
        self.y = self.y + 1

class Singleton2(object, metaclass=MetaSingleton):
    z = 0

    def increase(self):
        self.z = self.z +1

@singleton_decorator
class Singleton3(object):
    a = 0

    def increase(self):
        self.a = self.a + 1

if __name__ == "__main__":
    # Module can act like a singleton but no inheritance
    x = SingletonModule.singleton_function()
    x = SingletonModule.singleton_function()
    print(x)


    # Singletion via a Base Class
    # True class
    # multiple inheritance could mess it up
    sing1 = Singleton1()
    sing1.increase()

    sing2 = Singleton1()
    sing2.increase()
    print(sing1.y)

    # Metaclass
    # True class
    # Covers inheritance
    # Metaclasses freak people out
    meta_sing1 = Singleton2()
    meta_sing1.increase()
    meta_sing2 = Singleton2()
    meta_sing2.increase()
    print(meta_sing1.z)

    # Decorator
    # Can chain deocraotrs if needed
    # Cannot call class methods from it
    dec_sing1 = Singleton3()
    dec_sing1.increase()
    dec_sing2 = Singleton3()
    dec_sing2.increase()
    print(dec_sing1.a)


