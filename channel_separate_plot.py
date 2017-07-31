import sys
import csv
import time
from optparse import OptionParser
from argparse import ArgumentParser
import matplotlib.pyplot as plt
from datetime import datetime

# 24
CHAN24 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# 24s
CHAN24s = [1, 6, 11]
# 24x
CHAN24x = [2,3,4,5,7,8,9,10,12,13]
# 24xn
CHAN24xn = [2,5,7,10,12]
# 24xf
CHAN24xf = [3,4,8,9,13]
# 52
#CHAN52 = [34, 36, 38, 40, 42, 44, 46, 48]
CHAN52 = [36, 40, 44, 48]
# 53
CHAN53 = [52, 56, 60, 64]
# 56
CHAN56 = [100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140]
# 58
CHAN58 = [ 149, 153, 157, 161, 166 ]

def epoch2datetime(epoch):
    return datetime.fromtimestamp(int(epoch))

def bands2chans(bands):
    chans = []
    if "24" in bands:
        chans = chans + CHAN24
    elif "24s" in bands:
        chans = chans + CHAN24s
    elif "24x" in bands:
        chans = chans + CHAN24x
    elif "24xn" in bands:
        chans = chans + CHAN24xn
    elif "24xf" in bands:
        chans = chans + CHAN24xf
    if "52" in bands:
        chans = chans + CHAN52
    if "53" in bands:
        chans = chans + CHAN53
    if "56" in bands:
        chans = chans + CHAN56
    if "58" in bands:
        chans = chans + CHAN58
    return chans

desc = u'{0} [Args] [Options]\nDetailed options -h or --help'.format(__file__)

parser = OptionParser()

parser.add_option(
    '-i', '--input',
    dest = 'input',
    help = 'csv file to read from'
)

parser.add_option(
    '-b', '--band',
    dest = 'band',
    help = "band to display (24,24s,52,53,56,58 and comma separated string)"
)

parser.add_option(
    '-o', '--output',
    dest = 'output',
    help = "output file (png)"
)

parser.add_option(
    '-c', '--channels',
    dest = 'channels',
    help = "plot only these channels"
)

parser.add_option(
    '-L', '--legend-off',
    action="store_true",
    dest = 'legend_off',
    default = False,
    help = "don't print legend"
)

parser.add_option(
    '-r', '--row',
    dest = 'row_idx',
    default = 2,
    help = "row to plot"
)

options, args = parser.parse_args()

input_fname = options.input
band_str = options.band
output_fname = options.output
channels_selected = options.channels
legend_off = options.legend_off
row_idx = int(options.row_idx)

if input_fname == None:
    raise NameError("no input")

if band_str == None:
    band_str = "24,52,53,56,58"
bands = band_str.split(",")
chans = bands2chans(bands)

if channels_selected:
    chans = map(lambda n:int(n), channels_selected.split(","))
    band_str = channels_selected

if output_fname == None:
    output_fname = input_fname.split(".")[0] + band_str + "_plot.png"

# execute histgram
f = open(input_fname, "r")

data = csv.reader(f)
matrix = {}

for chan in chans:
    matrix[chan] = {"x": [], "y": []}

for row in data:
    time = epoch2datetime(float(row[0]))
    chan = int(row[1])
    val = float(row[row_idx])
    if chan not in chans:
        continue
    matrix[chan]["x"].append(time)
    matrix[chan]["y"].append(val)

plt.figure(figsize=(12,6))
# each chan
for chan in chans:
    if chan not in chans:
        continue
    x = matrix[chan]["x"]
    y = matrix[chan]["y"]
    plt.plot(x, y, label=(str(chan) + "ch"))

plt.gcf().autofmt_xdate()
if legend_off != True:
    plt.legend()
#plt.ylabel("count")
#plt.xlabel("Rate per single time span (%)")
#plt.figure(figsize=(12,6))
plt.tick_params(labelsize=18)
plt.savefig(output_fname, bbox_inches = "tight", pad_inches = 0.0)
