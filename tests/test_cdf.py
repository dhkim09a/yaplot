
from yaplot import DataPoints, Figure, CdfPlot

from .test_base import TestBase

class TestLinear(TestBase):
    def test_linear1(self):
        plot = CdfPlot()
        plot.append(DataPoints([0, 1, 2, 3, 4, 5, 6, 7]))

        fig = Figure()
        fig.append(plot)

        fig.show(block=False)

    def test_linear2(self):
        plot = CdfPlot()
        plot.append(DataPoints([0, 1, 2, 3, 4, 5, 6, 7], name='dp1'))
        plot.append(DataPoints([0, 1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7], name='dp2'))

        plot.legend_loc = 'best'
        plot.xlabel = 'x-axis'
        plot.ylabel = 'y-axis'

        fig = Figure()
        fig.append(plot)
        fig.append(plot)

        fig.show(block=False)
