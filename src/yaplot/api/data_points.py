from typing import Iterable


# class Datapoint(tuple):
#     pass


class DataPoints(list):
    def append(self, __object: tuple) -> None:
        return super().append(__object)
    
    def extend(self, __iterable: Iterable[tuple]) -> None:
        return super().extend(__iterable)