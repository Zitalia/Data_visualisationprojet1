# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:02:42 2020

@author: Utilisateur
"""

import pandas as pd
import dataset as ds

df_benef = ds.load_benef()
df_conv = ds.load_conv()
df_remu = ds.load_remu()

df_benef.head()