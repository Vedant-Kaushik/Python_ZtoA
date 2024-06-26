def board():
    import random
    avi_pos=['' for i in range (1,18)]
    a=[i for i in range (1,18)]
    print (avi_pos)
    first_pos=a[random.choice(range(1,18))]
    avi_pos[first_pos]=random.choice([2,4])
    a.remove(first_pos)
    second_pos=a[random.choice(range(1,17))]
    avi_pos[second_pos]=random.choice([2,4])
    print(first_pos)
    print(second_pos)
    print(avi_pos)
    print(f'|  { avi_pos[1] }  |  { avi_pos[2] }   |  { avi_pos[3] }   |  { avi_pos[4] }   |')
    print(f'|----|-----|-----|-----|')
    print(f'|  { avi_pos[5] }  |  { avi_pos[6] }   |  { avi_pos[7] }   |  { avi_pos[8] }   |')
    print(f'|----|-----|-----|-----|')
    print(f'|  { avi_pos[9] }  |  { avi_pos[10] }   |  { avi_pos[11] }   |  { avi_pos[12] }   |')
    print(f'|----|-----|-----|-----|')
    print(f'|  { avi_pos[13] }  |  { avi_pos[14] }   |  { avi_pos[15] }   |  { avi_pos[16] }   |')
# board()
# def play():
    inp=input('Enter w a s d depending upon direction of movement = ')
    if(inp == 'w'):
        # i=avi_pos
        if(first_pos!=[1,2,3,4]):
            while True and first_pos>0:
                first_pos= first_pos-4
                if(first_pos-second_pos==4 or second_pos-first_pos==4):
                    b=avi_pos[first_pos]+avi_pos[second_pos]
                    print(b)
board()