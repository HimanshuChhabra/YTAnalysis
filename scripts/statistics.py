#!/usr/bin/env python3
import csv
import math
import matplotlib.pyplot as plt

filepath = "csv files/test_data.csv"

answerPercentages = {}

stats = {"Tech": {"positive": 0, "negative": 0, "neutral": 0, "totalCount": 0 },
        "Comedy": {"positive": 0, "negative": 0, "neutral": 0, "totalCount": 0 },
        "News": {"positive": 0, "negative": 0, "neutral": 0, "totalCount": 0 },
        "TV": {"positive": 0, "negative": 0, "neutral": 0, "totalCount": 0 }}

def plot_graph():
    xCoordinates = []
    yCoordinates = []
    xLabels = []
    counter = 1
    
    for val in answerPercentages:
        xCoordinates.append(counter)
        yCoordinates.append(math.floor(answerPercentages[val]["positive"]))
        xLabels.append(val)
        counter += 1

    plt.title("Positive")
    plt.bar(xCoordinates, yCoordinates, tick_label = xLabels, width = 0.8, color = ['green'])
    
    for i, v in enumerate(yCoordinates):
        plt.text(v, i, " "+str(v), color='blue', va='center', fontweight='bold')
    
    
    plt.xlabel('Category')
    plt.ylabel('% of comments')
    plt.show()


if __name__ == "__main__":
    
    
    
    with open(filepath, "r") as commentFile:
        commentReader = csv.reader(commentFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        
        i = 0
        for row in commentReader:
            if i == 0:
                i=1
                continue
        
            (comment,label,category) = (row[0],row[1],row[2])

            if label == "positive":
                stats[category]["positive"] += 1
            elif label == "negative":
                stats[category]["negative"] += 1
            else:
                stats[category]["neutral"] += 1

            stats[category]["totalCount"] += 1

        for value in stats:
            positive = (stats[value]["positive"] / stats[value]["totalCount"]) * 100
            negative = (stats[value]["negative"] / stats[value]["totalCount"]) * 100
            neutral = (stats[value]["neutral"] / stats[value]["totalCount"]) * 100
            
            answerPercentages[value] = {"positive": positive,"negative": negative,"neutral": neutral}

        print(stats)
        print(answerPercentages)

        plot_graph()


