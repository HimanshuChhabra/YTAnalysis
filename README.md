# Main_Repo
# Text Mining and Analysis of YouTube Video Comments and other attributes across various genres:

YouTube being one of the most popular social media platforms with a giant user-base, hosting a wide range of video Categories (Genres) proves to be a very good candidate for text analysis. Our goal is to perform Qualitative, Quantitative and Sentimental Analysis on the comments posted by the users and derive possibly correlated conclusions across 4 selective video categories namely (Science/Tech, Comedy, TV Shows, news/politics). We intend to take a closer look into YouTube comments and determine how these comments correlate to and differ from comments amongst the 4 selected categories using parameters such as “emotions of the users after watching the videos, degree of profanity for each category, amount of effort taken by user to post a comment (Text length), Most popular words used in comments for each category”. We will also perform the power law distribution test considering the total number of video likes vs number of videos with those many likes

# Data-source / Data-Set:
1. Youtube API (https://developers.google.com/youtube/v3/ ) will be used to mine upto 100K comments, 25k for each of the 4 categories (Science/Tech, Comedy, TV Shows, news/politics)
2. We are using https://socialblade.com/youtube/top/100 to select the top youtube channels for our 4 Categories. We will be excluding those channels that target Non-English viewers.
3. We intent to select 25 most-watched videos from our selected channels mainly in the years 2017-2018 which will be mined for comments
4. Upto 500 most relevant first level English comments will be downloaded and saved as csv files.
5. Data will be filtered and cleansed to remove noise.

# Key Features and Data Analysis:
1. Quantitative Analysis: This analysis will be used to identify which are the most popular words used across each category and a comparison word cloud (for 4 categories) will be generated where the font size of the word denotes most occurring words used by the viewers for each category. This information can be used to analyze the extent of vocabulary and how choice of words influence the comments posted by viewers. We will generate graphical visualizing results and derive conclusions. Python Libraries used: numpy, pandas, matplotlib , wordcloud , Pillow.
2. Qualitative Analysis: This analysis will be used for the following: Firstly, identify the length of comments across all categories, this will give us an idea about amount of efforts put in by the viewers to comment after watching the videos. Secondly, we will identify what percentage of the comments are profane for each of the categories, Python Libraries used: numpy, pandas, matplotlib
3. Sentimental Analysis: Sentimental Analysis will be performed over the comments across all the 4 categories to determine the emotions of users after watching the videos and a comparative and correlative study will be done to identify which category has most positive, negative, neutral comments and other related conclusions will be derived and presented using graphical visualization.
We plan to divide the dataset into 70% training and 30% test data. We will make use of NLTK and SK-Learn python libraries to perform Vectorization of Data using TF-IDF approach, and create Linear SVM Model to train and for classification. Other Python Libraries used: NLTK, SK-Learn, numpy, pandas, matplotlib
4. Power Law Distribution Test: We speculate that a power law distribution exists between Video likes vs number of videos with those many likes. Number of videos with huge number of likes will be less as compared to number of videos with an average or less number of likes. We will plot the distribution graph here and present our analysis. Python Libraries used: pandas, matplotlib
