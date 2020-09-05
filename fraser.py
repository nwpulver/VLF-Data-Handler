# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:31:36 2020

@author: Nathan
"""

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(
    description="Takes file formatted from VLF_extract and calculates Fraser Tilt. Writes to csv with fraser tilt column"
)
parser.add_argument("file", help="input file to calculate fraser tilt on")
args = parser.parse_args()


def haversine_np(lon1, lat1, lon2, lat2):
    """
    from https://stackoverflow.com/questions/29545704/fast-haversine-approximation-python-pandas/29546836#29546836
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    All args must be of equal length.

    """
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2

    c = 2 * np.arcsin(np.sqrt(a))
    m = 6378137 * c
    return m


VLF = pd.read_csv(args.file, sep=" ")

ip = VLF["ip"].values
fraser = []

fraser = []

for x in range(len(ip)):
    try:
        filt = (ip[x + 2] + ip[x + 3]) - (ip[x] + ip[x + 1])
        fraser.append(filt)
    except:
        pass
fraser_col = {"Fraser Tilt (%)": fraser}
VLF = pd.concat([VLF, pd.DataFrame(fraser_col)], axis=1)

VLF["Distance along profile (m)"] = haversine_np(
    VLF.Y[0], VLF.X[0], VLF.loc[0:, "Y"], VLF.loc[0:, "X"]
)
plt.figure(figsize=(20, 4))
plt.plot(
    VLF["Distance along profile (m)"],
    VLF["Fraser Tilt (%)"],
    color="orange",
    marker="o",
    linewidth=0,
)
plt.axhline(y=5, color="orange", linestyle="dashed", linewidth=1)
plt.axhline(y=-5, color="orange", linestyle="dashed", linewidth=1)
# plt.plot( VLF['Distance along profile (m)'],VLF['ip'])
plt.ylabel("Fraser Tilt (%)")
plt.xlabel("Distance along profile (m)")
VLF.to_csv(args.file + "_fraser")

plt.savefig(args.file + "_plot.png", format="png")
