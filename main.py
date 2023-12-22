central = input("central letter, e.g., l: ")
letters = set(input("six outer letters, e.g. vitroc: "))
letters.add(central)

# read wordlist
# must be 4 letters long and have central in it, and have only "letters"
words = []
with open("wordlist.txt","r") as file:
    print("\n".join(sorted(
                    [word for word in file.read().split("\n") if len(word)>3 and # must have 4+ letters
                            central in word and # must contain the central letter
                            len(set(word) - letters)==0 # all letters in word must appear in letters
                            ], key=len # sort matching words by length
                    ))
         )
