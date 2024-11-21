import numpy as np
import json

# reading template file and copy the dictaionary
with open('inputs_2d.json', 'r') as f:
    template = json.load(f)

save_path = 'examples/sand2d_columns'
id_range = [0,10] # trajectory id e.g., [0, 10] means 10 trajectories from 0 to 9
friction_angle = [30,45] # friction angle range uniformly sampled
sim_space =[
        [
            0.05, # x_min
            0.95  # x_max
        ],
        [
            0.05, # y_min
            0.95 # y_max
        ]
    ]
cube_width_range = [0.15, 0.3] # width range uniformly sampled
cube_aspect_ratio = [0.5, 2.0] # aspect ratio range uniformly sampled
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
                    # x := np.random.uniform(sim_space[0][0], sim_space[0][1]-cube_width_range[0]), # bottom left x
                    x := sim_space[0][0],  # bottom left x
                    y := sim_space[1][0],  # bottom left y
                    width := min(np.random.uniform(*cube_width_range), sim_space[0][1] - x),  # width
                    height := np.clip(np.random.uniform(*cube_aspect_ratio) * width, a_min=None, a_max=sim_space[1][1] - y)  # height
                ]
            ],
            "velocity_for_cubes": [
                [
                    0.0, # vx
                    0.0 # vy
                ]
            ]
        }
    }
    for i in range(id_range[0], id_range[1])
]
template['visualization']['is_save_animation'] = True
# save the new dictionary to a new file
with open('new_inputs_2d.json', 'w') as f:
    json.dump(template, f, indent=4)