import os

import google_auth_oauthlib.flow

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
    result = ['Amorphis, Light My Fire (The Doors)', 'Anthrax, Carry on Wayward Son (Kansas)', 'Armored Saint, Saturday Night Special (Lynyrd Skynyrd)', 'Between the Buried and Me, Bicycle Race (Queen)', 'Black Sabbath, Evil Woman (Crow)', 'Blessthefall, Dream On (Aerosmith)', 'Body Count, Hey Joe (Billy Roberts)', 'Carnivore, Manic Depression (Jimi Hendrix)', 'Celtic Frost, Heroes (David Bowie)', 'Children of Bodom, Somebody Put Something in My Drink (Ramones)', 'Cirith Ungol, Fire (The Crazy World of Arthur Brown)', 'Crowbar, No Quarter (Led Zeppelin)', 'Dark Angel, Immigrant Song (Led Zeppelin)', 'Death, God of Thunder (KISS)', 'Destruction, My Sharona (The Knack)', 'Disturbed, The Sound of Silence (Simon and Garfunkel)', 'Dream Theater, Funeral for a Friend (Elton John)', 'Exodus, Low Rider (War)', 'Flotsam and Jetsam, Saturday Night’s Alright for Fighting (Elton John)', 'Fu Manchu, Godzilla (Blue Oyster Cult)', 'Ghost, Here Comes the Sun (The Beatles)', 'Guns N’ Roses, Knocking on Heaven’s Door (Bob Dylan)', 'GWAR, School’s Out (Alice Cooper)', 'Helloween, White Room (Cream)', 'HIM, (Don’t Fear) The Reaper (Blue Oyster Cult)', 'Iron Maiden, Cross-Eyed Mary (Jethro Tull)', 'Judas Priest, Green Manalishi (Fleetwood Mac)', 'Machine Head, Message in a Bottle (The Police)', 'Mastodon, Just Got Paid (ZZ Top)', 'Megadeth, No More Mr. Nice Guy (Alice Cooper)', 'Melvins, Goin’ Blind (KISS)', 'Metal Church, Highway Star (Deep Purple)', 'Metallica, Turn the Page (Bob Seger)', 'Monster Magnet, Brainstorm (Hawkwind)', 'Motley Crue, Smokin’ in the Boys Room (Brownsville Station)', 'Motorhead, Heroes (David Bowie)', 'Nightwish, High Hopes (Pink Floyd)', 'Overkill, Deuce (KISS)', 'Ozzy Osbourne, 21st Century Schizoid Man (King Crimson)', 'Primal Fear, Speed King (Deep Purple)', 'Queensryche, Welcome to the Machine (Pink Floyd)', 'Quiet Riot, Cum on Feel the Noize (Slade)', 'Riot, Born to Be Wild (Steppenwolf)', 'Rob Zombie/Marilyn Manson, Helter Skelter (The Beatles)', 'Sanctuary, White Rabbit (Jefferson Airplane)', 'Shadows Fall, Welcome to the Machine (Pink Floyd)', 'Slayer, In a Gadda Da Vida (Iron Butterfly)', 'Sodom, Surfin’ Bird (The Trashmen)', 'Testament, Nobody’s Fault (Aerosmith)', 'Trouble', 'Twisted Sister, It’s Only Rock and Roll (Rolling Stones)', 'Type O Negative, Cinnamon Girl (Neil Young)', 'Various Artists (Ronnie James Dio, Yngwie Malmsteen, Stu Hamm, Paul Taylor & Gregg Bisonette), Dream On (Aerosmith)', 'Voivod, Astronomy Domine (Pink Floyd)', 'W.A.S.P., The Real Me (The Who)']
    playlist_id = playlist_creator.create_playlist(name, credentials)
    for song in result:
        video_id = video_finder.find_video(song)
        playlist_insert.add_video(playlist_id, video_id, credentials)

        print("{} {} added to {}".format(song, video_id, playlist_id))


if __name__ == "__main__":
    main(url="https://loudwire.com/metal-covers-classic-rock-songs/")
