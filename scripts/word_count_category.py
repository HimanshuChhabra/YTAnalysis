#!/usr/bin/env python3

import csv
import math
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS


stopwords = set(STOPWORDS)
csv_filepath = "csv files/"
files = {"Tech": "comments_tech.csv","Comedy": "comments_comedy_good.csv","News":"comments_news.csv","TV":"comments_TV.csv"}
average_words_category = []

def count_words_with_file(filepath, category):
    totalRows = 0
    totalWords = 0
    comments = []
    
    with open(filepath, "r") as commentFile:
        commentReader = csv.reader(commentFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        
        for row in commentReader:
            comments.append(row[4].split())
            totalRows += 1
        
        for comment in comments:
            for word in comment:
                if word not in stopwords:
                    totalWords += 1

    return (category, int(math.floor(totalWords/totalRows)))

def plot_graph():
    xCoordinates = []
    yCoordinates = []
    xLabels = []
    counter = 1
    
    for val in average_words_category:
        xCoordinates.append(counter)
        yCoordinates.append(val[1])
        xLabels.append(val[0])
        counter += 1

    plt.bar(xCoordinates, yCoordinates, tick_label = xLabels, width = 0.8, color = ['red', 'green', 'blue','yellow'])

    plt.xlabel('Category')
    plt.ylabel('Words / Comment')
    plt.show()



if __name__ == "__main__":
    
    # Calculating average words per comment for various categories
    for category,filename in files.items():
        average_words_category.append(count_words_with_file(csv_filepath+filename, category))

    # ploting a graph for the statistics collected
    plot_graph()




