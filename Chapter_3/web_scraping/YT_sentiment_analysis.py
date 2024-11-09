import os
import csv
import googleapiclient.discovery
from textblob import TextBlob
import pandas as pd

# Set up YouTube API key and video ID
API_KEY = "AIzaSyAEuzGPhlXUWLdh2O-Aeo7zfkrc6rjJOmg"  # Replace with your actual API key
VIDEO_ID = "TYdAwMw37xw"

# Function to get comments from the YouTube video
def get_comments(api_key, video_id):
    comments = []
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )

    response = request.execute()

    while response:
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        # Check for next page of comments
        if "nextPageToken" in response:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                pageToken=response["nextPageToken"],
                maxResults=100
            )
            response = request.execute()
        else:
            break

    return comments

# Function to save comments to a CSV file
def save_comments_to_csv(comments, filename):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Comment"])
        for comment in comments:
            writer.writerow([comment])

# Function to perform sentiment analysis on comments
def sentiment_analysis(filename):
    data = pd.read_csv(filename)
    data["Polarity"] = data["Comment"].apply(lambda comment: TextBlob(comment).sentiment.polarity)
    data["Sentiment"] = data["Polarity"].apply(lambda polarity: "Positive" if polarity > 0 else ("Negative" if polarity < 0 else "Neutral"))
    
    # Save results to a new CSV file
    data.to_csv("sentiment_analysis_results.csv", index=False)
    print(data.head())

if __name__ == "__main__":
    # Step 1: Get YouTube comments
    comments = get_comments(API_KEY, VIDEO_ID)
    
    # Step 2: Save comments to CSV
    csv_filename = "youtube_comments.csv"
    save_comments_to_csv(comments, csv_filename)
    
    # Step 3: Perform sentiment analysis
    sentiment_analysis(csv_filename)


# Make sure to also run: python -m textblob.download_corpora for TextBlob to work correctly.