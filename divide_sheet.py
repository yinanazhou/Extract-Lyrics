import pandas as pd
import numpy as np
import argparse


PATH = "ml_balanced_test.xlsx"
SIZE = 250
destination = "output"

i = 1
df = pd.read_excel(PATH)
for chunk in np.array_split(df, SIZE):
    chunk.to_excel(destination + '/lyric_{:03d}.xlsx'.format(i), index=False, header=True)
    i += 1
