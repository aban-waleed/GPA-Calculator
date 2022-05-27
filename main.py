import time
import math
import subprocess
from itertools import cycle
from time import sleep
##################################################

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.WARNING + bcolors.BOLD + "GPA Calculator - by Noor & Aban                                  \n\n" + bcolors.ENDC)
###################################################

def letterGrade():
  numOfClasses = 0
  grade = 0
  condition = 0
  sum = 0

  numOfClasses = int(input('\nHow many classes do you have? '))

  for values in range(1,numOfClasses +1):
    grade = (input(f"\n\nGrade for the class {values}?  ").lower())

    if grade != 'a' and grade != 'b' and grade!= 'c' and grade!= 'd' and grade!= 'f':
      condition = 1
      time.sleep(1.5)
      break
    else:
      if grade == 'a':
        grade = 4
      if grade == 'b':
        grade = 3
      if grade == 'c':
        grade = 2
      if grade == 'd':
        grade = 1
      if grade == 'f':
        grade = 0
      sum = sum + grade
  if condition == 0:
    print (f"\n\nYour GPA is: {sum / numOfClasses}")
  else:
    print(bcolors.FAIL + "\n\n[ERROR] PROGRAM TERMINATING")

def numberGrade():
  sum = 0
  decimal  = 0
  decimalSum = 0

  numOfClasses = int(input('\nHow many classes do you have? '))

  for values in range(1,numOfClasses +1):
   grade = int(input(f"\n\nGrade for the class {values}? %"))

   if grade >= 90:
    decimal = 4
   elif grade >= 80:
    decimal = 3
   elif grade >=70:
    decimal = 2
   elif grade > 60:
    decimal = 1
   else:
    decimal = 0

   decimalSum = decimalSum + decimal 
   sum = sum + grade
  if optionCondition == 1:
    print(f'\n\nYour Average Grade is: %{sum /numOfClasses}')
  if optionCondition == 2:
    print(f"\n\nYour decimal GPA is: {decimalSum / numOfClasses}")
 
optionCondition = 0
optionCondition = int(input (bcolors.OKGREEN + "[1] to input letter grades\n[2] to input numbers\n\n"))
if optionCondition == 1:
  letterGrade()
if optionCondition == 2:
  optionCondition = int(input(bcolors.OKGREEN + "\n[1] to output percentage GPA\n[2] to output decimal GPA\n\n"))
  numberGrade()
