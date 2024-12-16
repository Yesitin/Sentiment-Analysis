# Sentiment-Analysis

This project is about sentiment analysis on comments of the Youtube channel Dean Schneider.

For this, at the beginning of the sentiment analysis the comments from the channel are accessed and retrieved by an API and the top 10 comments of each video are determined. Consequently some Analysis is performed on the results. This analysis consists of a overall distribution of each sentiment segment (positive, neutral, negative), most extreme sentiments by showing top positive and top negative comments, and extracting most common words across all comments.  Finally a visualization of a wordcloud completes the whole project. 

The _youtube_API_script.py_ file contains all functions to retrieve youtube channels data. The main work happens in _sentiment analysis.ipynb_.

## Getting started

To set up this repo create a folder for the project on your system (instructions for windows), open a terminal window, write "cd" and paste the folder path `cd "C:\Users\user\path\to\your\folder"`. Then type `git clone https://github.com/Yesitin/Sentiment-Analysis.git` to download the whole repository (ensure that you have installed python and git). 

Next, create a virtual environment in order to avoid dependency conflicts. For this, type into the terminal `python -m venv env`. With `env\Scripts\activate` you start the environment.

Now you can install all dependencies with `pip install -r requirements.txt`. 

After this, you need to get a Youtube API key. For this, you need a Google account and go to _https://console.developers.google.com/?hl=de_. Here create a "New Project", go to "Credentials", "Create Credentials" and finally "API key". Eventually, you can copy the API into _youtube_API_script.py_ and assign it to _api_key_. You find full documentation for Youtube API here: _https://developers.google.com/youtube/v3/getting-started?hl=de_. Now, you need the channel ID of the youtube channel you want to analyze. To get it click on any video of the channel, go to "page source" or "Seitenquelltext" and search for "channelId". Paste the ID into the script. Now you are ready to run the notebook.

