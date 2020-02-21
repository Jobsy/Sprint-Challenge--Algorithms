'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC
    # first pass
    # check if the first word is t and the second is h
    # if they are, increase counter by 1
    # else iterate and continue
    new_word = list(word)
    counter = 0
    for i in range(len(new_word) - 1):
        if new_word[i] == "t" and new_word[i+1] == "h":
            counter += 1
        else:
            next
    print(counter)
    print(new_word)
    return counter
