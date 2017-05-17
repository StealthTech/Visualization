import numpy as np
import math
import pylab as pl


def andrews_curve(x, theta):
    curve = []
    for th in theta:
        x1 = x[0] / math.sqrt(2)
        x2 = x[1] * math.sin(th)
        x3 = x[2] * math.cos(th)
        x4 = x[3] * math.sin(2 * th)
        x5 = x[4] * math.cos(2 * th)
        x6 = x[5] * math.sin(3 * th)

        curve.append(x1 + x2 + x3 + x4 + x5 + x6)
    return curve


def dump(limits, accuracy, filename='dump.csv'):
    steps = []
    for lim in limits:
        steps.append((lim[1] - lim[0]) / accuracy)
    for step in steps:
        print(round(step, 4))

    matrix = [[], ]
    for i in range(0, len(limits)):
        matrix.append([])
        for j in range(accuracy + 1):
            matrix[i + 1].append(round(limits[i][0] + steps[i] * j, 4))

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

    # for i in hypercube:
    #     print(round(max(i), 2), i)

    with open(filename, 'w') as csvfile:
        for line in matrix:
            dumpline = ''
            for element in line:
                dumpline += '{},'.format(element)
            dumpline += '\n'
            csvfile.write(dumpline)

    return matrix


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
    dump(task_limits, task_accuracy, 'samples/dump.csv')

    columns = [i for i in range(1001)]
    curves = np.loadtxt('dump.csv', usecols=columns, delimiter=',')

    theta = np.linspace(-math.pi, math.pi, task_accuracy)
    colors = ['k', 'r', 'g', 'b', 'c', 'm', 'y']
    for i in range(len(curves) - 1, -1, -1):
        pl.plot(theta, andrews_curve(curves[i], theta), colors[i])

    pl.xlim(-math.pi, math.pi)
    pl.show()