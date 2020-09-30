def main():
  
  # Project-1-Team-Compression
#This is team compression, this is what we did

#define the function with "my_char"
  def findcode(my_char):

    if my_char == "A":
      code = "000000"
    elif my_char == "B":
      code = "000001"
    elif my_char == "C":
      code = "000010"
    elif my_char == "D":
      code = "000011"
    elif my_char == "E":
      code = "000100"
    elif my_char == "F":
      code = "000101"
    elif my_char == "G":
      code = "000110"
    elif my_char == "H":
      code = "000111"
    elif my_char == "I":
      code = "001000"
    elif my_char == "J":
      code = "001001"
    elif my_char == "K":
      code = "001010"
    elif my_char == "L":
      code = "001011"
    elif my_char == "M":
      code = "001100"
    elif my_char == "N":
      code = "001101"
    elif my_char == "O":
      code = "001110"
    elif my_char == "P":
      code = "001111"
    elif my_char == "Q":
      code = "010000"
    elif my_char == "R":
      code = "010001"
    elif my_char == "S":
      code = "010010"
    elif my_char == "T":
      code = "010011"
    elif my_char == "U":
      code = "010100"
    elif my_char == "V":
      code = "010101"
    elif my_char == "W":
      code = "010110"
    elif my_char == "X":
      code = "010111"
    elif my_char == "Y":
      code = "011000"
    elif my_char == "Z":
      code = "011001"
    elif my_char == "'":
      code = "101000"
    elif my_char == "!":
      code = "101001"
    elif my_char == "-":
      code = "101010"
    elif my_char == " \" ":
      code = "101011"
    elif my_char == " \' ":
      code = "101100"


#Open's the text file
my_file = open "Code_File.txt"

#Reading the txt file as a string
my_string = Code_File.read()

#The string is printed
print(len(my_string))

Creates a loop in the program
for i in range(0,len(my_string)):
  val = findcode(my_string[i])
  print(i," " ,my)string[i]," ',val)
  



main()
