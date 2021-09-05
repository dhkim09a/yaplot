from yaplot import DataPoints, Figure, ScatterPlot

from .test_base import TestBase

class TestUsages(TestBase):
    def test_usage1(self):
        plot = ScatterPlot()
        plot.append(DataPoints([[0, 1], [1, 2], [2, 3]]))

        fig = Figure()
        fig.append(plot)

        fig.show(block=False)

    def test_usage2(self):
        plot = ScatterPlot()
        plot.append(DataPoints([[0, 1], [1, 2], [2, 3]], name='dp1'))
        plot.append(DataPoints([[0, 2], [1, 3], [2, 4]], name='dp2'))

        plot.legend_loc = 'best'
        plot.xlabel = 'x-axis'
        plot.ylabel = 'y-axis'

        fig = Figure()
        fig.append(plot)
        fig.append(plot)

        fig.show(block=False)
