import json, sched, spotipy, time
from spotipy.oauth2 import SpotifyOAuth

def parse_routines():
    routines = open('/routines.json')
    return json.load(routines)

def authenticate():
    scope = "user-modify-playback-state"
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, open_browser=False))

def check_track(scheduler, spotify, routines):
    # Get the track
    # Query the routines
    # Exec the routines
    # Reschedule
    scheduler.enter(60, 1, check_track, (scheduler, spotify, routines))

def get_track():
    return sp.current_user_playing_track()

def exec_routine(sp, routine):
    if(routine['routine_type'] == 'APPEND'):
        sp.add_to_queue(routine['append_id'])
    elif(routine['routine_type'] == 'SEEK'):
        sp.seek_track(routine['seek_end'])
    elif(routine['routine_type'] == 'SKIP'):
        sp.next_track()

if __name__ == '__main__':
    # Setup
    routines = parse_routines()
    spotify = authenticate()
    scheduler = sched.scheduler(time.time, time.sleep)
    # Check the track every second
    scheduler.enter(60, 1, check_track, (scheduler, spotify, routines))
    scheduler.run()