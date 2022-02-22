import json, sched, spotipy, time
from spotipy.oauth2 import SpotifyOAuth

def parse_routines():
    routines = open('/routines.json')
    return json.load(routines)

def authenticate():
    scope = "user-read-playback-state user-modify-playback-state"
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, open_browser=False))

def check_track(scheduler, spotify, routines):
    # Get the track and queue
    current_state = spotify.current_playback()
    # Query the routines
    if current_state and current_state['is_playing'] and current_state['item']:
        routine = routines.get(current_state['item']['id'])
        # If a routine exists, execute it.
        if routine:
            exec_routine(spotify, current_state, routine)
    # Reschedule
    scheduler.enter(1, 1, check_track, (scheduler, spotify, routines))

def exec_routine(spotify, current_state, routine):
    progress_ms = current_state['progress_ms']
    if routine['routine_type'] == 'APPEND' and progress_ms < 1000:
        spotify.add_to_queue(routine['append_id'])
    elif routine['routine_type'] == 'SEEK' and                                 \
         progress_ms >= routine.get('seek_start', 0) and                       \
         progress_ms < routine['seek_end']:
        spotify.seek_track(routine['seek_end'])
    elif routine['routine_type'] == 'SKIP' and                                 \
         progress_ms >= routine.get('skip_time', 0):
        spotify.next_track()

if __name__ == '__main__':
    # Setup
    routines = parse_routines()
    spotify = authenticate()
    scheduler = sched.scheduler(time.time, time.sleep)
    # Check the track every second
    scheduler.enter(1, 1, check_track, (scheduler, spotify, routines))
    scheduler.run()