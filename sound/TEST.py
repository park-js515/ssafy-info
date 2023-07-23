from timeDomain import compare_audio_time_domain
from frequencyDomain import compare_audio_frequency_domain
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

file_types = ("_원본.mp3", "_속도1up.mp3", "_속도1down.mp3",
              "_높낮이1up.mp3", "_높낮이2up.mp3", "_높낮이1down.mp3", "_높낮이2down.mp3")

nar = ("심규선", "조수빈", "민상", "신우")


def testing(idx):
    selected = nar[idx]
    names = tuple(map(lambda x: f"{selected}{x}", file_types))

    df = pd.DataFrame(index=range(7), columns=range(7))
    df_time = pd.DataFrame(index=range(7), columns=range(7))
    df_freq = pd.DataFrame(index=range(7), columns=range(7))

    for i in range(0, 7):
        for j in range(0, i):
            row = f"./nar/{names[i]}"
            col = f"./nar/{names[j]}"
            time_mae, time_cosine = compare_audio_time_domain(row, col)
            freq_mae, freq_cosine = compare_audio_frequency_domain(row, col)
            time_domain = 1 - time_mae + time_cosine
            freq_domain = 1 - freq_mae + freq_cosine
            df.iloc[i, j] = time_domain + freq_domain
            df.iloc[j, i] = time_domain + freq_domain
            df_time.iloc[i, j] = time_domain
            df_time.iloc[j, i] = time_domain
            df_freq.iloc[i, j] = freq_domain
            df_freq.iloc[j, i] = freq_domain

    df = df.apply(pd.to_numeric)
    df.index = file_types
    df.columns = file_types
    df_time = df_time.apply(pd.to_numeric)
    df_time.index = file_types
    df_time.columns = file_types
    df_freq = df_freq.apply(pd.to_numeric)
    df_freq.index = file_types
    df_freq.columns = file_types

    cmap = "PuBu"
    sns.heatmap(df, annot=True, fmt=".3f", cmap=cmap, linewidths=0.01)
    plt.title(f"{selected}'s total")
    plt.tight_layout()
    plt.savefig(f"./img/{selected}'s total.png")
    plt.show()

    cmap = "Oranges"
    sns.heatmap(df_time, annot=True, fmt=".3f", cmap=cmap, linewidths=0.01)
    plt.title(f"{selected}'s time_domain")
    plt.tight_layout()
    plt.savefig(f"./img/{selected}'s time_domain.png")
    plt.show()

    cmap = "Purples"
    sns.heatmap(df_freq, annot=True, fmt=".3f", cmap=cmap, linewidths=0.01)
    plt.title(f"{selected}'s freq_domain")
    plt.tight_layout()
    plt.savefig(f"./img/{selected}'s freq_domain.png")
    plt.show()


for i in range(4):
    testing(i)
