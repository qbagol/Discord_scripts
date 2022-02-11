from datetime import datetime
import pyautogui as pa
import requests
import time
import sys

def ButtonDetect(button_png_file, game_name):
    coordinates=pa.locateCenterOnScreen(button_png_file)
    pa.moveTo(coordinates.x, coordinates.y)
    pa.click(coordinates.x, coordinates.y)
    print('Game Automaticly Accepted')
    return game_name  
    
def AutoGameAccept():
    games = (('lol-accept.png', 'League of Legends'), ('cs-accept.png', 'Counter-Strike Global Offensive'))
    running_time=0
    status=True
 
    while status:
        for i in range(len(games)):
            try:
                game_id=ButtonDetect(games[i][0], games[i][1])
                status=False
                break;

            except OSError:
                print('Wrong button file, check if it is a PNG and make sure the file name is correct')
                break;

            except AttributeError:
                if running_time%5==0:
                    info= 'Running - no match ' + '     '
                else:
                    info= 'Running - no match ' + '.'*(running_time%5)
                sys.stdout.write('%s\r' % info)
                running_time += 1
                time.sleep(0.5) 
    return game_id

def Discord_bot_push():
    
    url='<CHANNEL ID>'

    payload = {
        'content' : 'Game has been accepted automatically      '+ f'            game id:  {game_id} '+ '                                                        action id: '+ str(datetime.now())
    }
       
    header = {
        'authorization' : '<BOT DISCORD ACCOUNT AUTHORIZATION ID>'
    }

    r=requests.post(url, data=payload, headers=header)

game_id = AutoGameAccept()
Discord_bot_push()