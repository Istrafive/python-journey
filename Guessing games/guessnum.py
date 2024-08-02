import random

def main() -> None:
    def g_game_num()->None:
        num_tries=0
        logged_num=random.randint(1,100)
        print(f"""Welcome to Malcolm's guess number code, you are to guess a number between 1 and 100 (inclusive)
            if the number you guess is larger than the number that is needed, you will get a print message
            saying: The number is too large, try again" and if the number needed is too small
            you will get a print message saying: The number is too small, try again""")
        print()
        while num_tries<5:
            guessed_num=input("Guess a random number from 1-1000(inclusive) ")
            if not guessed_num.isdigit():
                print("Try using a number this time")
            else:
                guessed_num=int(guessed_num)
                if guessed_num<1:
                    print("Number too small, remember the range starts at 1")
                    continue
                if guessed_num>100:
                    print("Number too large, remember the range ends at 100")
                    continue
                if guessed_num==logged_num:
                    print("You have correctly guessed the number, well done!")
                    break
                if guessed_num<logged_num:
                    print(f"The number {guessed_num} is too small, try again")
                    print()
                    num_tries+=1
                    continue
                if guessed_num>logged_num:
                    print(f"The number {guessed_num} is too large, try again")
                    print()
                    num_tries+=1
                    continue
    g_game_num()

if __name__=='__main__':
    main()