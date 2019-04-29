# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import googleapiclient.discovery
import googleapiclient.errors


def add_video(playlist, video, credentials):
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.playlistItems().insert(
        part="snippet",
        body={
          "snippet": {
            "playlistId": playlist,
            "position": 0,
            "resourceId": {
              "kind": "youtube#video",
              "videoId": video
            }
          }
        }
    )
    request.execute()