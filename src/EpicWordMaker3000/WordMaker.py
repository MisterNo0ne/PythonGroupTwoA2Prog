import random

list1 = ["Anti-","Un-","Dis-","Im-","Mid-","Mis-","Mal-","Over-","Post-","Co-","Micro-","Extra-","Sub-","Homo-","In-","En-","Pre-","Anti-","Inter-","Sub-"];
list2 = ["-ful","-less","-able","-ic","-al","-sion","-ly","-ish","-ology","-graphy","-s","-ment","-ify","-ism","-ed","-er","-ance","-ship","-tion","-ence"];
list3 = ["circum","counter","multi","cent","ambi","geo","bio","spect","mega","biblio","aqua","script","corp","dict","phobia","hydro","trans","ortho","aud","form"];

howManyWords = input("How many words do you want? \n")

for i in range(int(howManyWords)):
  print(random.choice(list1)+random.choice(list3)+random.choice(list2))