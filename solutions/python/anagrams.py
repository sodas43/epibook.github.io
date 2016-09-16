# Anagrams.cpp 69dab7578339012270872ba200cfff02f59ce894
import random
import string
import collections


# @include
def find_anagrams(dictionary):
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        # Sorts the string, uses it as a key, and then appends
        # the original string as another value into hash table.
        sorted_str = ''.join(sorted(s))
        sorted_string_to_anagrams[sorted_str].append(s)

    anagram_groups = [group for group in sorted_string_to_anagrams.values()
                      if len(group) >= 2]
    return anagram_groups
# @exclude


def rand_string(length):
    ret = (random.choice(string.ascii_lowercase) for i in range(length))
    return ''.join(ret)


def small_test():
    D = ['debit card',     'bad credit', 'the morse code',
         'here come dots', 'the eyes',   'they see',
         'THL']
    result = find_anagrams(D)
    # 3 nontrivial groups:
    # ['debit card', 'bad credit'],
    # ['the morse code', 'here come dots']
    # ['the eyes',     'they see']
    # Since the string 'THL' has no anagrams in D, the result
    # contains 3 entries
    assert len(result) == 3


def main():
    small_test()
    n = random.randint(0, 99999)
    table = {rand_string(random.randint(1, 12)) for i in range(n)}
    dictionary = list(table)
    find_anagrams(dictionary)


if __name__ == '__main__':
    main()