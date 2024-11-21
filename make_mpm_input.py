import numpy as np
import json

# reading template file and copy the dictaionary
with open('inputs_2d.json', 'r') as f:
    template = json.load(f)

save_path = '/Users/clawsy/Documents/gnn_fe/data/sand_multi_phi'
id_range = [0,10]
sim_space =[
        [
            0.1,
            0.9
        ],
        [
            0.1,
            0.9
        ]
    ]
cube_width_range = [0.15, 0.3]
cube_aspect_ratio = [0.5, 2.0]
template['save_path'] = save_path
template['id_range'] = id_range
template['sim_space'] = sim_space
template['gen_cube_from_data']['sim_inputs'] = [
    {
        "id": i,
        "mass": {
            "cubes": [
                [
                    x := np.random.uniform(sim_space[0][0], sim_space[0][1]-cube_width_range[0]),
                    y := sim_space[1][0],  # y
                    width := min(np.random.uniform(*cube_width_range), sim_space[0][1] - x),  # width
                    height := np.clip(np.random.uniform(*cube_aspect_ratio) * width, a_min=None, a_max=sim_space[1][1] - y)  # height
                ]
            ],
            "velocity_for_cubes": [
                [
                    0.0,
                    0.0
                ]
            ]
        }
    }
    for i in range(id_range[0], id_range[1])
]
# save the new dictionary to a new file
with open('new_inputs_2d.json', 'w') as f:
    json.dump(template, f, indent=4)