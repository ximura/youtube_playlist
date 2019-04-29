import os

import google_auth_oauthlib.flow

import extractor
import playlist_creator
import playlist_insert
import video_finder

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def main(url):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    client_secrets_file = "secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()

    name = '55 Awesome Metal Covers of Classic Rock Songs'
    result = extractor.extract(url)
    playlist_id = playlist_creator.create_playlist(name, credentials)
    for song in result:
        video_id = video_finder.find_video(song)
        playlist_insert.add_video(playlist_id, video_id, credentials)

        print("{} {} added to {}".format(song, video_id, playlist_id))


if __name__ == "__main__":
    main(url="https://loudwire.com/metal-covers-classic-rock-songs/")
