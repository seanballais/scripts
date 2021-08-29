import sys

import matplotlib.pyplot as plt
import pandas as pd

def main(args):
    csv_file = args[0]
    data = pd.read_csv(csv_file, header=None)
    data = data.drop([ data.columns[0] ], axis=1).T
    data.columns = [
        'GA',
        'GWO (c = 2)',
        'GWO (c = 4)',
        'GWO (c = 8)',
        'GWO (c = 12)',
        'PSO'
    ]

    num_rows = len(data.index)
    x_axis_labels = list(range(num_rows))

    data.set_axis(x_axis_labels, axis='index', inplace=True)

    data = data.astype(float)
    data.plot(lw=1, figsize=(20,12))

    plt.title('Fitness Over Time')
    plt.xlabel('Number of Iterations')
    plt.ylabel('Fitness')
    plt.yscale('log')
    plt.show()


if __name__ == '__main__':
    main(sys.argv[1:])
