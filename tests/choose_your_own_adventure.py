name = input('Type your name :')

print(f'Welcome {name} to this adventure')


answer = input('You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ').lower()


if answer== 'left':
    answer = ('You came to a river, type swin to swin across or walk to walk around it: ').lower()
    if answer== 'swin':
        print('You swin acrros and were eaten by an alliagator')
    elif answer == 'walk':
        print('You walked out for many miles, ran out of water and you lost the game.')

    else:
        print('Not a valid option. You lose')

elif answer=='right':
    answer = ('You came to a bridge, it looks wobbly, type cross to croos it or back to head back: ').lower()
    if answer == 'back':
        print('You go back and lose.')
    elif answer == 'cross':
        print('You win')
    else:
        print('Not a valid option. You lose')

else:
    print('Not a valid option. You lose')