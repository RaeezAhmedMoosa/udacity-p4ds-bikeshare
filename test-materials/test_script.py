# This file will be used as a testing ground, from which code written in the
# "test_code" file will be run. This file will not be included in the final
# version of the "Bikeshare" project.
import numpy as np
import pandas as pd

# File Directory Tests
wdc_data = "./washington.csv"

wdc_data1 = "../bikeshare-data/washington.csv"

wdc_df = pd.read_csv(wdc_data1)

print(type(wdc_df))
