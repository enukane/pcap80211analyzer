import sys
import csv
import time
from optparse import OptionParser
from argparse import ArgumentParser
import matplotlib.pyplot as plt
from datetime import datetime

desc = u'{0} [Args] [Options]\nDetailed options -h or --help'.format(__file__)

parser = OptionParser()

parser.add_option(
    '-i', '--input',
    dest = 'input',
    help = 'csv file to read from'
)

parser.add_option(
    '-o', '--output',
    dest = 'output',
    help = "output file (png)"
)

parser.add_option(
    '-t', '--start-time',
    dest = 'start_time',
    help = "time to start"
)

parser.add_option(
    '-T', '--end-time',
    dest = 'end_time',
    help = "time to end"
)

parser.add_option(
    '-b', '--bin-size',
    dest = 'bin_size',
    help = "bin size"
)

parser.add_option(
    '-n', '--normalize',
    action = "store_true",
    dest = "normalize",
    default = False,
    help = "normalize histogram"
)

parser.add_option(
    '-c', '--color',
    dest = "color",
    default = "blue",
    help = "color"
)

parser.add_option(
    '-Z', '--zero-less',
    action = "store_true",
    dest = 'zeroless'
)

parser.add_option(
    '-L', '--less-than',
    dest = 'less_than',
    default = 0,
    help = "trim less than this value"
)

options, args = parser.parse_args()

input_fname = options.input
output_fname = options.output
start_time = options.start_time
end_time = options.end_time
bin_size = options.bin_size
normalize = options.normalize
color = options.color
zeroless = options.zeroless
less_than = options.less_than

if input_fname == None:
    raise NameError("no input")

#if output_fname == None:
#    output_fname = input_fname.split(".")[0] + ".png"

if bin_size == None:
    bin_size = "50"
bin_size = int(bin_size)

# execute histgram
f = open(input_fname, "r")

data = csv.reader(f)

list = []

for row in data:
    val = float(row[1])
    if zeroless and val == 0:
        continue
    if val < float(less_than):
        continue
    list.append(val)

plt.figure(figsize=(12,6))
plt.hist(list, normed = normalize, bins = bin_size, alpha = 0.5, color = color,
        range = (min(list), max(list)))
print "max : %s\n" % max(list)
print "min : %s\n" % min(list)

# plt.legend()
plt.tick_params(labelsize=18)

# 1024 x 576
if output_fname == None:
    plt.show()
else:
    print output_fname
    plt.savefig(output_fname, bbox_inches = "tight", pad_inches = 0.0)
