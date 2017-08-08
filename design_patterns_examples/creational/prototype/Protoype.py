from copy import deepcopy

class Prototype:
    def __init__(self):
        self._prototypes = {}

    def register_object(self, name, object):
        self._prototypes[name] = object

    def unregister_object(self, name):
        if name in self._prototypes.keys():
            del self._prototypes[name]

    def clone(self, name):
        return deepcopy(self._prototypes[name])

if __name__ == "__main__":
    prototype_manager = Prototype()
    nums = [1, 2, 3, 4] # Object must be mutable!
    prototype_manager.register_object("numbers", nums)
    new_nums = prototype_manager.clone("numbers")

    print(id(nums))
    print(id(new_nums))
