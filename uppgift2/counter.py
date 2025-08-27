from collections import Counter

most_common_numbers = Counter([1, 5, 6, 5, 3, 1, 2, 5]).most_common(2)
print(most_common_numbers)
# -> [(5, 3), (1, 2)]

most_common_letters = Counter("abcbadfbcb").most_common(3)
print(most_common_letters)
# -> [('b', 4), ('a', 2), ('c', 2)]