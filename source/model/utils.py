import numpy as np
import random
import pandas as pd

def generate_playlist(pd_track, pd_playlist, num_playlist_to_test = 100):
    playlist_choices = random.choices(np.arange(pd_playlist.shape[0]), k = num_playlist_to_test)

    playlist_ids = []

    for playlist_index in playlist_choices:
        a = pd_track[pd_playlist.loc[playlist_index, 'playlist_id'] == pd_track['playlist_id']].shape[0]
        if(a >= 30):
            playlist_ids.append(pd_playlist.loc[playlist_index, 'playlist_id'])
    
    track_ids = {}
    for list_id in playlist_ids:
        track_ids[list_id] = list(pd_track[pd_track['playlist_id'] == list_id]['track_id'])
    return track_ids

def generate_test_playlist(track_ids, missing_rate = 0.2):
    track_id_for_test = {}
    for key in track_ids:
        all_tracks = track_ids[key]
        n = len(all_tracks)
        nums_songs_to_test = int(n * (1 - missing_rate))
        track_id_for_test[key] = all_tracks[:nums_songs_to_test]
    return track_id_for_test

def r_precision(prediction, label):
	prediction = list(set(prediction))
	label = list(set(label))
	score = len(list(set(prediction) & set(label))) / len(label)
	return score

pd_playlist = pd.read_csv('../data/20210824_212829_playlists.tsv', sep='\t')
pd_track = pd.read_csv('../data/20210824_212829_tracks.tsv', sep='\t')

playlist_test = generate_playlist(pd_track, pd_playlist)
# test = generate_test_playlist(playlist_test)
