import datetime as dt
import requests
import numpy as np
import pandas as pd




def scrape_travel_durations(api_key)
    first_time = dt.datetime(2021,8,22,0,0).timestamp()
    last_time = dt.datetime(2021,8,29,0,0).timestamp()
    timestamp = np.arange(first_time, last_time, 15*60)
    duration = np.zeros(timestamp.shape, dtype=int)
    day = np.zeros(timestamp.shape, dtype=int)
    hour = np.zeros(timestamp.shape)

    for k in range(timestamps.size):
        # log time information
        current_timestamp = timestamp[k]
        day[k] = int(dt.datetime.fromtimestamp(current_timestamp).day - 22)
        hour[k] = dt.datetime.fromtimestamp(current_timestamp).hour \
                  + dt.datetime.fromtimestamp(current_timestamp).minute/60
        
        # request travel duration from gmaps api
        request_string = 'https://maps.googleapis.com/maps/api/distancematrix'\
                         '/json?units=imperial&origins=37.872204,-122.266141&'\
                         'destinations=37.768152,-122.390961&departure_time='\
                         + str(int(current_timestamp)) + '&key=' + api_key
        r = requests.get(request_string)
        
        # log duration information
        duration[k] = int(r.json()['rows'][0]['elements'][0]\
                          ['duration_in_traffic']['text'][0:2])
    
    # put data together into a dataframe
    travel_duration_df = pd.DataFrame(np.array([day, hour, duration].T),
                                      columns=['day', 'hour', 'duration'])
    
    return travel_duration_df