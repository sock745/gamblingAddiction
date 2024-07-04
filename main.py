import random

LINES = 5
ROWS = 5
COLUMNS = 5

symbols = {
  "A": 1,
  "B": 3,
  "C": 4,
  "D": 5
}
#symbolValue is the reward multiplier
symbolValue = {
  "A": 5,
  "B": 4,
  "C": 3,
  "D": 1
}

def checkWins(column, lines, bet):
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbolCheck = column[line]
      if symbol != symbolCheck:
        break
    else:
      

def getSpin(rows, cols, symbols):
  allSymbols = []
  for symbol, symbolCount in symbols.items():
    allSymbols.extend([symbol]* symbolCount)
    #for i in range (symbolCount):
      #allSymbols.append(symbol)

  columns = []
  for c in range(cols):
    column = []
    currentSymbols = allSymbols[:]
    for row in range(rows):
      value = random.choice(allSymbols)
      column.append(value)
    columns.append(column)
  return columns

def slotMachine(columns):
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i != len(columns) - 1:
        print(column[row], " | ", end= " ")
      else:
        print(column[row], end = "")
    print()
    
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

  return moneyInput

def numbaLines():
  while True:
    lineInput = input("How many lines would you like to bet on (1-5)?")
    if lineInput.isdigit():
      lineInput = int(lineInput)
      if  1<= lineInput <= LINES:
        break
      else: 
        print ("Amount must be between 1 and 5")
    else:
      print ("Put in an number please.")
   
  return lineInput

def betNumba():
  while True:
    moneyInput = input("How much money would you like to bet?")
    if moneyInput.isdigit():
      moneyInput = int(moneyInput)
      if 0<= moneyInput <= 100:
        break
      else: 
        print ("You can only gamble between 0 and 100")
    else:
      print ("Put in an number please.")

  print(type(moneyInput))
  return moneyInput
  
def main():
  balance = gambling101()
  line = numbaLines()
  while True:
    bet = betNumba()
    betTotal = bet *line
    if betTotal > balance:
      print (f"You are a brokie, your current balance is ${balance}")
    else:
      break
  print (f"You're betting ${bet} on {line} lines. Your total bet is ${betTotal}")
  slots = getSpin(ROWS, COLUMNS, symbols)
  slotMachine(slots)

main()

