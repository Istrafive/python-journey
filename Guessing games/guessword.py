from random import choice

def main()->None:
    def g_word_game()->None:
        word_range={'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7,
                    'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
        list_months=list(word_range.keys())
        target_word=choice(list_months)
        month_value=word_range[target_word]
        tries=0
        print("""Welcome to Malcolm's guessing game, in this edition, you must simply guess a random month
            in a year (for example: march), if your guess is correct then the game ends, however if it
            is incorrect then you play until the number of tries you have played have been exceeded the limit
            in this game the months have a number value in accordance to how close they are to the year,
            for example January's value is 1 (it is the first month and hence the closest to the year) and
            November's value is 11, therefore if the month you guess has a value lower than the month
            needed, you will be informed and if the month you guessed has a value greater than the month
            needed, you will also be informed""")
        while tries<3:
            t_guess=input("Guess a random month in a year: ")
            print('\n')
            if t_guess.isdigit():
                print("Do not guess the value of the month, guess the month itself")
                print('\n')
                continue
            else:
                t_guess=t_guess.lower()
                if t_guess in list_months:
                    if t_guess==target_word:
                        print("Congrats! You have guessed the correct word")
                        break
                    if word_range[t_guess]<month_value:
                        print("The value of the month you have guessed is too low, try again")
                        print('\n')
                        tries+=1
                    if word_range[t_guess]>month_value:
                        print("The value of the month you have guessed is too high, try again")
                        print('\n')
                        tries+=1
                else:
                    print("Try guessing a month in the year")
                    print('\n')
                    continue
        if tries==3:
            print("You have failed to guess the correct month in the alloted amount of tries")
    g_word_game()

if __name__=='__main__':
    main()
