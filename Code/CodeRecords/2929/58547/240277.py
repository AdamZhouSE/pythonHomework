def func():
    temp_arr = [int(x) for x in input().split(" ")]
    songs_num = temp_arr[0]
    disk_storage = temp_arr[1]
    songs = []
    i = 0
    while i < songs_num:
        temp_arr = [int(x) for x in input().split(" ")]
        songs.append((temp_arr[0], temp_arr[1], temp_arr[0] - temp_arr[1]))
        i += 1

    songs = sorted(songs, key=lambda x: x[2], reverse=True)

    size_of_songs = 0
    i = 0
    while i < len(songs):
        size_of_songs += songs[i][0]
        i += 1

    if size_of_songs <= disk_storage:
        print(0)
        return

    zipped = 0
    i = 0
    while i < len(songs):
        zipped += 1
        size_of_songs -= songs[i][2]
        if size_of_songs <= disk_storage:
            print(zipped)
            return
        i += 1
        
    print(-1)


func()
