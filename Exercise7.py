import os
files=os.listdir('problem7')
n=1
format=input('enter the format to be chaged png or pdf = ')
for file in files:
    
    if(format=='png'):
        if file.endswith('.png'):
            os.rename(f'problem7/{file}',f'problem7/{n}.png')
            n=n+1
    elif(format=='pdf'):
        if file.endswith('.pdf'):
            os.rename(f'problem7/{file}',f'problem7/{n}.pdf')
            n=n+1
    else:
        print('Unsupported Format')