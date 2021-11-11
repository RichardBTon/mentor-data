import pandas as pd
import numpy as np
from total import total_inntekt

vippspath = "./data/vipps_raw.csv"
# with open(vippspath) as f:
#     data = f.readlines()


df = pd.read_csv(vippspath)

customers = df["TEKST"]
print(customers)

# print(åsne)
# print(total_inntekt(åsne))
