import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row["letter"]:row["code"] for (index, row) in df.iterrows()}
#print(nato_dict)

word = input("Enter a word: ").upper() #turn everything upper case
coded_word = [nato_dict[letter] for letter in word]
print(coded_word)