import numpy as np
import random
import pandas as pd


def generate_playlist(pd_track, pd_playlist, num_playlist_to_test=100,threshold=30):
    playlist_sampled = pd_playlist[pd_playlist["playlist_num_tracks"] >= threshold]
    playlist_selected = playlist_sampled["playlist_id"].sample(n=num_playlist_to_test,random_state=0)
    track_ids = {}
    for list_id in playlist_selected:
        track_ids[list_id] = list(pd_track[pd_track['playlist_id'] == list_id]['track_id'])
    return track_ids

# TODO: refactor with df.sample
def generate_test_playlist(track_ids, missing_rate=0.2):
    track_id_for_test = {}
    for key in track_ids:
        all_tracks = track_ids[key]
        n = len(all_tracks)
        nums_songs_to_test = int(n * (1 - missing_rate))
        track_id_for_test[key] = all_tracks[:nums_songs_to_test]
    return track_id_for_test


def r_precision(prediction, label):
    """
    Calculate r-precision: union(p,l)/size
    :rtype: r-precision score
    """
    prediction = list(set(prediction))
    label = list(set(label))
    try:
        score = len(list(set(prediction) & set(label))) / len(label)
    except Exception:
        print(f"division by zero prediction: {prediction}, label: {label}, len(label): {len(label)}")
    return score


pd_playlist = pd.read_csv('../data/20210824_212829_playlists.tsv', sep='\t')
pd_track = pd.read_csv('../data/20210824_212829_tracks.tsv', sep='\t')

playlist_test = generate_playlist(pd_track, pd_playlist)
# test = generate_test_playlist(playlist_test)
