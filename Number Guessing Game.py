#number guessing game
from random import randrange

def hidden_number():


    random_generated_numer = randrange(1,1000)

    str_random_number = str(random_generated_numer)

    r_g_n_len = len(str_random_number)

    hint_count = 0

    print("\nWELCOME TO NUMBR GUESSING GAME....\n")

    start_game = input("Wanna play ? (Y or N : ")


    print(f'HINT - 1 : ITS A NUMBER WITH {r_g_n_len} CHARACTERS')

    user_guess1 = int(input("\nGuess The Number : "))


    while True:

        if user_guess1 == random_generated_numer:

            print("CONGRATULATIONS YOU WON !....")
            break

        else:

            if r_g_n_len == hint_count + 1:
                print(f'your loose Hidden number is {random_generated_numer}')
                break

            else:

                if hint_count == 0:
                    print(f'WRONG : HINT - 2 : FIST NUMBER IS {str_random_number[0]}')

                elif hint_count == 1:
                    print(f'WRONG : Hint - 3 FISRT 2 NUMBERS ARE {str_random_number[0:-1]}')

                elif hint_count == 2:
                    print(f'WRONG : HINT - 4 : SECOND NUMBER IS {str_random_number[0:-1]}')



            user_guess2 = int(input("\nGuess The Number Again: "))
            user_guess1 = user_guess2
            hint_count += 1


    game_end_question = input("\nWant To play again ? 'Y OR N' : ")

    if game_end_question == "Y":
        hidden_number()

    else:
        print("\nTHANK YOU HAVE A NICE DAY...")



hidden_number()