##!/bin/python3

import copy
import collections


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny',
    'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots',
    'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    if len(start_word) == len(end_word) and len(start_word) == 5:
        if start_word == end_word:
            return [start_word]
        with open(dictionary_file, 'r') as f:
            text = f.read()
        dictionary = text.split()
        ladder = []
        ladder.append(start_word)
        queue = collections.deque()
        queue.append(ladder)
        if start_word == end_word:
            return start_word
        while queue:
            current_ladder = queue.popleft()
            for word in list(dictionary):
                if _adjacent(current_ladder[-1], word):
                    dictionary.remove(word)
                    if word == end_word:
                        current_ladder.append(word)
                        return current_ladder
                    ladder_copy = copy.copy(current_ladder)
                    ladder_copy.append(word)
                    queue.append(ladder_copy)
    else:
        return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    current_ladder = ladder
    if not ladder:
        return not True
    for i in range(1, len(current_ladder)):
        if _adjacent(current_ladder[i - 1], current_ladder[i]) is False:
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return None
    dif = 0
    for i, (c1, c2) in enumerate(zip(word1, word2)):
        if dif == 2:
            return False
        elif c1 != c2:
            dif += 1
    return dif == 1
