from typing import List
from .plot import Plot


class Figure(List[Plot]):
    def show(self, block=True):
        pass