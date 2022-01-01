import matplotlib.pyplot as plt
from global_config import *


# {0: "no_emotion", 1: "ANGER", 2: "DISGUST", 3: "FEAR",
# 4: "HAPPINESS", 5: "SADNESS", 6: "SURPRISE"}
def plot_emo_pols(x1, x2, x3, x4, x5, x6):
    fig, axs = plt.subplots(2, 3)
    col = '#62BCB9'
    axs[0, 0].hist(x1, color=col, range=[1, 5])
    axs[0, 0].set_title(emotion_labels[1])
    axs[0, 1].hist(x2, color=col, range=[1, 5])
    axs[0, 1].set_title(emotion_labels[2])
    axs[0, 2].hist(x3, color=col, range=[1, 5])
    axs[0, 2].set_title(emotion_labels[3])
    axs[1, 0].hist(x4, color=col, range=[1, 5])
    axs[1, 0].set_title(emotion_labels[4])
    axs[1, 1].hist(x5, color=col, range=[1, 5])
    axs[1, 1].set_title(emotion_labels[5])
    axs[1, 2].hist(x6, color=col, range=[1, 5])
    axs[1, 2].set_title(emotion_labels[6])
    for ax in axs.flat:
        ax.set(xlabel='Politeness', ylabel='Utterances')
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()
    plt.show()


# {1: "INFORM", 2: "QUESTION", 3: "DIRECTIVE", 4: "COMMISSIVE"}
def plot_act_pols(x1, x2, x3, x4):
    fig, axs = plt.subplots(2, 2)
    col = '#62BCB9'
    axs[0, 0].hist(x2, color=col, range=[1, 5])
    axs[0, 0].set_title(act_labels[2])
    axs[0, 1].hist(x1, color=col, range=[1, 5])
    axs[0, 1].set_title(act_labels[1])
    axs[1, 0].hist(x3, color=col, range=[1, 5])
    axs[1, 0].set_title(act_labels[3])
    axs[1, 1].hist(x4, color=col, range=[1, 5])
    axs[1, 1].set_title(act_labels[4])
    for ax in axs.flat:
        ax.set(xlabel='Politeness', ylabel='Utterances')
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()
    plt.show()
