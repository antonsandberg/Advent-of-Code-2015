import re


def bad_phrases(word):
    if any(item in word for item in disallowed_strings):
        return False
    return True


def three_vowels(word):
    vowels = 'aeiou'
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    if count >= 3:
        return True
    else:
        return False


def double_letter(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False


def double_letter_between(word):
    if re.search(r'(.).\1', word):
        return True
    else:
        return False


def double_pair(word):
    if re.search(r'(.)(.).*\1\2', word):
        return True
    else:
        return False


with open('input.txt') as f:
    data = f.read().strip().split()

disallowed_strings = ['ab', 'cd', 'pq', 'xy']
n_of_words = len(data)
good_words = 0
for word in data:
#    if bad_phrases(word):
#        continue
    if double_letter_between(word) and double_pair(word):
        good_words += 1

print(good_words)



