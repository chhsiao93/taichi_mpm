import numpy as np
from datasets import load_dataset

ds = load_dataset('chhsiao93/mpm_sand_2d')
print(np.array(ds['train'][1]['x']).shape)