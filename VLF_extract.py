# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:16:40 2020

@author: Nathan Pulver (nwpulver@cpp.edu), Kyle Macy
"""

import argparse
import numpy as np

parser = argparse.ArgumentParser(
    description="Convert raw VLF data from GEM systems computer"
)
parser.add_argument("file", help="input file")
args = parser.parse_args()
path = args.file
# Loading data into numpy array
data = np.loadtxt(path, dtype="str", delimiter="\n", skiprows=0 + 1)
new_data = []
# Only taking VLF data in, not mag
for i in data:
    if len(i) > 75:
        new_data.append(i[1:])

# splitting items within line
data_2 = []
for i in new_data:
    i2 = i.split(" ")
    data_2.append(i2)
# Sorting through data and taking important stuff
x = []
y = []
elev = []
nT = []
sq = []
time = []
a_kHz = []
a_ip = []
a_op = []
a_h1 = []
a_h2 = []
a_pT = []
b_kHz = []
b_ip = []
b_op = []
b_h1 = []
b_h2 = []
b_pT = []
c_kHz = []
c_ip = []
c_op = []
c_h1 = []
c_h2 = []
c_pT = []
for i2 in data_2:
    x.append(i2[0])
    y.append(i2[1])
    elev.append(i2[2])
    nT.append(i2[3])
    sq.append(i2[4])
    time.append(i2[8])
    a_kHz.append(i2[13])
    a_ip.append(i2[14])
    a_op.append(i2[15])
    a_h1.append(i2[16])
    a_h2.append(i2[17])
    a_pT.append(i2[18])
    b_kHz.append(i2[19])
    b_ip.append(i2[20])
    b_op.append(i2[21])
    b_h1.append(i2[22])
    b_h2.append(i2[23])
    b_pT.append(i2[24])
    c_kHz.append(i2[25])
    c_ip.append(i2[26])
    c_op.append(i2[27])
    c_h1.append(i2[28])
    c_h2.append(i2[29])
    c_pT.append(i2[30])
# Removing + in front of positive numbers
for c, i in enumerate(a_ip):
    if "+" in i:
        a_ip[c] = i[1:]
for c, i in enumerate(a_op):
    if "+" in i:
        a_op[c] = i[1:]
for c, i in enumerate(b_ip):
    if "+" in i:
        b_ip[c] = i[1:]
for c, i in enumerate(b_op):
    if "+" in i:
        b_op[c] = i[1:]
for c, i in enumerate(c_ip):
    if "+" in i:
        c_ip[c] = i[1:]
for c, i in enumerate(c_op):
    if "+" in i:
        c_op[c] = i[1:]
# writing files to pathname + khz + vlf.txt
file = open(path + "_" + a_kHz[0] + "_vlf.txt", "w")
file.write("X Y elevation nT sq time kHz ip op h1 h2 pT\n")
for a, b, c, d, e, f, g, h, i, j, k, l in zip(
    x, y, elev, nT, sq, time, a_kHz, a_ip, a_op, a_h1, a_h2, a_pT
):
    file.write(
        "%s %s %s %s %s %s %s %s %s %s %s %s\n" % (a, b, c, d, e, f, g, h, i, j, k, l)
    )

file = open(path + "_" + a_kHz[0] + "_vlf.txt", "w")
file.write("X Y elevation nT sq time kHz ip op h1 h2 pT\n")
for a, b, c, d, e, f, g, h, i, j, k, l in zip(
    x, y, elev, nT, sq, time, a_kHz, a_ip, a_op, a_h1, a_h2, a_pT
):
    file.write(
        "%s %s %s %s %s %s %s %s %s %s %s %s\n" % (a, b, c, d, e, f, g, h, i, j, k, l)
    )
file = open(path + "_" + b_kHz[0] + "_vlf.txt", "w")
file.write("X Y elevation nT sq time kHz ip op h1 h2 pT\n")
for a, b, c, d, e, f, g, h, i, j, k, l in zip(
    x, y, elev, nT, sq, time, b_kHz, b_ip, b_op, b_h1, b_h2, b_pT
):
    file.write(
        "%s %s %s %s %s %s %s %s %s %s %s %s\n" % (a, b, c, d, e, f, g, h, i, j, k, l)
    )

file = open(path + "_" + b_kHz[0] + "_vlf.txt", "w")
file.write("X Y elevation nT sq time kHz ip op h1 h2 pT\n")
for a, b, c, d, e, f, g, h, i, j, k, l in zip(
    x, y, elev, nT, sq, time, b_kHz, b_ip, b_op, b_h1, b_h2, b_pT
):
    file.write(
        "%s %s %s %s %s %s %s %s %s %s %s %s\n" % (a, b, c, d, e, f, g, h, i, j, k, l)
    )
file = open(path + "_" + c_kHz[0] + "_vlf.txt", "w")
file.write("X Y elevation nT sq time kHz ip op h1 h2 pT\n")
for a, b, c, d, e, f, g, h, i, j, k, l in zip(
    x, y, elev, nT, sq, time, c_kHz, c_ip, c_op, c_h1, c_h2, c_pT
):
    file.write(
        "%s %s %s %s %s %s %s %s %s %s %s %s\n" % (a, b, c, d, e, f, g, h, i, j, k, l)
    )

file = open(path + "_" + c_kHz[0] + "_vlf.txt", "w")
file.write("X Y elevation nT sq time kHz ip op h1 h2 pT\n")
for a, b, c, d, e, f, g, h, i, j, k, l in zip(
    x, y, elev, nT, sq, time, c_kHz, c_ip, c_op, c_h1, c_h2, c_pT
):
    file.write(
        "%s %s %s %s %s %s %s %s %s %s %s %s\n" % (a, b, c, d, e, f, g, h, i, j, k, l)
    )
