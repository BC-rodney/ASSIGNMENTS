numbers = {
"0": "zero",
"1": "one",
"2": "two",
"3": "three",
"4": "four",
"5": "five",
"6": "six",
"7": "seven",
"8": "eight",
"9": "nine"
}
 
user_input = input("ENTER NUMBER: ")

out_put = ""
for digit in user_input:

    out_put += numbers.get(digit,"!") + " "
    f"output\t"

print(out_put)
  
#while user_input < 10:
#print(numbers[User_input])
    #break
