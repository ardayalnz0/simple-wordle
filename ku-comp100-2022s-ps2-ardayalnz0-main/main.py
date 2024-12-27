import csv

guess_word_list = ['aback', 'abaft', 'abbey', 'aboon', 'abort', 'about', 'above', 'abuse', 'abyss',  'aches',
             'acids', 'acnes', 'actor', 'acute', 'adapt', 'adder', 'adios', 'admin', 'admit', 'adobe', 'adopt', 'adore',
             'adown', 'adult', 'afoot', 'afore', 'afoul', 'after', 'again', 'agape', 'agent', 'agile', 'aging', 'agone', 'agree', 'ahead', 'ahold', 'ahull', 'aided', 'aisle', 'alarm', 'album', 'alert', 'algae',
             'align', 'alike', 'aline', 'alive', 'allow', 'aloft', 'alone', 'along', 'aloof', 'aloud', 'alter', 'amaze',
             'amiss', 'among', 'amply', 'amuck', 'amuse', 'angel', 'anger', 'angle', 'angry', 'annoy', 'apace', 'apart',
             'apple', 'apply', 'aptly', 'arear', 'argon', 'argue', 'arise', 'arrow', 'arson', 'aside', 'askew',
             'audio', 'audit', 'avoid', 'await', 'awake', 'award', 'aware', 'awful', 'azote', 'azure', 'bacon',
             'badge', 'badly', 'bagel', 'baker', 'bally', 'baron', 'based', 'basic', 'basil', 'basin', 'basis', 'batch',
             'beach', 'beady', 'beams', 'beans', 'beard', 'beast', 'began', 'begin', 'begun', 'beige', 'being', 'bells',
             'below', 'belts', 'bench', 'berry', 'bezel', 'bible', 'biker', 'birth', 'bison', 'black', 'blade', 'blame',
             'blaze', 'blend', 'blind', 'bliss', 'block', 'blood', 'blues', 'bluff', 'blume', 'blunt', 'blush', 'board',
             'bogey', 'bound', 'boxer', 'brain', 'brake', 'brave', 'bravo', 'bread', 'break', 'breed', 'brick',
             'brief', 'bring', 'broad', 'broom', 'brown', 'brush', 'build', 'bulky', 'bunny', 'burst', 'busty', 'buyer',
             'buzzy', 'bytes', 'cabal', 'cajun', 'camel', 'canal', 'candy', 'canny', 'capri', 'cargo', 'carry', 'catch',
             'cause', 'chain', 'chair', 'cheap', 'check', 'chest', 'chief', 'child', 'china', 'circa', 'civil', 'claim',
             'class', 'clean', 'clear', 'climb', 'clock', 'close', 'coach', 'coast', 'count', 'court', 'cover', 'coyly',
             'crazy', 'cream', 'crime', 'cross', 'crowd', 'crown', 'cycle', 'daily', 'dance', 'death', 'depth', 'dimly',
             'dirty', 'ditto', 'doubt', 'draft', 'drama', 'dream', 'dress', 'drily', 'drink', 'drive', 'dryly', 'dully',
             'early', 'earth', 'empty', 'enemy', 'enjoy', 'enter', 'entry', 'equal', 'error', 'event', 'exact', 'exist',
             'extra', 'faint', 'faith', 'false', 'fatly', 'fault', 'feyly', 'field', 'fifth', 'fight', 'final', 'first',
             'fitly', 'floor', 'focus', 'force', 'forte', 'forth', 'frame', 'frank', 'fresh', 'front', 'fruit', 'fully',
             'funny', 'furth', 'gaily', 'gayly', 'giant', 'glass', 'godly', 'grand', 'grant', 'grass', 'great', 'green',
             'gross', 'group', 'guess', 'guide', 'haply', 'happy', 'harsh', 'heart', 'heavy', 'hence', 'henry',
             'horse', 'hotel', 'hotly', 'house', 'human', 'icily', 'ideal', 'image', 'imply', 'index', 'infra', 'inner',
             'input', 'issue', 'japan', 'joint', 'jolly', 'jones', 'judge', 'knife', 'large', 'laugh',
             'laura', 'laxly', 'layer', 'learn', 'leave', 'legal', 'lento', 'level', 'lewis', 'light', 'limit',
             'local', 'loose', 'lowly', 'lucky', 'lunch', 'madly', 'magic', 'major', 'march', 'marry', 'match', 'maybe',
             'metal', 'minor', 'minus', 'model', 'money', 'month', 'moral', 'motor', 'mouth', 'music', 'naked', 'nasty',
             'naval', 'neath', 'never', 'newly', 'night', 'nobly', 'noise', 'north', 'novel', 'nurse', 'occur', 'oddly',
             'offer', 'often', 'order', 'other', 'ought', 'outer', 'owner', 'panel', 'paper', 'party', 'peace', 'peter',
             'phase', 'phone', 'piano', 'piece', 'pilot', 'pitch', 'place', 'plain', 'plane', 'plant', 'plate', 'plonk',
             'plumb', 'point', 'pound', 'power', 'press', 'price', 'pride', 'prime', 'prior', 'prize', 'proof', 'proud',
             'prove', 'queen', 'queer', 'quick', 'quiet', 'quite', 'radio', 'raise', 'ramen', 'range', 'rapid', 'ratio',
             'reach', 'ready', 'redly', 'refer', 'relax', 'reply', 'right', 'river', 'roman', 'rough', 'round', 'route',
             'royal', 'rugby', 'rural', 'sadly', 'scale', 'scene', 'scope', 'score', 'sense', 'serve',
             'shall', 'shape', 'share', 'sharp', 'sheep', 'sheer', 'sheet', 'shift', 'shily', 'shirt', 'shock', 'shoot',
             'short', 'shyly', 'sight', 'silly', 'since', 'sixth', 'skill', 'slash', 'sleek', 'sleep', 'slyly',
             'small', 'smart', 'smile', 'smith', 'smoke', 'solid', 'solve', 'sorry', 'sound', 'south', 'space',
             'spang', 'spare', 'speak', 'speed', 'spend', 'spite', 'split', 'sport', 'squad', 'staff', 'stage',
             'stand', 'stark', 'start', 'state', 'steam', 'steel', 'steep', 'stick', 'still', 'stock', 'stone', 'store',
             'stour', 'study', 'stuff', 'style', 'sugar', 'super', 'sweet', 'table', 'tally', 'tanto', 'taste', 'teach',
             'terry', 'thank', 'theme', 'there', 'thick', 'thing', 'think', 'third', 'throw', 'tight', 'title', 'today',
             'total', 'touch', 'tough', 'tower', 'track', 'trade', 'train', 'treat', 'trend', 'trial', 'truly',
             'trust', 'truth', 'twice', 'uncle', 'under', 'union', 'unity', 'until', 'upper', 'upset', 'urban', 'usual',
             'utter', 'vague', 'valid', 'value', 'verry', 'video', 'visit', 'vital', 'voice', 'wanly', 'waste', 'watch',
             'water', 'wetly', 'where', 'while', 'white', 'whole', 'woman', 'world', 'worry', 'would', 'write', 'wrong',
             'young', 'youth']

valid_word_list = []
with open('valid-words.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        valid_word_list += row







from words import guess_word_list, valid_word_list
import random


print("=== W O R D L E ===")
print(f"Cached {len(guess_word_list)} guess words.")
mode = int(input('Select a mode, Enter (1) for Debug Mode, (2) for Test Mode: '))

trial = 5

def selectedword():
    '''
    selects a word from the word list
    '''
    selected_word = guess_word_list[word]
    return selected_word

def is_valid(w):
    '''
    decides whether the entered word by the user is valid or not
    '''
    if len(entered_word) == 5:
        if entered_word.lower() in valid_word_list:
            return True
        else:
            return False
    else:
        return False


def is_equal(w):
    '''
    Colours the letters
    '''
    if is_valid(entered_word) == True:
        if selectedword()[w].lower() == entered_word[w].lower():
            letter = entered_word[w]
            return f"\033[92m{letter}\033[0m"
        elif selectedword()[w].lower() != entered_word[w].lower():
            for a in range(0, 5):
                if entered_word[w].lower() == entered_word[a].lower():
                    letter = entered_word[w]
                    if w > a:
                        if is_equal(a) == (f"\033[33m{letter}\033[0m"):
                            return (f'{letter}')
                    '''If a letter repeats in the entered word, only colour the one on the left to yellow. 
                    Valid only if the letter is not in the correct position but is in the selected word'''
            for i in range(0, 5):
                if entered_word[w].lower() == selectedword()[i]:
                    if i != w:
                        if entered_word[w].lower() != entered_word[i].lower():
                            letter = entered_word[w]
                            return (f"\033[33m{letter}\033[0m")
                    elif i != w and entered_word[w].lower() == entered_word[i].lower():
                        letter = entered_word[w]
                        return (f'{letter}')
                    '''If a letter has turned green and it repeats, don't turn the one in the wrong position
                    into yellow'''

            else:
                letter = entered_word[w]
                return (f'{letter}')



def is_equal_ew1(w):
    '''
    Colours the letters
    '''
    if is_valid(input_list[0]) == True:
        if selectedword()[w].lower() == input_list[0][w].lower():
            letter = input_list[0][w]
            return f"\033[92m{letter}\033[0m"
        elif selectedword()[w].lower() != input_list[0][w].lower():
            for a in range(0, 5):
                if input_list[0][w].lower() == input_list[0][a].lower():
                    letter = input_list[0][w]
                    if w > a:
                        if is_equal_ew1(a) == (f"\033[33m{letter}\033[0m"):
                            return (f'{letter}')
                    '''If a letter repeats in the entered word, only colour the one on the left to yellow. 
                    Valid only if the letter is not in the correct position but is in the selected word'''
            for i in range(0, 5):
                if input_list[0][w].lower() == selectedword()[i]:
                    if i != w:
                        if input_list[0][w].lower() != input_list[0][i].lower():
                            letter = input_list[0][w]
                            return (f"\033[33m{letter}\033[0m")
                    elif i != w and input_list[0][w].lower() == input_list[0][i].lower():
                        letter = input_list[0][w]
                        return (f'{letter}')
                    '''If a letter has turned green and it repeats, don't turn the one in the wrong position
                    into yellow'''
            else:
                letter = input_list[0][w]
                return (f'{letter}')



def is_equal_ew2(w):
    '''
    Colours the letters
    '''
    if is_valid(input_list[1]) == True:
        if selectedword()[w].lower() == input_list[1][w].lower():
            letter = input_list[1][w]
            return f"\033[92m{letter}\033[0m"
        elif selectedword()[w].lower() != input_list[1][w].lower():
            for a in range(0, 5):
                if input_list[1][w].lower() == input_list[1][a].lower():
                    letter = input_list[1][w]
                    if w > a:
                        if is_equal_ew2(a) == (f"\033[33m{letter}\033[0m"):
                            return (f'{letter}')
                    '''If a letter repeats in the entered word, only colour the one on the left to yellow. 
                    Valid only if the letter is not in the correct position but is in the selected word'''
            for i in range(0, 5):
                if input_list[1][w].lower() == selectedword()[i]:
                    if i != w:
                        if input_list[1][w].lower() != input_list[1][i].lower():
                            letter = input_list[1][w]
                            return (f"\033[33m{letter}\033[0m")
                    elif i != w and input_list[1][w].lower() == input_list[1][i].lower():
                        letter = input_list[1][w]
                        return (f'{letter}')
                    '''If a letter has turned green and it repeats, don't turn the one in the wrong position
                    into yellow'''
            else:
                letter = input_list[1][w]
                return (f'{letter}')


def is_equal_ew3(w):
    '''
    Colours the letters
    '''
    if is_valid(input_list[2]) == True:
        if selectedword()[w].lower() == input_list[2][w].lower():
            letter = input_list[2][w]
            return f"\033[92m{letter}\033[0m"
        elif selectedword()[w].lower() != input_list[2][w].lower():
            for a in range(0, 5):
                if input_list[2][w].lower() == input_list[2][a].lower():
                    letter = input_list[2][w]
                    if w > a:
                        if is_equal_ew3(a) == (f"\033[33m{letter}\033[0m"):
                            return (f'{letter}')
                    '''If a letter repeats in the entered word, only colour the one on the left to yellow. 
                    Valid only if the letter is not in the correct position but is in the selected word'''
            for i in range(0, 5):
                if input_list[2][w].lower() == selectedword()[i]:
                    if i != w:
                        if input_list[2][w].lower() != input_list[2][i].lower():
                            letter = input_list[2][w]
                            return (f"\033[33m{letter}\033[0m")
                    elif i != w and input_list[2][w].lower() == input_list[2][i].lower():
                        letter = input_list[2][w]
                        return (f'{letter}')
                    '''If a letter has turned green and it repeats, don't turn the one in the wrong position
                    into yellow'''
            else:
                letter = input_list[2][w]
                return (f'{letter}')


def is_equal_ew4(w):
    '''
    Colours the letters
    '''
    if is_valid(input_list[3]) == True:
        if selectedword()[w].lower() == input_list[3][w].lower():
            letter = input_list[3][w]
            return f"\033[92m{letter}\033[0m"
        elif selectedword()[w].lower() != input_list[3][w].lower():
            for a in range(0, 5):
                if input_list[3][w].lower() == input_list[3][a].lower():
                    letter = input_list[3][w]
                    if w > a:
                        if is_equal_ew4(a) == (f"\033[33m{letter}\033[0m"):
                            return (f'{letter}')
                    '''If a letter repeats in the entered word, only colour the one on the left to yellow. 
                    Valid only if the letter is not in the correct position but is in the selected word'''
            for i in range(0, 5):
                if input_list[3][w].lower() == selectedword()[i]:
                    if i != w:
                        if input_list[3][w].lower() != input_list[3][i].lower():
                            letter = input_list[3][w]
                            return (f"\033[33m{letter}\033[0m")
                    elif i != w and input_list[3][w].lower() == input_list[3][i].lower():
                        letter = input_list[3][w]
                        return (f'{letter}')
                    '''If a letter has turned green and it repeats, don't turn the one in the wrong position
                    into yellow'''
            else:
                letter = input_list[3][w]
                return (f'{letter}')

input_list = []

if mode == 1:
    word = int(input('Enter an index in between 0-548: '))
    print(f'The selected word is {selectedword()}')
    notfound = True
    while notfound:
        entered_word = input('Enter a word: ')
        if is_valid(entered_word):
            input_list.append(entered_word)
        if selectedword() == entered_word:
            if trial == 5:
                print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')
            if trial == 4:
                print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')
            if trial == 3:
                print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                print(f'{is_equal_ew2(0)} {is_equal_ew2(1)} {is_equal_ew2(2)} {is_equal_ew2(3)} {is_equal_ew2(4)}')
                print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')

            if trial == 2:
                print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                print(f'{is_equal_ew2(0)} {is_equal_ew2(1)} {is_equal_ew2(2)} {is_equal_ew2(3)} {is_equal_ew2(4)}')
                print(f'{is_equal_ew3(0)} {is_equal_ew3(1)} {is_equal_ew3(2)} {is_equal_ew3(3)} {is_equal_ew3(4)}')
                print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')

            if trial == 1:
                print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                print(f'{is_equal_ew2(0)} {is_equal_ew2(1)} {is_equal_ew2(2)} {is_equal_ew2(3)} {is_equal_ew2(4)}')
                print(f'{is_equal_ew3(0)} {is_equal_ew3(1)} {is_equal_ew3(2)} {is_equal_ew3(3)} {is_equal_ew3(4)}')
                print(f'{is_equal_ew4(0)} {is_equal_ew4(1)} {is_equal_ew4(2)} {is_equal_ew4(3)} {is_equal_ew4(4)}')
                print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')



            for slot in range(1, trial):
                print('- - - - -')
            notfound = False
        else:
            if is_valid(entered_word) == False:
                if len(entered_word) != 5:
                    print('Word length should be 5.')
                elif entered_word not in valid_word_list:
                    print(f'Word {entered_word} is not found in the list.')
            else:
                trial -= 1
                if trial == 4:
                    print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')
                if trial == 3:
                    print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                    print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')
                if trial == 2:
                    print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                    print(f'{is_equal_ew2(0)} {is_equal_ew2(1)} {is_equal_ew2(2)} {is_equal_ew2(3)} {is_equal_ew2(4)}')
                    print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')

                if trial == 1:
                    print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                    print(f'{is_equal_ew2(0)} {is_equal_ew2(1)} {is_equal_ew2(2)} {is_equal_ew2(3)} {is_equal_ew2(4)}')
                    print(f'{is_equal_ew3(0)} {is_equal_ew3(1)} {is_equal_ew3(2)} {is_equal_ew3(3)} {is_equal_ew3(4)}')
                    print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')

                if trial == 0:
                    print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                    print(f'{is_equal_ew2(0)} {is_equal_ew2(1)} {is_equal_ew2(2)} {is_equal_ew2(3)} {is_equal_ew2(4)}')
                    print(f'{is_equal_ew3(0)} {is_equal_ew3(1)} {is_equal_ew3(2)} {is_equal_ew3(3)} {is_equal_ew3(4)}')
                    print(f'{is_equal_ew4(0)} {is_equal_ew4(1)} {is_equal_ew4(2)} {is_equal_ew4(3)} {is_equal_ew4(4)}')
                    print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')
                    print(f'The word was {selectedword()}')
                    notfound = False


                for slot in range(1, trial + 1):
                    print('- - - - -')



 


elif mode == 2:
    word = random.randint(0,548)
    selectedword()
    notfound = True
    while notfound:
        entered_word = input('Enter a word: ')
        if is_valid(entered_word):
            input_list.append(entered_word)
        if selectedword() == entered_word:
            if trial == 5:
                print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')
            if trial == 4:
                print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')
            if trial == 3:
                print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                print(f'{is_equal_ew2(0)} {is_equal_ew2(1)} {is_equal_ew2(2)} {is_equal_ew2(3)} {is_equal_ew2(4)}')
                print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')

            if trial == 2:
                print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                print(f'{is_equal_ew2(0)} {is_equal_ew2(1)} {is_equal_ew2(2)} {is_equal_ew2(3)} {is_equal_ew2(4)}')
                print(f'{is_equal_ew3(0)} {is_equal_ew3(1)} {is_equal_ew3(2)} {is_equal_ew3(3)} {is_equal_ew3(4)}')
                print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')

            if trial == 1:
                print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                print(f'{is_equal_ew2(0)} {is_equal_ew2(1)} {is_equal_ew2(2)} {is_equal_ew2(3)} {is_equal_ew2(4)}')
                print(f'{is_equal_ew3(0)} {is_equal_ew3(1)} {is_equal_ew3(2)} {is_equal_ew3(3)} {is_equal_ew3(4)}')
                print(f'{is_equal_ew4(0)} {is_equal_ew4(1)} {is_equal_ew4(2)} {is_equal_ew4(3)} {is_equal_ew4(4)}')
                print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')

            for slot in range(1, trial):
                print('- - - - -')
            notfound = False
        else:
            if is_valid(entered_word) == False:
                if len(entered_word) != 5:
                    print('Word length should be 5.')
                elif entered_word not in valid_word_list:
                    print(f'Word {entered_word} is not found in the list.')
            else:
                trial -= 1
                if trial == 4:
                    print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')
                if trial == 3:
                    print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                    print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')
                if trial == 2:
                    print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                    print(f'{is_equal_ew2(0)} {is_equal_ew2(1)} {is_equal_ew2(2)} {is_equal_ew2(3)} {is_equal_ew2(4)}')
                    print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')

                if trial == 1:
                    print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                    print(f'{is_equal_ew2(0)} {is_equal_ew2(1)} {is_equal_ew2(2)} {is_equal_ew2(3)} {is_equal_ew2(4)}')
                    print(f'{is_equal_ew3(0)} {is_equal_ew3(1)} {is_equal_ew3(2)} {is_equal_ew3(3)} {is_equal_ew3(4)}')
                    print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')

                if trial == 0:
                    print(f'{is_equal_ew1(0)} {is_equal_ew1(1)} {is_equal_ew1(2)} {is_equal_ew1(3)} {is_equal_ew1(4)}')
                    print(f'{is_equal_ew2(0)} {is_equal_ew2(1)} {is_equal_ew2(2)} {is_equal_ew2(3)} {is_equal_ew2(4)}')
                    print(f'{is_equal_ew3(0)} {is_equal_ew3(1)} {is_equal_ew3(2)} {is_equal_ew3(3)} {is_equal_ew3(4)}')
                    print(f'{is_equal_ew4(0)} {is_equal_ew4(1)} {is_equal_ew4(2)} {is_equal_ew4(3)} {is_equal_ew4(4)}')
                    print(f'{is_equal(0)} {is_equal(1)} {is_equal(2)} {is_equal(3)} {is_equal(4)}')
                    print(f'The word was {selectedword()}')
                    notfound = False

                for slot in range(1, trial + 1):
                    print('- - - - -')
