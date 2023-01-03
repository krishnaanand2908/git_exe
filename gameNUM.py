import GuessGameV8_
import fontstyle as fnt
import os


os.system('cls')


while True:
    try:
        challange = int(input(fnt.apply("Enter the upper limit of the GuessGame:  ", 'purple/bold')))
        GuessGameV8_.guess_game_v5(challange)
    except:
        continue
    
    
    
    choice = input(fnt.apply('Press Enter to contine else quite: ', 'blue/bold'))
    if choice == '':
        print('/n'*25)
        continue
    else:
        break