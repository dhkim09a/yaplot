from unittest import TestCase

from yaplot import DataPoints, Figure, LinearPlot
from yaplot import ScatterPlot


class TestUsages(TestCase):

    def test_usage1(self):
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

        fig2 = Figure()
        fig2.append(plot)

        fig2.show()

    # def test_usage2(self):
    #     dp = DataPoints([[0, 1], [1, 2]])

    #     linearPlot = LinearPlot([dp])

    #     fig = Figure([linearPlot])

    #     fig.show()

    # def test_usage3(self):
    #     dp = DataPoints([[0, 1], [1, 2]])
    #     print(dp.dimension)
