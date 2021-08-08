import os
import json
import matplotlib.pyplot as plt
from collections import Counter


def get_info(folder):
    artist = []
    title = []
    lyric = []
    mood = []

    for fn in fnames:
        trg_path = os.path.join(in_folder + '/' + fn)
        # print(trg_path)
        with open(trg_path) as f:
            song_info = json.load(f)

        artist.extend(song_info["Artist"])
        title.extend(song_info["Title"])

        lyric_info = {"Lyric": []}
        for l in song_info["Lyric"]:
            lyric_info["Lyric"].extend(l["Lyrics"][0])
        lyric.extend(lyric_info["Lyric"])
        mood.extend(song_info["Mood"])

    return artist, title, lyric, mood


def distribution(tag):
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
    plt.savefig('piechart.png')

    # print info
    print("number of songs: ", len(tag))
    print(plt_labels)
    print(sizes)


if __name__ == "__main__":
    in_folder = "json"
    out_file = "moody.json"

    allowed_exts = ".json"
    fnames = [x for x in os.listdir(in_folder) if x.split('.')[-1] in allowed_exts]

    moodylyrics = {"Artist": [], "Title": [], "Lyric": [], "Mood": []}

    Artist, Title, Lyric, Mood = get_info(in_folder)

    moodylyrics["Artist"].append(Artist)
    moodylyrics["Title"].append(Title)
    moodylyrics["Lyric"].append(Lyric)
    moodylyrics["Mood"].append(Mood)

    distribution(Mood)

    with open(out_file, 'w') as fp:
        json.dump(moodylyrics, fp, indent=4)






