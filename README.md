# Advent of Code 2022

Welcome to my trash code for the event [Advent of Code 2022](https://adventofcode.com/2021)!

## Setup

This project uses Anaconda and Python.  The YAML configuration file is found in `./environment/environment.yaml`. To set up the environment, execute:

```bash
conda env create -f ./environment/environment.yaml
```

After environment creation, execute:

```bash
conda activate aoc
```

## Execution

Code is kept in `./code/day{day_of_month}`.  Each day will have the set of code used to accomplish the task, example input files, and my own assigned inputs.  These tend to be randomized, so they will not work for your own submission.  The general flow will be:

```bash
python <script>.py <input_file>.txt
```

## GoLang

At some point, I plan to use this event to learn GoLang.  My plan is to first solve each task using Python, then try to recreate it using Go.  It will be in its own separate `./go/` directory. 