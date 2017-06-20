import utils


def base(limits, accuracy):
    print(utils.version())
    print('Available commands:\n'
          f':: dump (filename) :: Dumps new .csv datafile \'filename\' '
          f'(by default \'{utils.SAMPLES_DEFAULT_FILENAME}\')\n'
          ':: plot [andrews|parallel] (filename) :: Plots .csv datafile \'filename\' with selected method '
          f'(by default \'{utils.SAMPLES_DEFAULT_FILENAME}\')\n'
          ':: quit|q :: Shuts down the program\n')
    while True:
        response = input('Enter menu command: ').casefold()
        argv = response.split()
        argc = len(argv)
        if argv[0] == 'dump':
            if argc > 1:
                utils.dump(limits, accuracy, argv[1])
            else:
                utils.dump(limits, accuracy)
        elif argv[0] == 'plot':
            if argc <= 1:
                print('Not enough parameters to plot.\nUsage: plot type (filename)')
                continue
            elif argc == 2:
                if argv[1] == 'andrews':
                    utils.plot_andrews()
                if argv[1] == 'parallel':
                    utils.plot_parallel()
            elif argc == 3:
                if argv[1] == 'andrews':
                    utils.plot_andrews(argv[2])
                if argv[1] == 'parallel':
                    utils.plot_andrews(argv[2])
        elif response == 'quit' or response == 'q':
            print(f'\nThank you for using {utils.version()}! Have a nice day!')
            break


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
    base(task_limits, task_accuracy)
