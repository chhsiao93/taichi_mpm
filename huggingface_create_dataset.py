import numpy as np
from datasets import Dataset
# load mpm data
def gen():
    for i in range(1000):
        mpm_data = np.load(f'adam/train/trajectory{i}.npz', allow_pickle=True)
        trajectory = mpm_data[f'trajectory{i}']
        x = trajectory[0][:,:,0]
        y = trajectory[0][:,:,1]
        v_x = x[1:] - x[:-1]
        v_y = y[1:] - y[:-1] 
        mat = trajectory[1]
        n_particles = mat.shape[0]
        n_steps = x.shape[0]
        friction_angle = trajectory[-1]
        # create dataset dict
        dataset_dict = {'x': x, 'y': y, 'v_x': v_x, 'v_y': v_y, 'mat': mat, 'n_particles': n_particles, 'n_steps': n_steps, 'friction_angle': friction_angle}
        yield dataset_dict

ds = Dataset.from_generator(gen, cache_dir='huggingface_cache') # by default is "~/.cache/huggingface/datasets", which will make the home directory on TACC explode. That's why I specify a folder for cache files.
ds.push_to_hub('chhsiao93/mpm_sand_2d')