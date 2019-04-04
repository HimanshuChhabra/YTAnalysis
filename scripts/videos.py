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
import json
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

def get_videos(youtube, maxResults, pageToken):
    result = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    pageToken=pageToken,
    maxResults=maxResults,
    chart="mostPopular"
    ).execute()
    return result

def clean_str(string):
    string = string.encode("ascii", "ignore");
    string = string.decode('utf-8')
    print(type(string))
    return re.sub(r"\s+", " ", string).strip()

args = argparser.parse_args()
youtube = get_authenticated_service(args)

def collect_videos():
    videos = []
    pageToken = None
    
    for _ in range(1):
        if pageToken != False:
            resultVideos = get_videos(youtube, 50, pageToken)
            videos.extend(resultVideos["items"])
            pageToken = resultVideos.get("nextPageToken", False)
                   
    print(json.dumps(videos,indent = 1))
         
    with open("videos.csv", "w+") as videoFile:
        videoWriter = csv.writer(videoFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        videoWriter.writerows([["videoId", "videoTitle", "videoDesc", "videoLike","videoViews","videoDuration"]])
        for video in videos:
            videoWriter.writerows([[
                                    video["id"],
                                    clean_str(video["snippet"]["title"]),
                                    clean_str(video["snippet"]["description"]),
                                    video["statistics"]["likeCount"],
                                    video["statistics"]["viewCount"],
                                    video["contentDetails"]["duration"],
                                                                    
    ]])

          
collect_videos()
    