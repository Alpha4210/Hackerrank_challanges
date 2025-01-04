def minion_game(string):
    vowels = "AEIOU"
    kevin_scores = stuart_scores = 0
    length = len(string)

    # Counting the number of substrings and assigning the values
    for i in range(length):
        if string[i] in vowels:
            kevin_scores += length - i
        else:
            stuart_scores += length - i
    # Declaring the winner of the game
    if stuart_scores > kevin_scores:
        print(f'Stuart {stuart_scores}')
    elif stuart_scores < kevin_scores:
        print(f'Kevin {kevin_scores}')
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)