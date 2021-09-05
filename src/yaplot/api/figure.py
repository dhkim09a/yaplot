import matplotlib.figure as mf
import matplotlib.pyplot as plt
from typing import List

from .plot import Plot


class Figure(List[Plot]):
    __figure: mf.Figure = None

    maxcol: int = 4
    padding: float = 0.2
    legend_loc: str = None
    figsize: tuple = None

    def show(self, block=True):
        if self.__figure is None:
            self.__figure = plt.figure(figsize=self.figsize)
            plt.clf()

        for i, plot in enumerate(self):
            sf: plt.subplot = self.__figure.add_subplot(
                int((len(self) - 1) / self.maxcol + 1),
                int(min(len(self), self.maxcol)),
                int(i + 1),
            )

            plot._do_draw(sf)

        # plt.subplots_adjust(left=self.padding)

        plt.show(block=block)
