import string
k = 'shopper'
m = [i for i in k]
d = {}
viowel = ['a', 'e', 'i', 'o', 'u']
for ind, val in enumerate(string.ascii_lowercase, start=1):
    d[val] = ind
min_values = []
for i in m:
    kr = []
    for j in viowel:
        t = abs(d[i] - d[j])
        kr.append(t)
    min_values.append(min(kr))
print(min_values)
#Write a function that takes in a string and for each character, returns the distance to the nearest vowel. If the character is a vowel itself, return 0
