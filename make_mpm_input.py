import numpy as np
import json

# reading template file and copy the dictaionary
with open('inputs_2d.json', 'r') as f:
    template = json.load(f)

save_path = "/Users/clawsy/Documents/GitHub/taichi_mpm/data/multi_phi/" # path to save the simulation data
id_range = [0,15] # trajectory id e.g., [0, 10] means 10 trajectories from 0 to 9
friction_angle = [25,55] # friction angle range uniformly sampled
domain_size = 1.0
sim_space =[
        [
            0.1, # x_min
            0.9  # x_max
        ],
        [
            0.1, # y_min
            0.9 # y_max
        ]
    ]
cube_width_range = [0.2, 0.2] # width range uniformly sampled
cube_aspect_ratio = [0.5, 1.5] # aspect ratio range uniformly sampled

template['domain_size'] = domain_size
template['save_path'] = save_path
template['id_range'] = id_range
template['friction_angle'] = friction_angle
template['sim_space'] = sim_space
template['gen_cube_randomly']['generate'] = False # set to False to generate cubes from data
template['gen_cube_from_data']['generate'] = True # set to True to generate cubes from data
template['gen_cube_from_data']['sim_inputs'] = [
    {
        "id": i,
        "mass": {
            "cubes": [
                [
                    x := np.random.uniform(sim_space[0][0], sim_space[0][1] - (width := min(np.random.uniform(*cube_width_range), sim_space[0][1]))),  # bottom left x
                    y := sim_space[1][0],  # bottom left y
                    width,  # width
                    height := np.clip(np.random.uniform(*cube_aspect_ratio) * width, a_min=None, a_max=sim_space[1][1] - sim_space[1][0])  # height
                ]
            ],
            "velocity_for_cubes": [
                [
                    0.0,  # vx
                    0.0  # vy
                ]
            ],
            "material": [3], # sand
        }
    }
    for i in range(id_range[0], id_range[1])
]
template['visualization']['is_save_animation'] = True
# save the new dictionary to a new file
with open('inputs_sand2d_multi_phi.json', 'w') as f:
    json.dump(template, f, indent=4)