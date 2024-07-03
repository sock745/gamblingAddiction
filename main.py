LINES = 5
COLUMNS = 5

def gambling101():
  while True:
    moneyInput = input("How much money would you like to gamble away (you're going to lose it)?")
    if moneyInput.isdigit():
      moneyInput = int(moneyInput)
      if moneyInput > 0:
        break
      else: 
        print ("Please enter a positive number")
  else:
    print ("Put in an number please.")

  print(type(moneyInput))
  return gambling101()

def numbaLines():
  while True:
    linesInput = input("How many lines would you like to bet on (1-5)?")
    if linesInput.isdigit():
      lineInput = int(linesInput)
      if  1<= linesInput <= LINES:
        break
      else: 
        print ("Please enter a positive number")
    else:
      print ("Put in an number please.")
   
  return numbaLines()


def main():
  balance = gambling101()
  


gambling101()
