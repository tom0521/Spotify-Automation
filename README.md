# Spotify-Automation

This script monitors your Spotify activity in order to execute "routines" based on what you are listening to.

The routines.json file contains an example of all routine types. The json is a dictionary of routines where the key is the Spotify track id and the value is the routine in the following formats.

To add a song to the queue when one song is being listened to, follow this example:
```
"0a9sd6MEXZXIPHk0fAxpZ4": {
    "title": "We Will Rock You",
    "artist": "Queen",
    "routine_type": "APPEND",
    "append_id": "4kzvAGJirpZ9ethvKZdJtg"
}
```
This will add 'We Are the Champions' by Queen to the queue if 'We Will Rock You' by Queen is being played. If the queu is empty, one will play after the other as it should be.

To skip a portion of a song, follow this example:
```
"3TO7bbrUKrOSPGRTB5MeCz": {
    "title": "Time",
    "artist": "Pink Floyd",
    "routine_type": "SEEK",
    "seek_start": 0,
    "seek_end": 43000
}
```
This will skip the first 43 second of 'Time' by Pink Floyd. The exact time in the song that all the clock chimes stop. The `seek_start` value is optional and if it is not supplied, the value defaults to 0.

To skip a song, follow this example:
```
"0hKRSZhUGEhKU6aNSPBACZ": {
    "title": "A Day In The Life",
    "artist": "The Beatles",
    "routine_type": "SKIP",
    "skip_time": 300000
}
```
This will skip to the next track once the 5 minute mark of 'A Day In The Life' by The Beatles is reached which is the exact time the song outro begins. The `skip_time` values is optional and will default to 0, meaning the song will be skipped anytime it is played.