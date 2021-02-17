import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
with open(arg.filename) as file :
    n = int(file.readline())
    sum1 = 0
    sum2 = 0
