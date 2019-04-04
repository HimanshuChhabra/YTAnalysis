#!/usr/bin/python

# Based on: https://developers.google.com/youtube/v3/code_samples/python#create_and_manage_comment_threads
#
# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
#
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets

import httplib2
import os
import sys
import csv
import re

from unidecode import unidecode
from apiclient.discovery import build_from_document
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
from importlib  import reload

reload(sys)
#sys.setdefaultencoding("utf-8")

CLIENT_SECRETS_FILE = "client_secrets.json"
YOUTUBE_READ_WRITE_SSL_SCOPE = "https://www.googleapis.com/auth/youtube.force-ssl"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
MISSING_CLIENT_SECRETS_MESSAGE = "WARNING: Please configure OAuth 2.0"

def get_authenticated_service(args):
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_READ_WRITE_SSL_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)
    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage, args)
    with open("youtube-v3-discoverydocument.json", "r") as f:
        doc = f.read()
    return build_from_document(doc, http=credentials.authorize(httplib2.Http()))

def get_videos(youtube, channelId, maxResults, pageToken):
    result = youtube.search().list(
    part="snippet",
    channelId=channelId,
    pageToken=pageToken,
    order="viewCount",
    publishedAfter="2016-01-01T00:00:00Z",
    publishedBefore="2018-01-01T00:00:00Z",
    safeSearch="none",
    type="video",
    maxResults=maxResults
    ).execute()
    return result

def get_comments(youtube, videoId, maxResults, pageToken):
    result = youtube.commentThreads().list(
    part="snippet",
    videoId=videoId,
    pageToken=pageToken,
    order="relevance",
    textFormat="plainText",
    maxResults=maxResults
    ).execute()
    return result

def clean_str(string):
    string = string.encode("ascii", "ignore");
    string = string.decode('utf-8')
    print(type(string))
    return re.sub(r"\s+", " ", string).strip()

args = argparser.parse_args()
youtube = get_authenticated_service(args)


    
channels = [
  {"category": "comedy", "id": "UC-lHJZR3Gqxm24_Vd_AJ5Yw", "name": "PewDiePie"},
  {"category": "comedy", "id": "UCY30JRSgfhYXA6i6xX1erWg", "name": "SMOSH"},
  {"category": "comedy", "id": "UCY30JRSgfhYXA6i6xX1erWg", "name": "SMOSH"},
  {"category": "comedy", "id": "UCPDXXXJj9nax0fr0Wfc048g", "name": "CollegeHumor"},
  {"category": "comedy", "id": "UCPDis9pjXuqyI7RYLJ-TTSA", "name": "FailArmy"},
  {"category": "comedy", "id": "UC9gFih9rw0zNCK3ZtoKQQyA", "name": "JennaMarbles"},
  {"category": "tv", "id": "UC8-Th83bH_thdKZDJCrn88g", "name": "Fallon"},
  {"category": "tv", "id": "UCi7GJNg51C3jgmYTUwqoUXA", "name": "Conan"},
  {"category": "tv", "id": "UCJ0uqCI0Vqr2Rrt1HseGirg", "name": "Corden"},
  {"category": "tv", "id": "UCa6vGFO9ty8v5KZJXQxdhaw", "name": "Kimmel"},
  {"category": "tv", "id": "UCp0hYYBW6IMayGgR-WeoCvQ", "name": "Ellen"},
  {"category": "science", "id": "UCC552Sd-3nyi_tk2BudLUzA", "name": "AsapSCIENCE"},
  {"category": "science", "id": "UCZYTClx2T1of7BRZ86-8fow", "name": "SciShow"},
  {"category": "science", "id": "UCoxcjq-8xIDTYp3uz647V5A", "name": "Numberphile"},
  {"category": "science", "id": "UCvJiYiBUbw4tmpRSZT2r1Hw", "name": "ScienceChannel"},
  {"category": "science", "id": "UCHnyfMqiRRG1u-2MsSQLbXA", "name": "Veritasium"},
  {"category": "news", "id": "UC1yBKRuGpC1tSM73A0ZjYjQ", "name": "TYT"},
  {"category": "news", "id": "UCBi2mrWuNuyYy4gbM6fU18Q", "name": "ABCNews"},
  {"category": "news", "id": "UCupvZG-5ko_eiXAupbDfxWw", "name": "CNN"},
  {"category": "news", "id": "UCvsye7V9psc-APX6wV1twLg", "name": "AlexJones"},
  {"category": "news", "id": "UCLXo7UDZvByw2ixzpQCufnA", "name": "Vox"}
]

for channel in channels:
    videos = []
    pageToken = None
    comments = []
    
    for _ in range(1):
        if pageToken != False:
            resultVideos = get_videos(youtube, channel["id"], 25, pageToken)  # 25 most watched videos
            videos.extend(resultVideos["items"])
            pageToken = resultVideos.get("nextPageToken", False)
    
    for i, vi in enumerate(videos):
        
        print ("%s: %d" % (channel["name"], i))
        videoId = vi["id"]["videoId"]
        pageToken = None
        
        for _ in range(3):
            if pageToken != False:
                resultComments = get_comments(youtube, videoId, 100, pageToken) # find out 250
                comments.extend(resultComments.get("items", []))
                pageToken = resultComments.get("nextPageToken", False)
            
    with open("comments.csv", "a+") as commentFile:
        commentWriter = csv.writer(commentFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        commentWriter.writerows([["channelId","videoId", "commentId", "author", "text", "replies", "likes", "publishedAt"]])
        for comment in comments:
            clc = comment["snippet"]["topLevelComment"]["snippet"]
            
            commentWriter.writerows([ [
                                      channel["id"],
                                      comment["snippet"]["videoId"],
                                      comment["snippet"]["topLevelComment"]["id"],
                                      clean_str(clc["authorDisplayName"]),
                                      clean_str(clc["textDisplay"]),
                                      comment["snippet"]["totalReplyCount"],
                                      clc["likeCount"],
                                      clc["publishedAt"].encode("ascii", "ignore")
      ]])
            
