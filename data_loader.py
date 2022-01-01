import os
from global_config import *


def load_data(dpath, mode):
    assert mode == 'train' or mode == 'test' or mode == 'validation'
    dial_f = os.path.join(dpath, '{}/dialogues_{}.txt'.format(mode, mode))
    act_f = os.path.join(dpath, '{}/dialogues_act_{}.txt'.format(mode, mode))
    emo_f = os.path.join(dpath, '{}/dialogues_emotion_{}.txt'.format(mode, mode))
    dlg_data, act_data, emo_data = [], [], []
    with open(act_f, 'r') as f:
        lines = f.readlines()
        for l in lines:
            acts = [int(d) - 1 for d in l.strip().split(' ')]  # -1 for range [0,3]
            act_data.append(acts)
    with open(emo_f, 'r') as f:
        lines = f.readlines()
        for l in lines:
            emos = [int(d) for d in l.strip().split(' ')]
            emo_data.append(emos)
    with open(dial_f, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for l in lines:
            turns = [t.strip().split(' ') for t in l.split(STOKEN)]
            if turns[-1] == ['']:
                turns = turns[:-1]
            dlg_data.append(turns)

    return dlg_data, act_data, emo_data


def read_pol_data(mode):
    pol_f = os.path.join(dpath, '{}/dialogues_politeness_{}.txt'.format(mode, mode))
    with open(pol_f, 'r') as f:
        lines = f.readlines()
        politeness_values, pol_count = [], 0
        for l in lines:
            pols = l.strip().split(', ')
            pols_format = []
            for p in pols:
                pol_count += 1
                pols_format.append(float(p.replace('[', '').replace(']', '')))
            politeness_values.append(pols_format)
        print('Total pol utt count {} in {}'.format(pol_count, mode))
    return politeness_values
