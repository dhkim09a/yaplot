from matplotlib import axes
from typing import Iterable, List

from .data_points import DataPoints


class Plot(List[DataPoints]):
    name: str = None
    xlabel: str = None
    ylabel: str = None
    xlim: tuple = None
    ylim: tuple = None
    legend_loc: str = None

    def _do_draw(self, subplot: axes.SubplotBase):
        if self.name:
            subplot.title.set_text(self.name)
        if self.xlabel:
            subplot.set_xlabel(self.xlabel)
        if self.ylabel:
            subplot.set_ylabel(self.ylabel)
        if self.xlim:
            subplot.set_xlim(list(self.xlim))
        if self.ylim:
            subplot.set_ylim(list(self.ylim))

        self._draw(subplot)

        if self.legend_loc:
            subplot.legend(loc=self.legend_loc)

    def _draw(self, subplot: axes.SubplotBase):
        raise NotImplementedError
