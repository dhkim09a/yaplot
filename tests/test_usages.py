from unittest import TestCase

from yaplot import DataPoints, Figure, LinearPlot


class TestUsages(TestCase):

    def test_usage1(self):
        dp = DataPoints([(0, 1), (1, 2)])

        linearPlot = LinearPlot()
        linearPlot.append(dp)

        fig = Figure()
        fig.append(linearPlot)

        fig.show()

    def test_usage2(self):
        dp = DataPoints([(0, 1), (1, 2)])

        linearPlot = LinearPlot(dp)

        fig = Figure(linearPlot)

        fig.show()