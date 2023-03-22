import random

#these tables are lists of lists that have the morphemes and definitions
prefixTable = [
  ["Anti-", "not/against "],
  ["Un-", "not/no "],
  ["Dis-", "not/no "],
  ["Im-", "not/no "],
  ["Mid-", "the middle of "],
  ["Mis-", "badly/wrongly "],
  ["Mal-", "not/no "],
  ["Over-", "over "],
  ["Post-", "after "],
  ["Co-", "together "],
  ["Micro-", "small/slight "],
  ["Extra-", "beyond "],
  ["Sub-", "under/less than "],
  ["Homo-", "same "],
  ["In-", "in/on/not "],
  ["En-", "being within "],
  ["Pre-", "before "],
  ["Ante-", "before "],
  ["Inter-", "between "],
  ["Semi-", "half "]]

suffixTable = [
  ["-ful", "Full of "],
  ["-less", "Without "],
  ["-able", "Capable of "],
  ["-ic", "Of or pertaining to "],
  ["-al", "Of or pertaining to "],
  ["-sion", "The state of "],
  ["-ly", "Similar to "],
  ["-ish", "Having the characteristics of "],
  ["-ology", "The study of "],
  ["-graphy", "Writing or representation of "],
  ["-s", "Multiple of "],
  ["-ment", "A product of "],
  ["-ify", "To become "],
  ["-ism", "Principle or theory of "],
  ["-ed", "Past participle of "],
  ["-er", "Adjective that describes "],
  ["-ance", "The action of process of "],
  ["-ship", "The condition of "],
  ["-tion", "A state of "],
  ["-ence", "A state of "]]

rootTable = [
  ["circum", "around."],
  ["counter", "being opposite or against."],
  ["multi", "many."],
  ["cent", "one hundred."],
  ["ambi", "both/around."],
  ["geo", "earth."],
  ["bio", "life."],
  ["spect", "look/looking."],
  ["mega", "large."],
  ["biblio", "relating to books."],
  ["hydro", "aquatic."],
  ["script", "write/writings."],
  ["corp", "body."],
  ["dict", "say/sayings."],
  ["phobia", "fear."],
  ["aqua", "aquatic."],
  ["trans", "across/through."],
  ["ortho", "straight."],
  ["aud", "hear/hearing."],
  ["form", "shape."]]

#asks user of how many words they want
howManyWordsSTR = input("How many words do you want? \n")

#makes howManyWordsSTR into an int, and then bounds it at 100
howManyWordsINT = int(howManyWordsSTR)
if (howManyWordsINT > 50):
  howManyWordsINT = 50

#loops over how many words the user asked for
for i in range(howManyWordsINT):
  #picks a pair from each of the tables
  prefixPair = random.choice(prefixTable)
  rootPair = random.choice(rootTable)
  suffixPair = random.choice(suffixTable)
  #prints the funny epic gamer word and definition
  print(prefixPair[0] + rootPair[0] + suffixPair[0])
  print("-- " + suffixPair[1] + prefixPair[1] + rootPair[1] + "\n")

print("hi mr kapptie :)")