from os import path
import numpy as np
from PIL import Image
#from wordcloud import WordCloud, STOPWORDS
from wordcloud import WordCloud,STOPWORDS
import csv

# get path to script's directory
currdir = path.dirname(__file__)

def readCSV():
    merged =""
    with open('comments_TV.csv') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:
            string = row[4].lower()
            merged+=" "+string
            
    return merged.strip()   


def create_wordcloud(text):
    # create numpy araay for wordcloud mask image
    mask = np.array(Image.open(path.join(currdir, "cloud.png")))

    # create set of stopwords
    stopwords = set(STOPWORDS)
    stopwords.add("video")
    stopwords.add("youtube")
    stopwords.add("one")
    stopwords.add("oregon")

    # create wordcloud object
    wc = WordCloud(background_color="white",
                    max_words=200,
                    mask=mask,
                       stopwords=stopwords)

    # generate wordcloud
    wc.generate(text)

    # save wordcloud
    wc.to_file(path.join(currdir, "wc.png"))

# generate wordcloud
text = readCSV()
create_wordcloud(text)






        