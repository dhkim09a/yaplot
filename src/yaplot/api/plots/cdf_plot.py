from matplotlib import axes
import numpy as np

from ..plot import Plot

class CdfPlot(Plot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.ylabel:
            self.ylabel = 'CDF'

        if not self.ylim:
            self.ylim = (0, 1)

    def _draw(self, subplot: axes.SubplotBase):
        for points in self:
            np.sort(points)

            y = 1. * np.arange(len(points)) / (len(points) - 1)

            args, kwargs = (lambda *a, **ka: (a, ka))(points, y, label=points.name,
                                                    #   **subplot_kwargs
                                                      )

            subplot.plot(*args, **kwargs)
