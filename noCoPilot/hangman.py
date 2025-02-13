# I want to try using a for else statment 
# I also want to use a match statemtn 
#
import random 
words_easy = ['BOLD', 'FAST', 'JUMP', 'KIND', 'LUSH', 'MAZE', 'NEST', 'POND', 'RUST', 'VINE']
words_medium = ['BLAST', 'CRISP', 'DWELL', 'FLARE', 'GRASP', 'HATCH', 'JOLLY', 'PLUMB', 'SHOCK', 'TWIST']
words_hard = ['BRIGHT', 'CANDLE', 'DETOUR', 'FIERCE', 'GROOVE', 'HUMBLE', 'JUMPER', 'MINGLE', 'RHYTHM', 'STRIKE']

cur_words = None
word_used = None 
word_dict = {}
template = []
guessed = set()
mistake = 0

def main (): 
    global cur_words
    while True:

        while True: 
            diffuculty = input("Choose your diffuculty! \nEasy (E)\nMedium (M)\nHard (H) ")
            
            match diffuculty: 
                case 'E' | 'e' | 'Easy':
                    print("Should be a breeze")
                    cur_words = words_easy
                    word()
                    break
                case 'M' | 'm' | 'Medium':
                    print("Good Luck!")
                    cur_words = words_medium
                    word()
                    break
                case 'H' | 'h' | 'Hard':
                    print("This won't be easy! ")
                    cur_words= words_hard
                    word()
                    break
                case _:
                    print("Your input is not an option")
        
        while True: 
            if mistake==6:
                again = input("You lost!\nWant to paly again? (y/n)")
                if again == 'y':
                    play_again()
                    break 
                else: 
                    print("Goodbye! ")

            elif "_" not in template:
                again = input("You WON!\nWant to paly again? (y/n)")
                if again == 'y':
                    play_again()
                    break 
                else: 
                    print("Goodbye! ")


            start(mistake)
            tmp = ' '.join(template)
            print(tmp)
            print(f" guessed: {list(guessed)} lives: {6 - mistake}/6")

            guess = input("Guess a letter").upper()
            if len(guess) == 1 and ord(guess) > 64 and ord(guess) < 91:
                if guess not in guessed: 
                    make_guess(guess)
                else:
                    print("Already guessed that letter, try again!")

            else:
                print("Not a letter try again! ")

def play_again():
    global cur_words
    global word_used 
    global word_dict 
    global template 
    global guessed
    global mistake
    cur_words = None
    word_used = None 
    word_dict = {}
    template = ()
    guessed = set()
    mistake = 0
  
def word(): 
    global template
    global word_used
    word_used = random.choice(cur_words)
    for i in range(len(word_used)):
        template.append('_')

    for i in range(len(word_used)):
        if word_used[i] in word_dict:
            tmp_list = [word_dict[word_used[i]]]
            word_dict[word_used[i]] = tmp_list.append(i)
        else: 
            word_dict[word_used[i]] = i


def make_guess(letter): 
    global mistake 
    if letter in word_dict.keys(): 
        tmp_list = [word_dict[letter]]
        for index in tmp_list:
            template[index]=letter
    else:
        print("Incorrect")
        mistake += 1
    guessed.add(letter)
    
    
def start(mistakes): 
    match mistakes: 
        case 0: 
            print(figure(" ", " ", " ", " ", " ", " "))
        case 1:
            print(figure("O", "", " ", " ", " ", " "))
        case 2:
            print(figure("O", "|", " ", " ", " ", " "))
        case 3:
            print(figure("O", "|", "/", " ", " ", " "))
        case 4:
            print(figure("O", "|", "/", "\\", " ", " "))
        case 5:
            print(figure("O", "|", "/", "\\", "/", " "))
        case 6:
            print(figure("O", "|", "/", "\\", "/", "\\"))


def figure(a, b, c, d, e, f):
    return(f"  |-----\n  |    {a}\n  |    {b}{c}{d}\n  |   {e}{f}\n  |\n-----------")


main()