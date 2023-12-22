central = input("central letter: ")
letters = set(input("six outer letters, separated by spaces: ").split())
letters.add(central)

# read wordlist
# must be 4 letters long and have central in it, and have only "letters"
words = []
with open("wordlist.txt","r") as file:
    words = [word.strip() for word in file.readlines()]

words = [word for word in words if len(word)>3 and 
        central in word and
        len(set(word) - letters)==0
        ]

print("\n".join(sorted(words, key=len)))
