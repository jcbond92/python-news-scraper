import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

# Word cloud creator credit: Andreas Mueller
# https://amueller.github.io/word_cloud/auto_examples/frequency.html


def createWordCloud(config):
    # create file path to write json
    script_dir = os.path.dirname(__file__)
    rel_path = 'results/' + config['name'] + '.png'
    abs_file_path = os.path.join(script_dir, rel_path)

    # Generate a word cloud image
    text = ' '.join(config['text'])
    wordcloud = WordCloud().generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(abs_file_path)

    print("completed creating word cloud")
