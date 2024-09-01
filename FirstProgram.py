#FirstProgram.py
#Name: Reiy
#Date: 9/1/24
#Assignment: Lab 1

def main():
  print("First Program")
  #Say hello
  print ("Hello")
  #Ask for the user's name
  name = input("Please enter your name: ")
  #Use the user's name in the program.
  print("Hi there", name)
  #Ask the user for their age.
  age = input("Please enter your age: ")
  age = int(age) #convert from words to number
  #Tell the user what year they were born in.
  born = 2024 - age 
  #Assume that they have not had their birthday yet this year.
  print("You were born in", born)

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
