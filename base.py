import pandas as pd
from pandas.plotting import parallel_coordinates, andrews_curves

import utils


if __name__ == '__main__':
    task_limits = [
        [0.36, 1.8],
        [0.8, 4],
        [1, 4.5],
        [1472.6, 3610.9],
        [15, 120],
        [200000, 237500],
    ]
    task_accuracy = 1000
    utils.dump(task_limits, task_accuracy)
    