#MadLib.py
#Name: Reiy
#Date: 9/1/24
#Assignment: Lab 1

def main():
  print("Madlib")
  #Ask user for words
  noun = input("Enter a noun: ")
  adjective = input("Enter an adjective: ")
  feeling = input("Enter a feeling: ")
  bodypart = input("Enter a bodypart: ")
  verb1 = input("Enter a verb: ")
  verb2 = input("Enter another verb: ")
  #Print the story with the user supplied words.
  print("Today, I go to " +noun+ " class. It is very " +adjective+ ". I start to get " +feeling+ ". My " +bodypart+ " gets tired. After class, I start to " +verb1+ ". Time to " +verb2+ "!")



#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
