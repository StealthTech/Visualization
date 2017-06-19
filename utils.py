import numpy as np

SAMPLES_DIR = 'samples'


def dump(limits, accuracy, filename='dump.csv'):
    filepath = f'{SAMPLES_DIR}/{filename}'

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