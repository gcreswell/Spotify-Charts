# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:35:13 2018

@author: garrett
"""

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd

# used to sign into the Spotify API
spotifyID = 
spotifySECRET = 
client_credentials_manager = SpotifyClientCredentials(spotifyID, spotifySECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

""" countries and playlist ID's have to all be done seperately, Spotify's API
 only reads the first 100 songs of a playlist, so consolidating the Top 50's
 to one playlist would unfortunately not be possible"""
country_list = {
        "0" : "Argentina",
        "1" : "Australia",
        "2" : "Austria",
        "3" : "Belgium",
        "4" : "Bolivia",
        "5" : "Brazil",
        "6" : "Bulgaria",
        "7" : "Canada",
        "8" : "Chile",
        "9" : "Colombia",
        "10" : "Costa Rica",
        "11" : "Czech Republic",
        "12" : "Denmark",
        "13" : "Dominican Republic",
        "14" : "Ecuador",
        "15" : "El Salvador",
        "16" : "Estonia",
        "17" : "Finland",
        "18" : "France",
        "19" : "Germany",
        "20" : "Greece",
        "21" : "Guatemala",
        "22" : "Honduras",
        "23" : "Hong Kong",
        "24" : "Hungary",
        "25" : "Iceland",
        "26" : "Indonesia",
        "27" : "Ireland",
        "28" : "Israel",
        "29" : "Italy",
        "30" : "Japan",
        "31" : "Latvia",
        "32" : "Lithuania",
        "33" : "Luxembourg",
        "34" : "Malaysia",
        "35" : "Mexico",
        "36" : "Netherlands",
        "37" : "New Zealand",
        "38" : "Nicaragua",
        "39" : "Norway",
        "40" : "Panama",
        "41" : "Paraguay",
        "42" : "Peru",
        "43" : "Philippines",
        "44" : "Poland",
        "45" : "Portugal",
        "46" : "Romania",
        "47" : "Singapore",
        "48" : "Slovakia",
        "49" : "Spain",
        "50" : "Sweden",
        "51" : "Switzerland",
        "52" : "Taiwan",
        "53" : "Thailand",
        "54" : "Turkey",
        "55" : "United Kingdom",
        "56" : "United States",
        "57" : "Uruguay",
        "58" : "Vietnam" 
        }

# These can be changed by changing the user and playlist ID...Can do any number of playlists
playlist_tracks = {
    "0" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbMMy2roB9myp"),
    "1" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbJPcfkRz0wJ0"),
    "2" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbKNHh6NIXu36"),
    "3" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbJNSeeHswcKB"),
    "4" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbJqfMFK4d691"),
    "5" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbMXbN3EUUhlg"),
    "6" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbNfM2w2mq1B8"),
    "7" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbKj23U1GF4IR"),                    
    "8" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbL0GavIqMTeb"),
    "9" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbOa2lmxNORXQ"),
    "10" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbMZAjGMynsQX"),
    "11" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbIP3c3fqVrJY"),
    "12" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbL3J0k32lWnN"),
    "13" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbKAbrMR8uuf7"),
    "14" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbJlM6nvL1nD1"),
    "15" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbLxoIml4MYkT"),
    "16" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbLesry2Qw2xS"),
    "17" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbMxcczTSoGwZ"),
    "18" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbIPWwFssbupI"),
    "19" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbJiZcmkrIHGU"),                  
    "20" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbJqdarpmTJDL"),
    "21" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbLy5tBFyQvd4"),
    "22" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbJp9wcIM9Eo5"),
    "23" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbLwpL8TjsxOG"),
    "24" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbNHwMxAkvmF8"),
    "25" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbKMzVsSGQ49S"),
    "26" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbObFQZ3JLcXt"),
    "27" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbKM896FDX8L1"),
    "28" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbJ6IpvItkve3"),
    "29" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbIQnj7RRhdSX"),
    "30" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbKXQ4mDTEBXq"),
    "31" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbJWuzDrTxbKS"),
    "32" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbMx56Rdq5lwc"),
    "33" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbKGcyg6TFGx6"),
    "34" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbJlfUljuZExa"),
    "35" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbO3qyFxbkOE1"),
    "36" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbKCF6dqVpDkS"),
    "37" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbM8SIrkERIYl"),
    "38" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbISk8kxnzfCq"),
    "39" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbJfdy5b0KP7W"),
    "40" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbKypXHVwk1f0"),
    "41" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbNOUPGj7tW6T"),
    "42" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbJfdy5b0KP7W"),
    "43" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbNBz9cRCSFkY"),
    "44" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbN6itCcaL3Tt"),
    "45" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbKyJS56d1pgi"),
    "46" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbNZbJ6TZelCq"),
    "47" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbK4gjvS1FjPY"),
    "48" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbKIVTPX9a2Sb"),
    "49" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbNFJfN1Vw8d9"),
    "50" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbLoATJ81JYXz"),
    "51" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbJiyhoAPEfMK"),
    "52" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbMnZEatlMSiu"),
    "53" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbMnz8KIWsvf9"),
    "54" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbIVYVBNw9D5K"),
    "55" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbLnolsZ8PSNw"),
    "56" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbLRQDuF5jeBp"),
    "57" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbMJJi3wgRbAy"),
    "58" : sp.user_playlist_tracks(user="spotifycharts", playlist_id="37i9dQZEVXbLdGSmz6xilI")
}

# These details + track_features will go into a dataframe later on
tids = []
names = []
release = []
popu = []
isExplicit = []
country = []
for tr in playlist_tracks:
    for i, t in enumerate(playlist_tracks[tr]['items']):
        names.append(t['track']['name'])
        popu.append(t['track']['popularity'])
        isExplicit.append(t['track']['explicit'])
        release.append(t['track']["album"]["release_date"])
        tids.append(t['track']['uri'])
        country.append(country_list[tr])
    
#sp.audio_featuers can only do 50 max at a time, so we have to split tids into chunks
chunks =[tids[x:x+50] for x in range(0, len(tids), 50)]
features = []
for i, chunk in enumerate(chunks):
    feat_sublist = sp.audio_features(chunk)
    features.extend(feat_sublist)

# Removes invalid songs (could possibly be music videos in playlists, for example)
nonelist = []
for i, feature in enumerate(features):
    if feature is None:
        nonelist.append(i)
        del(features[i])
        del(names[i])
        del(release[i])
        del(popu[i])
        del(isExplicit[i])
        del(country[i])
        
# creating dataframe and adding the details from before
songs = pd.DataFrame(features)
songs["song_name"] = names
songs["explicit"] = isExplicit
songs["release_date"] = release
songs["popularity"] = popu
songs["country"] = country

#dropping columns that I personally find unnecessary for what I want to do
songs = songs.drop(columns=["analysis_url", "track_href", "type", "uri"])

songs.to_csv("spotify_data.csv")