
import os
import sys
import csv


from unidecode import unidecode

comments = []

with open("comments.csv", "r") as commentFile:
    commentReader = csv.reader(commentFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    for row in commentReader:
        comments.append(row[4])

print(comments)

