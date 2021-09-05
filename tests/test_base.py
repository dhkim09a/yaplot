import matplotlib.pyplot as plt
from unittest import TestCase


class TestBase(TestCase):
    pause = .001
    # pause = 1

    def tearDown(self) -> None:
        super().tearDown()

        plt.pause(self.pause)
        plt.close()
