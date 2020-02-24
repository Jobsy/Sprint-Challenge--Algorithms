'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


# def count_th(word, counting=0):

#     # TBC
#     # first pass
#     # check if the first word is t and the second is h
#     # if they are, increase counter by 1
#     # else iterate and continue
#     # new_word = list(word)
#     # counter = 0
#     # for i in range(len(new_word) - 1):
#     #     if new_word[i] == "t" and new_word[i+1] == "h":
#     #         counter += 1
#     #     else:
#     #         next
#     # print(counter)
#     # print(new_word)
#     # return counter

#     # second pass
#     # convert first pass to recursive function
#     # counter = 0
#     n = len(list(word))
#     if n <= 1:
#         return 0
#     else:
#         if word[-n] == "t" and word[-n+1] == "h":
#             print("yes")

#             def counter():
#                 nonlocal counting
#                 # counting = 0
#                 counting += 1
#             counter()
#         count_th(word[-n+1:], counting)

#     # print(counter, "counter1111")
#     print(counting)
#     return counting


def count_th(word):

    if len(word) < 2:
        return 0

    # if the first two letters == 'th'
    elif word[0:2] == 'th':
        # Recursively check the first 2 letters
        return count_th(word[1:]) + 1
    else:
        # else return
        return count_th(word[1:])
