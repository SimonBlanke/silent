# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License


import random

import numpy as np


class SearchSpace:
    def __init__(self, start_points, search_config):
        self.start_points = start_points
        self.search_config = search_config

    def create_kerasSearchSpace(self, search_config):
        search_space = {}

        for layer_str in search_config.keys():

            for param_str in search_config[layer_str].keys():
                new_param_str = layer_str + "." + param_str

                search_space[new_param_str] = search_config[layer_str][param_str]

        self.search_space = search_space

    def create_mlSearchSpace(self, search_config):
        self.search_space = search_config[list(search_config.keys())[0]]

    def init_eval(self, n_process):
        hyperpara_indices = None
        if self.start_points:
            for key in self.start_points.keys():
                if key == n_process:
                    hyperpara_indices = self.set_start_position(n_process)

        if not hyperpara_indices:
            hyperpara_indices = self.get_random_position()

        return hyperpara_indices

    def set_start_position(self, n_process):
        pos_dict = {}

        for hyperpara_name in self.search_space.keys():
            search_position = self.search_space[hyperpara_name].index(
                self.start_points[n_process][hyperpara_name]
            )

            pos_dict[hyperpara_name] = search_position

        return pos_dict

    def get_random_position(self):
        """
        get a random N-Dim position in search space and return:
        N indices of N-Dim position (dict)
        """
        pos_dict = {}

        for hyperpara_name in self.search_space.keys():
            n_hyperpara_values = len(self.search_space[hyperpara_name])
            search_position = random.randint(0, n_hyperpara_values - 1)

            pos_dict[hyperpara_name] = search_position

        return pos_dict

    def pos_dict2values_dict(self, pos_dict):
        values_dict = {}

        for hyperpara_name in pos_dict.keys():
            pos = pos_dict[hyperpara_name]
            values_dict[hyperpara_name] = list(self.search_space[hyperpara_name])[pos]

        return values_dict

    def pos_dict2np_array(self, pos_dict):
        return np.array(list(pos_dict.values()))

    def pos_np2values_dict(self, np_array):
        if len(self.search_space.keys()) == np_array.size:
            values_dict = {}
            for i, key in enumerate(self.search_space.keys()):
                pos = int(np_array[i])
                values_dict[key] = list(self.search_space[key])[pos]

            return values_dict
        else:
            raise ValueError("search_space and np_array have different size")