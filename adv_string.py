#Advanced Strings

my_name = "Adithya"

print(my_name[0])
print(my_name[-1])

sentence = "This is a Sentence."
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, \"give me all your money\""
print(quote)


too_much_space = "                   hello"
print(too_much_space.strip())


print("A" in "Apple")

letter = "A"
word = "Apple"
print (letter.lower() in word.lower())


movie = "Hangover"
print("My favorite movie is {}.".format(movie))

