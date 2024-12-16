from googleapiclient.discovery import build
import pandas as pd

api_key = your_api_key

# ID of the desired channel (can be found under page source)
channel_ids = ["UCIsz3XD8_E1ebhE4YScWeJg"
               # more channels
               ]

# from youtube API documentation
api_service_name = "youtube"
api_version = "v3"

# Get credentials and create an API client
youtube = build(
    api_service_name, api_version, developerKey=api_key)



# function to retrieve channel stas
def get_channel_stats(youtube, channel_ids):

    all_data = []

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=".".join(channel_ids)
    )
    response = request.execute()

    for item in response["items"]:
        data = {"channelName": item["snippet"]["title"],
                "subscribers": item["statistics"]["subscriberCount"],
                "views": item["statistics"]["viewCount"],
                "totalVideos": item["statistics"]["videoCount"],
                "playlistId": item["contentDetails"]["relatedPlaylists"]["uploads"]
                }
        
        all_data.append(data)

    return all_data

channel_stats = get_channel_stats(youtube, channel_ids)

for items in channel_stats:
    if "playlistId" in items:
        playlist_id = items["playlistId"]
    else:
        print("PlaylistID does not exist")


# function to retrieve all id's of the videos of a channel
def get_video_ids(youtube, playlist_id):

        video_ids = []

        request = youtube.playlistItems().list(
                part="snippet,contentDetails",
                playlistId=playlist_id,
                maxResults = 50
        )
        response = request.execute()

        for item in response["items"]:
                video_ids.append(item["contentDetails"]["videoId"])

        next_page_token = response.get("nextPageToken")

        while next_page_token is not None:
                request = youtube.playlistItems().list(
                        part="contentDetails",
                        playlistId=playlist_id,
                        maxResults = 50,
                        pageToken = next_page_token
                )
                response = request.execute()

                for item in response["items"]:
                        video_ids.append(item["contentDetails"]["videoId"])

                next_page_token = response.get("nextPageToken")

        return video_ids

video_ids = get_video_ids(youtube, playlist_id)


# retrieve top10 comments of a video (only top10 due to youtube API restriction)
def get_comments_in_videos(youtube, video_ids):

    all_comments = []

    for video_id in video_ids:
        try:
            request = youtube.commentThreads().list(
                part="snippet,replies",
                videoId=video_id

            )
            response = request.execute()

            comments_in_video = [comment["snippet"]["topLevelComment"]["snippet"]["textOriginal"] for comment in response["items"][0:10]]
            comments_in_video_info = {"video_id": video_id, "comments": comments_in_video}

            all_comments.append(comments_in_video_info)
        
        except HttpError as e:
            error_reason = e.error_details[0]["reason"]
            if error_reason == "commentsDisabled":
                print(f"Comments are disabled for video ID: {video_id}")
            else:
                print(f"An error occurred for video ID: {video_id}: {e}")

    return all_comments

comments = get_comments_in_videos(youtube, video_ids)
print(comments)

