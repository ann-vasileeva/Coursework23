import os
import pandas as pd

sim_res = pd.DataFrame(
    columns=['dd', 'death_r', 'epochs_count', 'area_length_x', 'area_length_y', 'initial_pop', 'b', 'sd_b', 'sd_d', 'd',
             'final_pop'])

folder_path = "/home/anna/Desktop/sim_res"

for subfolder in os.listdir(folder_path):
    subfolder_path = os.path.join(folder_path, subfolder)

    description_file = os.path.join(subfolder_path, 'description.txt')
    population_file = os.path.join(subfolder_path, 'population.csv')

    with open(description_file, 'r') as f:
        description_lines = f.readlines()

    params = {}
    for line in description_lines:
        key, value = line.strip().split('=')
        params[key.strip()] = value.strip()

    population_data = pd.read_csv(population_file)

    final_pop = population_data['pop'].iloc[-1]
    pre_final_pop = population_data['pop'].iloc[-2]

    if len(population_data['pop']) == 2:
        continue

    if final_pop == 0 and pre_final_pop >= 5:
        final_pop = pre_final_pop

    new_row = pd.DataFrame({
        'dd': [params['dd']],
        'death_r': [params['death_r']],
        'epochs_count': [params['epochs_count']],
        'area_length_x': [params['area_length_x']],
        'area_length_y': [params['area_length_y']],
        'initial_pop': [params['initial_pop']],
        'b': [params['b']],
        'sd_b': [params['sd_b']],
        'sd_d': [params['sd_d']],
        'd': [params['d']],
        'final_pop': [final_pop]
    })

    sim_res = pd.concat([sim_res, new_row], ignore_index=True)

sim_res.to_csv('sim_res_3.csv', index=False)
