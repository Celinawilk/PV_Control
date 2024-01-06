# Copyright 2021 Siemens Corporation
# SPDX-License-Identifier: MIT

import os
import inspect
import re
from powergym.env import Env

# map from system_name to fixed information of the system

_SYS_INFO = {
    '13Bus_PV_Attack': {
        'source_bus': 'sourcebus',
        'node_size': 500,
        'shift': 10,
        'show_node_labels': True
    }
}

# map from env_name to the necessary information
_ENV_INFO = {
    '13Bus_PV_Attack': {
        'system_name': '13Bus_PV_Attack',
        'dss_file': 'IEEE13Nodeckt_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': 33,
        'power_w': 10.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 0.0 / 33,
        'dis_w': 6.0 / 33,
        'enable_FDI': True,
        'attack_start_time': 1.0,
        'attack_end_time': 5.0,
        'attack_position1': ['675'],
        'attack_position2': ['671'],
        'attack_position3': ['634'],
        'attack_strength': [0.05],
        'lower_limit': 0.95,
        'upper_limit': 1.05
    }
}

# add system information to environment
for env in _ENV_INFO.keys():
    sys = _ENV_INFO[env]['system_name']
    _ENV_INFO[env].update(_SYS_INFO[sys])


####################### functions ########################
def get_info_and_folder(env_name):
    # check env scale and env name
    is_scaled = re.match('.*(_s)([0-9]*[.])?[0-9]+?', env_name)
    if is_scaled:
        matched_str = is_scaled.group(0)
        idx = matched_str.rfind('_s')
        env_name = matched_str[:idx]
        scale = float(matched_str[idx + 2:])
    assert env_name in _ENV_INFO, env_name + ' not implemented'

    # get base_info
    base_info = _ENV_INFO[env_name].copy()
    if is_scaled:
        base_info['scale'] = scale
        base_info['soc_w'] = base_info['soc_w'] * (scale ** 2)

    # get folder path
    folder_path = os.path.join(os.path.dirname(os.path.abspath(inspect.getsourcefile(Env))), '..', 'systems')
    folder_path = os.path.abspath(folder_path)
    return base_info, folder_path


def make_env(env_name, dss_act=False, worker_idx=None):
    base_info, folder_path = get_info_and_folder(env_name)

    if worker_idx is None:
        return Env(folder_path, base_info, dss_act)
    else:
        base_file = os.path.join(folder_path, base_info['system_name'], base_info['dss_file'])
        assert os.path.exists(base_file), base_file + ' does not exist'
        fin = open(base_file, 'r')

        with open(base_file[:-4] + '_' + str(worker_idx) + '.dss', 'w') as fout:
            for line in fin:
                if line.strip() == 'redirect loadshape.dss':
                    fout.write('redirect loadshape_' + str(worker_idx) + '.dss\n')
                else:
                    fout.write(line)
        info = base_info.copy()
        info['dss_file'] = info['dss_file'][:-4] + '_' + str(worker_idx) + '.dss'
        info['worker_idx'] = worker_idx
        return Env(folder_path, info, dss_act)


def remove_parallel_dss(env_name, num_workers):
    base_info, folder_path = get_info_and_folder(env_name)
    base_main = os.path.join(folder_path, base_info['system_name'], base_info['dss_file'])
    base_loadshape = os.path.join(folder_path, base_info['system_name'], 'loadshape.dss')

    bases = [base_main, base_loadshape]
    for base in bases:
        for i in range(num_workers):
            fname = base[:-4] + '_' + str(i) + '.dss'
            if os.path.exists(fname):
                os.remove(fname)

