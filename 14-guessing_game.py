number = 9
guess_count = 0
guess_limit = 3 
while guess_count < guess_limit: 
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == number:
        print('You won!')
        break
else: #se o while nao executar o break 
    print ('Sorry you failed')



