import time
import random


def guess(chances, num):
    for guessesTaken in range(chances):
        a = eval(input('Entring your number: '))
        if a < num:
            print('Too small,You got %d chances left!' % (chances - 1 - guessesTaken))
            continue
        elif a > num:
            print('Too big,You got %d chances left!' % (chances - 1 - guessesTaken))
            continue
        else:
            return True
    return False


print('Hello!May I know your name?')
name = input()
print('Well, ' + name + ' ,I\'m thinking a number,can you guess it?')
time.sleep(1)
print('It\'s between 1 and 100')
time.sleep(1)
print('Do you want the hard mode? Y/N')
while True:
    grade = input('')
    if grade == 'Y':
        Chances = 5
        break
    elif grade == 'N':
        Chances = 10
        break
    else:
        print('Please entry Y or N,it means yes or no')
print('You\'ve got %d chances' % Chances)

number = random.randint(1, 100)
if guess(Chances, number):
    print('You win')
else:
    print('Sorry ' + name + ' ,but you lose!')
