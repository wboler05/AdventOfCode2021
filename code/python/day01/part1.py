#!/usr/bin/env python

import argparse, os, sys
import numpy as np
from numpy.lib.arraysetops import isin

def load_data(input_filename: str) -> np.ndarray:
    assert(os.path.exists(input_filename))
    assert(os.path.isfile(input_filename))

    data = None
    with open(input_filename, 'r') as ifile:
        data = [d for d in ifile.read().splitlines() if len(d) > 0]

    data = np.array(data).astype(int)
    return data

def calc_deltas(data:np.ndarray) -> np.ndarray:
    assert(isinstance(data, np.ndarray))
    assert(len(data) > 1)

    deltas = data[1:] - data[:-1]

    return deltas

def count_upside_measurements(deltas: np.ndarray) -> int:
    assert(isinstance(deltas, np.ndarray))
    
    if len(deltas) == 0:
        return 0
    else:
        upside_swings = deltas[deltas > 0]
        return len(upside_swings)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_filename', type=str, help='Input text in a file')
    args = parser.parse_args()

    data = load_data(args.input_filename)
    deltas = calc_deltas(data)
    upside_swings = count_upside_measurements(deltas)

    print(f'Data:   \t{data}')
    print(f'Deltas: \t{deltas}')
    print(f'Upside Swings: {upside_swings}')

if __name__ == '__main__':
    main()