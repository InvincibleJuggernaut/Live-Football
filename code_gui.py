from tkinter import *
import urllib3
import json

window =Tk()
window.title("Live Score")
window.geometry('500x500')
window.configure(bg="black")

#scrollbar=Scrollbar(window)
#scrollbar.pack(side=RIGHT, fill=Y)


lb1=Label(window, text="LIVE MATCHES", bg="#282828", fg="white", font=("Roboto", 30), padx=10, pady=10)
lb1.config(anchor=CENTER)
lb1.pack()

def refresh():
    http = urllib3.PoolManager()
    r3 = http.request('GET', 'https://allsportsapi.com/api/football/?met=Livescore&APIkey=<insert your API key here>')
    results = json.loads(r3.data.decode('utf-8'))
    
    counter=1
    x=len(results['result'])
    for i in range(0,x):
        if (results['result'][i]['event_live']=="1"):
            
            home_team=results['result'][i]['event_home_team']
            away_team=results['result'][i]['event_away_team']
            score=results['result'][i]['event_final_result']
            time=results['result'][i]['event_status']
            venue=results['result'][i]['event_stadium']
            result =(home_team+' '+score+' '+away_team)
            lb2=Label(window, text=result, bg="black", fg="white")
            lb3=Label(window, text=time, bg="black", fg="white")
            lb2.pack(ipadx=5, pady=(35,5))
            lb3.pack(ipadx=5, pady=(5, 15))
            counter+=1
        lb2.after(1000, lb2.destroy)
        lb3.after(1000, lb3.destroy)
    window.after(1000, refresh)

window.after(0, refresh)  
window.mainloop()

    


