import urllib3
import json
import os
import sched, time
import sys
from IPython.display import clear_output


def clear():
    os.system('cls')
    
s=sched.scheduler(time.time, time.sleep)

trigger=1
counter=1

def fetch(sc):
    global trigger
    global counter
    http = urllib3.PoolManager()
    r3 = http.request('GET', 'https://allsportsapi.com/api/football/?met=Livescore&APIkey=<insert your API key here>')
    results = json.loads(r3.data.decode('utf-8'))
    
    if(len(results)==1):
        print("NO LIVE MATCHES RIGHT NOW !")
        sys.exit()

    clear_output(wait=True)
    os.system('cls')
    print(trigger)
    x=len(results['result'])
    for i in range(0,x):
        if (results['result'][i]['event_live']=="1" and results['result'][i]['event_status']!=""):
            print("MATCH",counter)
            home_team=results['result'][i]['event_home_team']
            away_team=results['result'][i]['event_away_team']
            score=results['result'][i]['event_final_result']
            time=results['result'][i]['event_status']
            venue=results['result'][i]['event_stadium']
            #print("HOME TEAM : ",home_team)
            #print("AWAY TEAM : ",away_team)
            #print("SCORE : ",score)
            #print("TIME : ",time)
            #print("VENUE :", venue)
            print(home_team+' | '+score+' | '+away_team)
            print("STATUS : ", time)
            for z in results['result'][i]['goalscorers']:
                if(z['home_scorer']=="" and z['away_scorer']!=""):
                    away_scorer=z['away_scorer']
                    time_score=z['time']
                    print(time_score+' '+away_scorer+' ( '+ away_team+' ) ')
                elif(z['home_scorer']!="" and z['away_scorer']==""):
                    home_scorer=z['home_scorer']
                    time_score=z['time']
                    print(time_score+' '+home_scorer+' ( '+ home_team+' ) ')
                else:
                    print("Verifying the scorer")
            counter+=1
            print("\n")
    s.enter(1,1,fetch,(sc,))
    trigger+=1
    counter=1
s.enter(1,1,fetch,(s,))
s.run()
