import os
import sys

def main(args):
    data_filename = args[0]

    group_freqs = dict()
    num_lines = 0

    with open(data_filename, 'r') as data_file:
        for line in data_file:
            line = line.strip()
            
            group = int(float(line) // 0.1)
            if group in group_freqs:
                group_freqs[group] += 1
            else:
                group_freqs[group] = 1

            num_lines += 1

    for idx in range(0, 10):
        print(f'{idx} - {idx}.999:\t', end='')
        if idx not in group_freqs:
            print(f'0\t(0%)')
        else:
            percentage = (group_freqs[idx] / num_lines) * 100
            print(f'{group_freqs[idx]}\t({percentage}%)')
    
    print(f'Total No. of Lines: {num_lines}')


if __name__ == '__main__':
    main(sys.argv[1:])
