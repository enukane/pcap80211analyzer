pcap80211analyzer
=================

## Description

802.11 frame pcapng analyzer

## Requirements

- ruby
-- requires faraday
- tshark
- gnuplot (for charter)

## Programs

contains 2 programs

- pcap80211analyzer
- charter

### pcap80211analyzer

Analyzes pcapng which contains 802.11 radiotap frame.
Enter command below to see what can be done.

```sh
% ./pcap80211analyzer -r <pcappath> (list|help)
```

For example, if typed like this...

```
% ./pcap80211analyzer -r $PCAPPATH/test.pcapng uniq_ap_per_band_num
```

it analyzes given pcapng and print out its result.
In this case, the number of APs seen is shown.

```
TotalAP, 3142.0, 100
2.4GHz, 2393, 75.46148949713557
5GHz, 771, 23.83831954169319
both, 22, 0.7001909611712286
```

### charter

Draws some types of bar chart png image from given csv file or csv stdin.

normal usage is like this

```
% ./charter -t bar -o output.png data.csv

or

% cat data.csv | ./charter -t bar -o output.png
```

In combination with pcap80211analyzer

```
% ./pcap80211analyzer -r $PCAPPATH/test.pcapng uniq_ap_oui_histogram | ./charter -t bar -o output.png
```
