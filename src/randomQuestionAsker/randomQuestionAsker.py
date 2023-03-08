questions = open("input.txt", "a")
import random
def random_line(questions):
  lines = open("input.txt").read().splitlines()
  return random.choice(lines)

randomQuestion = random_line('input.txt')
amguosgn = open("output.txt", "w")
amguosgn.write(randomQuestion + input(randomQuestion))
amguosgn.close()