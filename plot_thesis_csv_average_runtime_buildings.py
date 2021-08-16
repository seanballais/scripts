import sys

import matplotlib.pyplot as plt
import pandas as pd

def main(args):
    csv_file = args[0]
    data = pd.read_csv(csv_file, header=None)
    data = data.drop([ data.columns[0] ], axis=1).T
    data.columns = [ 'GA', 'GWO', 'PSO' ]

    num_rows = len(data.index)
    x_axis_labels = [ 8, 20, 30 ]

    data.set_axis(x_axis_labels, axis='index', inplace=True)

    data = data.astype(float)
    data.plot(lw=1, figsize=(20,12), marker='o')

    plt.title('Average Runtime as Number of Buildings Increase')
    plt.xlabel('Number of Buildings')
    plt.ylabel('Average Runtime (s)')
    plt.show()


if __name__ == '__main__':
    main(sys.argv[1:])
