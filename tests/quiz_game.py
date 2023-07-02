def lower(name):
    return name.lower()

print('Welcome to my computer quiz!')

playing = input('Do you want to play?')


if lower(playing) != 'yes':
    quit()

print("Okay! Let's play:)")
score=0
answer = input('What does CPU stand for? ')
if lower(answer) == 'central processing unit':
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
    
    
answer = input('What does GPU stand for? ')
if lower(answer) == 'graphic processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
answer = input('What does RAM stand for? ')
if lower(answer) == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does PSU stand for? ')
if lower(answer) == 'power supply unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


print(f'You got {str(score)} questions correct.')
print(f'You got {str(score/4*100)}%.')