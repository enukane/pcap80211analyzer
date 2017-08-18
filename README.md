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
  - analyze pcapng with specified viewpoint
- charter
  - draw chart from given CSV input
- summarize
  - runs pcap80211analyzer 

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

#### Supported metrics in pcap80211analyzer



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

### summarize

"summarize" runs pcap80211analyze with charter for all interested viewpoints.

- "channel_ap_histogram": number of AP per channel
- "channel_ap_data_histogram": number of APs sending Data frame per channel
- "channel_sta_histogram": number of statsions per channel
- "channel_sta_wo_ap_histogram": number of stations (withoug APs) per channel
- "channel_sta_data_histogram": number of stations sending Data frame per channel
- "channel_sta_data_wo_ap_histogram": number of station (without APs) sending Data frame per channel
- "channel_type_histogram": histogram of frame type (Mgmt/Ctrl/Data) for each channel
- "channel_type_histogram": histogram (with fixed size stached bar) of frame type for each channel
- "subtype_histogram": histogram of each frame subtype
- "subtype_24_histogram": histogram of each frame subtype for 2.4GHz band
- "subtype_5_histogram": histogram of each frame subtype for 5GHz band
- "rate_histogram": data rate histogram
- "rate_24_histogram": data rate histogram for 2.4GHz band
- "rate_5_histogram": data rate histogram for 5GHz band
- "data_rate_histogram": data rate for Data frame histogram
- "data_rate_24_histogram": data rate for Data frame histogram for 2.4Ghz band
- "data_rate_5_histogram": data rate for Data frame histogram for 5GHz band
- "uniq_ap_oui_histogram_10": OUI vendor histogram for unique AP mac address
- "uniq_ap_oui_24_histogram_10": OUI vendor histogram for unique AP mac address for 2.4GHz
- "uniq_ap_oui_5_histogram_10": OUI vendor histogram for unique AP mac address for 5 GHz
- "uniq_sta_oui_histogram_10": OUI vendor histogram for unique station mac address for 5 GHz
- "uniq_sta_with_data_histogram_10": OUI vendor histogram for unique station mac address that sends Data frame
- "channel_datarate_data_histogram": data rate histogram for Data frames (channel x rate heat map)
- "channel_datarate_histogram": data rate histogram for All frame (channel x rate heat map)
- "channel_datarate_data_noretry_histogram": data rate histogram for Data frames which is not RETRY (channel x rate heat map)
- channel utilization (utilization log required)
- "chan_fcs_error_rate": 
- "chan_goodfcs_frame_count"
- "chan_retry_rate"
- "chan_probereq_frame_count"
- "null_data_frame_retry_count"
- "chan_fcs_error_rate"
- "chan_goodfcs_frame_count"
- "chan_retry_rate"
- "chan_probereq_frame_count"
- "null_data_frame_retry_count"
- "ap_recognized_span"
- "sta_wo_ap_recognized_span"
- "sta_wo_ap_recognized_span.unknown"
- "chan_ba_frame_count"
- "chan_data_n_ba_frame_rate"
- "chan_data_n_ba_frame_rate"
- "chan_data_n_ba_frame_rate", "dataonly", {:row_idx => 3})
- "chan_data_n_ba_frame_rate", "dataonly", {:row_idx => 3})
- "chan_data_n_ba_frame_rate", "baonly", {:row_idx => 4})
- "chan_data_n_ba_frame_rate", "databacnt", {:row_idx => 5})
- "chan_data_n_ba_frame_rate", "datacnt", {:row_idx => 6})
- "chan_duration"
- "chan_duration", "ocp", {:row_idx => 3})
- "chan_duration", "ocp", {:row_idx => 3})
- "chan_duration", "data", {:row_idx => 4})
- "chan_duration", "dataocp", {:row_idx => 5})
- "chan_duration", "dataocp", {:row_idx => 5})
- "chan_duration", "datalen", {:row_idx => 6})


