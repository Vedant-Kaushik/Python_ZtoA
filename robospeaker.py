import os
if __name__=='__main__':
    while True:
        x=input('enter text you wanna say = ')
        if x=='q': #q=quit
            os.system('say bye bye')
            break
        command=f'say {x}'
        os.system(command)