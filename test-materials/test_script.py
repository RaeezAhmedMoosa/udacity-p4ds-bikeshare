# This file will be used as a testing ground, from which code written in the
# "test_code" file will be run. This file will not be included in the final
# version of the "Bikeshare" project.
import numpy as np
import pandas as pd

# File Directory Tests
ch_data = "./chicago.csv"

ch_df = pd.read_csv(ch_data)

print(type(ch_df))
