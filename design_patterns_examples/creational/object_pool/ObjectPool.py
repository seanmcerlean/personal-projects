class Reusable:
    def __init__(self):
        pass


class ReusablePool:
    def __init__(self, pool_size):
        self._pool = [Reusable() for _ in range(pool_size)]

    def acquire(self):
        try:
            return self._pool.pop()
        except IndexError:
            # Could create new, or wait until one becomes free
            raise IndexError('No objects in pool')

    def release(self, reusable_object):
        assert isinstance(reusable_object, Reusable), \
            'Can only add reusable objects to the pool'

        self._pool.append(reusable_object)


if __name__ == "__main__":
    pool = ReusablePool(2)
    r = pool.acquire()
    pool.release(r)
    l = ['abc']
    pool.release(l)