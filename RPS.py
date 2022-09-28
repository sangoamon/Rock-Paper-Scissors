import random
actions = ['Rock', 'Paper', 'Scissors']
dante_turns = []
vergil_turns = []

while(True):
    dante_turn = input('Choose Dante action, or type exit: ')
    vergil_turn = random.choice(actions)

    if dante_turn == 'exit':
        print('Thank you for ... something')
        break
    
    dante_turns.append(dante_turn)
    vergil_turns.append(vergil_turn)


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
    
print(f'You have played {len(dante_turns)} times')
print(dante_turns)
print(vergil_turns)
