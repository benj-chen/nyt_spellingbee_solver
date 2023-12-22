central = input("central letter: ")
outer = input("six outer letters, separated by spaces: ").split()

# read wordlist
words = []
with open("wordlist.txt","r") as file:
    words = [word.strip() for word in file.readlines()]

# find all words, then sort by length of word

# must be 4 letters or longer
ok_words = []
for word in words:
    if len(word)<4:
        continue
    if central not in word:
        continue
    ok = True
    for letter in word: # there must be a more elegant way to do this.
        if letter not in [central]+outer:
            ok = False
            break
    if ok:
        ok_words.append(word)

print("\n".join(sorted(ok_words,reverse=True, key=len)))
