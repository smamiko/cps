#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:28:32 2020

@author: mamiko
"""
import pandas as pd
import matplotlib as plt


def PlotSpectrum(path):
    data = pd.read_csv(path)
    # print(type(data))
    # print(data)
    x = data["Frequency"]
    y = data["Ta"]
    # print(y)
    plt.plot(x, y)
    plt.savefig('test.pdf')
