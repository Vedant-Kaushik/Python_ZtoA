import time
from plyer import notification  
# from playsound import playsound 
# frequency = 2000
# duration = 1500

for i in range(0,3600):
    
    time.sleep(5)
    # playsound.Beep(frequency, duration)
    notification_title = 'Time for Water'  
    notification_message = f'{i} reminder to drink water'
  
    notification.notify(  
        title = notification_title,  
        message = notification_message,  
        app_icon = None,  
        timeout = 3,  
        toast = False  
    )  

    
