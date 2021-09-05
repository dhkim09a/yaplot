from typing import Iterable
from .data_points import DataPoints


class Plot(list):
    def append(self, __object: DataPoints) -> None:
        return super().append(__object)
    
    def extend(self, __iterable: Iterable[DataPoints]) -> None:
        return super().extend(__iterable)