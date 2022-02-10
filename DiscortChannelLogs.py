from datetime import datetime
import requests
import json
import pandas

def Discord_bot_get():
    
    channel_id='<>'
    key='<>'
    
    now = datetime.now()
    time = now.strftime("%H.%M.%S")
   
    url=f'https://discord.com/api/v9/channels/{channel_id}/messages'

    header = {
        'authorization' : f'{key}'
    }

    get_response=requests.get(url, headers=header)
    load_response=json.loads(get_response.text)
    df = pandas.DataFrame(columns=['user','message','time'])
    
    for i in range(len(load_response)):
        df = df.append({'user':load_response[i]['author']['username'], 'message':load_response[i]['content'], 'time':load_response[i]['timestamp']}, ignore_index=True)
    
    df.to_csv(f'discord_logs_channel_{channel_id}_time_{time}.csv')
    
Discord_bot_get()