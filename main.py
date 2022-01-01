import os
from tqdm import tqdm
from data_loader import load_data, read_pol_data
from plot_utils import *
from utility import *
from pprint import pprint

train_data, train_act_data, train_emo_data = load_data(dpath, 'train')
test_data, test_act_data, test_emo_data = load_data(dpath, 'test')
val_data, val_act_data, val_emo_data = load_data(dpath, 'validation')
data = train_data + test_data + val_data

train_data_joined = joinwords(train_data)
test_data_joined = joinwords(test_data)
val_data_joined = joinwords(val_data)


def pr_data(mode):
    import politenessr as pr
    if mode == 'test': data_joined = test_data_joined
    if mode == 'train': data_joined = train_data_joined
    if mode == 'validation': data_joined = val_data_joined
    data_file = os.path.join(dpath, '{}/dialogues_politeness_{}.txt'.format(mode, mode))
    f = open(data_file, 'w')
    for item in tqdm(data_joined):
        prs = str(list(pr.predict(item)))
        f.write(prs + '\n')
    f.close()


# If you want to annotate politeness data, uncomment following ##########
# pr_data('test')
# pr_data('validation')
# pr_data('train')

# Else read the annotated politeness data
test_pols = read_pol_data('test')
val_pols = read_pol_data('validation')
train_pols = read_pol_data('train')


def correlate(utt_data, emo_data, act_data, pol_data):
    emotions, politenesses, dacts = [], [], []
    emo_1_pols, emo_1_acts, emo_2_pols, emo_2_acts = [], [], [], []
    emo_3_pols, emo_3_acts, emo_4_pols, emo_4_acts = [], [], [], []
    emo_5_pols, emo_5_acts, emo_6_pols, emo_6_acts = [], [], [], []
    act_1_pols, act_1_emos, act_2_pols, act_2_emos = [], [], [], []
    act_3_pols, act_3_emos, act_4_pols, act_4_emos = [], [], [], []
    acts_no_emotion, all_emo, all_pols, all_acts, all_data = [], [], [], [], []
    count_no_emo, count_emo, count = 0, 0, 0
    for i in range(len(emo_data)):
        for j in range(len(emo_data[i])):
            em = emo_data[i][j]
            all_emo.append(emotion_labels[em]), all_pols.append(pol_data[i][j])
            all_acts.append(act_labels[act_data[i][j] + 1]), all_data.append(utt_data[i][j])
            count += 1
            if em == 0:
                acts_no_emotion.append(act_data[i][j])
                count_no_emo += 1
            if em == 1 or em == 2 or em == 3 or em == 4 or em == 5 or em == 6:
                emotions.append(emo_data[i][j])
                dacts.append(act_data[i][j])
                politenesses.append(pol_data[i][j])
                count_emo += 1
                if act_data[i][j] == 0:
                    act_1_emos.append(emo_data[i][j])
                    act_1_pols.append(pol_data[i][j])
                if act_data[i][j] == 1:
                    act_2_emos.append(emo_data[i][j])
                    act_2_pols.append(pol_data[i][j])
                if act_data[i][j] == 2:
                    act_3_emos.append(emo_data[i][j])
                    act_3_pols.append(pol_data[i][j])
                if act_data[i][j] == 3:
                    act_4_emos.append(emo_data[i][j])
                    act_4_pols.append(pol_data[i][j])

            if em == 1:
                emo_1_pols.append(pol_data[i][j])
                emo_1_acts.append(act_data[i][j])
            if emo_data[i][j] == 2:
                emo_2_pols.append(pol_data[i][j])
                emo_2_acts.append(act_data[i][j])
            if emo_data[i][j] == 3:
                emo_3_pols.append(pol_data[i][j])
                emo_3_acts.append(act_data[i][j])
            if emo_data[i][j] == 4:
                emo_4_pols.append(pol_data[i][j])
                emo_4_acts.append(act_data[i][j])
            if emo_data[i][j] == 5:
                emo_5_pols.append(pol_data[i][j])
                emo_5_acts.append(act_data[i][j])
            if emo_data[i][j] == 6:
                emo_6_pols.append(pol_data[i][j])
                emo_6_acts.append(act_data[i][j])

    plot_act_pols(act_1_pols, act_2_pols, act_3_pols, act_4_pols)
    plot_emo_pols(emo_1_pols, emo_2_pols, emo_3_pols, emo_4_pols, emo_5_pols, emo_6_pols)
    print('no_emotion utterances {} and emo utts {} total {}'.format(count_no_emo, count_emo, count_no_emo + count_emo))

    sorted_pols = sorted(zip(all_pols, all_acts, all_emo, all_data))
    sorted_pols.reverse()

    print('TOP 10 Polite'), pprint(sorted_pols[0:10], width=250)
    print('TOP 10 Polite_N'), pprint(sorted_pols[20580:20590], width=250)
    print('TOP 10 Neutral'), pprint(sorted_pols[51485:51495], width=250)
    print('TOP 10 ImPolite_N'), pprint(sorted_pols[82380:82390], width=250)
    print('TOP 10 ImPolite'), pprint(sorted_pols[102969:102979], width=250)

    return emotions, politenesses, dacts


emotion, politeness, acts = correlate(test_data_joined + val_data_joined + train_data_joined,
                                      test_emo_data + val_emo_data + train_emo_data,
                                      test_act_data + val_act_data + train_act_data,
                                      test_pols + val_pols + train_pols)

print('done')
