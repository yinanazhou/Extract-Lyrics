import pandas as pd
import numpy as np


PATH = "ml_balanced.xlsx"
SIZE = 200
destination = "output"

i = 0
df = pd.read_excel(PATH)
for chunk in np.array_split(df, SIZE):
    i += 1
    chunk.to_excel(destination + '/lyric_{:03d}.xlsx'.format(i), index=False, header=True)
