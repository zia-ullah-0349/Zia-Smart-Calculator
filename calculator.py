print( "=== zia ka calculator ===")

while True:
     first_number = input("give a number \n or enter exit to dismissed the program")
    
if first_number == "exit":
    print("program dismissed!")

second_number = int(input("give another number: "))
operation = input("what to do: select any option from 1 to 4; \n 1 for addition, \n 2 for subtraction,\n 3 for multiplication , \n 4 for division \n select your option: ")

print(f"\nResults")

if operation == "1":
      print(f"{first_number} + {second_number} = {first_number + second_number} ")

elif operation == "2":     
      print(f"{first_number} - {second_number} = {first_number - second_number} ")
elif operation == "3":
      print(f"{first_number} * {second_number} = {first_number * second_number}" )
elif operation == "4":
      print(f"{first_number} / {second_number} = {first_number / second_number} ")
else :
      print("invalid input")
      print("please select a correct opyion")