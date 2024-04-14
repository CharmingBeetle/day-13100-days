print("***GRADE CALCULATOR***")
print()
#Name of Test
test = input("Name of Test: ")
print()
#Max Points
max = int (input("Maximum possible points: "))
#Score received
score = int (input("Score recieved: "))
print()
numberScore = float((score / max))
pc = numberScore * 100
pc = round(pc, 2)
print()

if  pc <= 100 and pc >= 90:
  print("You got", pc,"%, which is an A+")
elif pc <= 89 and pc >= 80:
  print("You got", pc, "%, which is an A")
elif pc <= 79 and pc >= 70:
  print("You got", pc, "%, which is a B")
elif pc <= 69 and pc >= 60:
  print("You got", pc, "%, which is a C")
elif pc <= 59 and pc >= 50:
  print("You got", pc, "%, which is a D")
elif pc <= 49:
  print("You got", pc, "%, which is a U")
else: 
  print("Try again!")

