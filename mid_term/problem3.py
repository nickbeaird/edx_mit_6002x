

def song_playlist(songs, max_size):
    track_size = 0 
    tracks_list = []
    song_1_tuple = songs[0]
    
    song_1_time = song_1_tuple[2]
    song_1_name = song_1_tuple[0]
    if song_1_time < max_size:
        tracks_list.append(song_1_name)
        track_size += song_1_time
    else:
        return tracks_list
    

    other_songs = songs[1:]
    sorted_other_songs = sorted(other_songs, key=lambda o: o[2])

    for song in sorted_other_songs:
        if song[0] in tracks_list:
            continue
        if track_size + song[2] < max_size:
            tracks_list.append(song[0])
            track_size += song[2]
    
    return tracks_list


if __name__ == '__main__':
    print('testing')
    song_set1 = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]

    song_set2 = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]

    print(song_playlist(song_set1, max_size=12.2))
    print(song_playlist(song_set2, max_size=5))
