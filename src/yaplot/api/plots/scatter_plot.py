from matplotlib import axes

from ..plot import Plot

class ScatterPlot(Plot):

    def _draw(self, subplot: axes.SubplotBase):
        for points in self:
            if points.dimension != 2:
                raise Exception('yaplot only supports 2D scatter plot for now')

            x, y = map(list, zip(*points))

            args, kwargs = (lambda *a, **ka: (a, ka))(x, y, label=points.name,
                                                    #   **subplot_kwargs
                                                      )

            subplot.scatter(*args, **kwargs)
