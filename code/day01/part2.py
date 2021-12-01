#!/usr/bin/env python

import argparse, os, sys
import numpy as np

from part1 import load_data, calc_deltas, count_upside_measurements

def smooth_by_three(data:np.ndarray) -> np.ndarray:
    assert(isinstance(data, np.ndarray))
    assert(len(data) > 2)

    a = list()

    for i in range(2, len(data)):
        a.append(data[i-2] + data[i-1] + data[i])
    return np.array(a)

def main():

    parser = argparse.ArgumentParser(description='Day 1, Part 2')
    parser.add_argument('input_filename', type=str, help='Input text')
    args = parser.parse_args()

    data = load_data(args.input_filename)
    smooth_data = smooth_by_three(data)
    deltas = calc_deltas(smooth_data)
    upside_swings = count_upside_measurements(deltas)
    
    print(f'Data:          \t{data}')
    print(f'Smoothed Data: \t{smooth_data}')
    print(f'Smooth Deltas: \t{deltas}')
    print(f'Upside Swings: \t{upside_swings}')


if __name__ == '__main__':
    main()