import numpy as np
from typing import Any, Iterable


# class Datapoint(tuple):
#     pass

# https://numpy.org/doc/stable/user/basics.subclassing.html#slightly-more-realistic-example-attribute-added-to-existing-array
class DataPoints(np.ndarray):
    __dimension: int

    name: str = ''

    def __new__(cls, *args, name: str = None, **kwargs):
        arr = np.array(*args, **kwargs)
        obj = arr.view(cls)
        obj.name = name
        return obj

    def __array_finalize__(self, obj):

        if obj is None: return

        self.name = getattr(obj, 'name', None)
        # if not hasattr(obj, 'name'):
        #     raise Exception(self.name)

    @property
    def dimension(self) -> int:
        # raise Exception(np.array([[1,2,3],[2,3,4]]).__class__)
        try:
            nr, nc = self.shape
        except ValueError:
            raise Exception('Invalid np')

        if not isinstance(nc, int):
            raise Exception('')

        return nc
