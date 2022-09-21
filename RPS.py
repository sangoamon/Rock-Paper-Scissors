dante_turn = input('Choose Dante action: ')
vergil_turn = input('Choose Vergil action: ')

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
