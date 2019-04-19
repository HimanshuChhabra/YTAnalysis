#!/usr/bin/env python3
import requests
import csv
import re
from textblob import TextBlob


csv_filepath = "csv files/"
files = {"Tech": "comments_tech.csv","Comedy": "comments_comedy_good.csv","News":"comments_news.csv","TV":"comments_TV.csv"}


def read_comments(filepath, category):
    comments = []
    with open(filepath, "r") as commentFile:
        commentReader = csv.reader(commentFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        i=0
        for row in commentReader:
            if (i<20000):
                i+=1
                continue
            temp = re.sub(r'[^\w\s\*]','',row[4], flags=re.MULTILINE)
            if len(temp.strip()) > 0:
                comments.append(temp)
            i+=1


    return comments

def write_comments(comments):
    with open("csv files/test_data.csv", "a+") as commentFile:
        commentWriter = csv.writer(commentFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        
        for comment in comments:
            label = ""
            l = [comment,label]
            print(l)
            commentWriter.writerow(l)


if __name__ == "__main__":
    
    list_input = []


    
    for category,filename in files.items():
        list_input += read_comments(csv_filepath+filename, category)

    print("length",len(list_input))

    with open("csv files/test_data.csv", "w") as commentFile:
        commentWriter = csv.writer(commentFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        commentWriter.writerow(["Comment","Label"])

    write_comments(list_input)


