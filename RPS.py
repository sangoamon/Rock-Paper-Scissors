import random
actions = ['Rock', 'Paper', 'Scissors']


while(True):
    dante_turn = input('Choose Dante action, or type exit: ')
    vergil_turn = random.choice(actions)

    if dante_turn == 'exit':
        print('Thank you for ... something')
        break

    print(f'Dante:{dante_turn} versus Vergil:{vergil_turn}')
    if dante_turn == vergil_turn:
        print('They are both injured and cant continue the fight')
    elif dante_turn == 'Scissors' and vergil_turn == 'Rock':
        print('Dante defeated Vergil')
    elif dante_turn == 'Rock' and vergil_turn == 'Scissors':
        print('Dante defeated Vergil')
    elif dante_turn == 'Paper' and vergil_turn == 'Rock':
        print('Dante defeated Vergil')
    else:
        print('Saul Goodman 3D')
