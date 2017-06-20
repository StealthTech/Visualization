import numpy as np
import pandas as pd
import pandas.plotting
import pylab as pl
import os

PROJECT_TITLE = 'Vizualization'
VERSION = '0.5a'

SAMPLES_DIR = 'samples'
SAMPLES_DEFAULT_FILENAME = 'dump.csv'


def version():
    return f'{PROJECT_TITLE} {VERSION}'


def dump(limits, accuracy, filename=SAMPLES_DEFAULT_FILENAME):
    if not os.path.exists(SAMPLES_DIR):
        os.mkdir(SAMPLES_DIR)

    filepath = f'{SAMPLES_DIR}/{filename}'

    steps = []
    for lim in limits:
        steps.append((lim[1] - lim[0]) / accuracy)
    # for step in steps:
    #     print(round(step, 4))

    matrix = [[], ]
    for i in range(0, len(limits)):
        matrix.append([])
        for j in range(accuracy + 1):
            matrix[i + 1].append(round(limits[i][0] + steps[i] * j, 4))
        if i % 2:
            matrix[i + 1].append('first')
        else:
            matrix[i + 1].append('second')

    for i in range(accuracy + 1):
        matrix[0].append(round(
            8.375 -
            0.875 * matrix[1][i] -
            0.125 * matrix[2][i] -
            0.875 * matrix[3][i] -
            0.375 * matrix[4][i] +
            2.375 * matrix[5][i] +
            1.375 * matrix[6][i] +
            1.125 * matrix[2][i] * matrix[3][i] +
            2.625 * matrix[1][i] * matrix[6][i] +
            0.625 * matrix[2][i] * matrix[4][i] * matrix[5][i],
        4))

        matrix = np.array(matrix)
        matrix = matrix.transpose()

    with open(filepath, 'w') as csvfile:
        for row in matrix:
            dumpline = ''
            for element in row:
                dumpline += '{},'.format(element)
            dumpline += '\n'
            csvfile.write(dumpline)

    return matrix


def plot_parallel(filename=SAMPLES_DEFAULT_FILENAME):
    filepath = f'{SAMPLES_DIR}/{filename}'
    data = pd.read_csv(filepath, sep=',')
    pd.plotting.parallel_coordinates(data, 'Name')
    pl.show()


def plot_andrews(filename=SAMPLES_DEFAULT_FILENAME):
    filepath = f'{SAMPLES_DIR}/{filename}'
    data = pd.read_csv(filepath, sep=',')
    pd.plotting.andrews_curves(data, 'Name')
    pl.show()