from os import system
names = ["Rahul", "Nishant", "Harry","qwert"]
for name in names:
    

    if (name==names[len(names)-1]):
        system(f" say and lastly Shoutout to {name}")
        break 
    system(f" say Shoutout to {name}")
