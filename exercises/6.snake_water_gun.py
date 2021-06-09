import random as r

def judge(user,computer):
    
    if (user =='s' and computer=='w') or( user=='w' and computer=='g') or (user=='g' and computer =='s'):
        return 'user'
    elif (user=='s' and computer=='g') or (user =='w' and computer=='s') or (user=='g' and computer=='w'):
        return 'computer'

    else:
        return 0


print("""Welcome to the snake water gun game
1.There will be 10 rounds and who has the more points will win.
2.Each round is worth 1 point.""")


li=['s','g','w']


cnt_u,cnt_c=0,0

for i in range(10):
    us=input('enter your choice :\n')
    cs=r.choice(li)
    us=us.lower()

    answer = judge(us,cs)

    if answer=='user':
        print('you won this round')
        cnt_u+=1
    elif answer =='computer':
        print('you loose this round')
        cnt_c+=1
    else:
        print('it is a tie')

if cnt_c < cnt_u:
    print('Congrats you are the winner with score : ',f'{cnt_u}-{cnt_c}')
elif cnt_c>cnt_u:
    print('better luck next time, your score was : ',f'{cnt_u}-{cnt_c}')
else:
    print('wow it is a tie',5,"-",5)
