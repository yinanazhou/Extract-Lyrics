import os
import json
import matplotlib.pyplot as plt
from collections import Counter
import argparse

# merge all json files and get statistics


def get_info(folder):
    artist = []
    title = []
    lyric = []
    mood = []

    for fn in fnames:
        trg_path = os.path.join(in_folder + '/' + fn)
        with open(trg_path) as f:
            song_info = json.load(f)

        artist.extend(song_info["Artist"])
        # print(type(song_info["Artist"]))
        title.extend(song_info["Title"])

        lyric_info = {"Lyric": []}
        for l in song_info["Lyric"]:
            lyric_info["Lyric"] = ' '.join(l["Lyrics"][0])

        lyric.extend([lyric_info["Lyric"]])
        mood.extend(song_info["Mood"])

    return artist, title, lyric, mood


def distribution(tag, path):
    # draw distribution

    plt.figure(figsize=(7.8, 5), dpi=80)  # fig size
    plt_labels = list(Counter(tag).keys())  # label
    sizes = list(Counter(tag).values())

    colors = ['mediumaquamarine', 'salmon', 'sandybrown', 'skyblue']  # color of each sector
    explode = (0.01, 0.01, 0.01, 0.01)
    patches, text1, text2 = plt.pie(sizes,
                                    explode=explode,
                                    labels=plt_labels,
                                    colors=colors,
                                    # labeldistance = 1.2,
                                    labeldistance=1.1,
                                    autopct='%3.2f%%',
                                    shadow=False,
                                    startangle=90,
                                    pctdistance=0.75)
    # draw the circle to make donut
    circle = plt.Circle((0, 0), 0.5, fc='white')
    donut = plt.gcf()
    donut.gca().add_artist(circle)
    # patches: pie chart，texts1: label text，texts2: pie chart text
    plt.axis('equal')
    plt.legend(title='Cluster', loc='upper right')
    plt.savefig(path)

    # print info
    print("number of songs: ", len(tag))
    print(plt_labels)
    print(sizes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    in_folder_parser = parser.add_argument('--i', metavar='IN', action='store', help='input folder name', type=str)
    out_file_parser = parser.add_argument('--o', metavar='OUT', action='store', help='out file name', type=str)
    chart_path_parser = parser.add_argument('--chart', metavar='CHART', action='store', help='chart name', type=str)

    args = parser.parse_args()
    in_folder = args.i
    out_file = args.o
    chart_path = args.chart

    allowed_exts = ".json"
    fnames = [x for x in os.listdir(in_folder) if x.split('.')[-1] in allowed_exts]

    moodylyrics = {"Artist": [], "Title": [], "Lyric": [], "Mood": []}

    Artist, Title, Lyric, Mood = get_info(in_folder)

    moodylyrics["Artist"].append(Artist)
    moodylyrics["Title"].append(Title)
    moodylyrics["Lyric"].append(Lyric)
    moodylyrics["Mood"].append(Mood)

    distribution(Mood, chart_path)

    with open(out_file, 'w') as fp:
        json.dump(moodylyrics, fp, indent=4)






