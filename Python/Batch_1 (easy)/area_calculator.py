# Write code below 💖

import math

print("Welcome to the Area Calculator, Please select a shape to calculate for its Area")
area_calculator = int(input("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n\nSo, What will it be? "))

while True:
  if area_calculator == 1:
    uom = input("Unit of Measurement: ") #for desired unit of measurement
    height = float(input(f"Height in {uom}: "))
    base = float(input(f"Base in {uom}: "))
    area = (height * base)/2
    print(f"The Area of The Triangle is {area} {uom}")
    choose = input("Would you like to keep going or use a different area calculator? (keep going or different)\nPrompt Here: ")
    if choose == "keep going":
      area_calculator == 1
    else:
      area_calculator = int(input("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n\nSo, What will it be? "))


  elif area_calculator == 2:
    uom = input("Unit of Measurement: ") 
    length = float(input(f"Length in {uom}: "))
    width = float(input(f"Width i {uom}: "))
    area = length * width
    print(f"The Area of The Rectangle is {area} {uom}")
    choose = input("Would you like to keep going or use a different area calculator? (keep going or different)\nPrompt Here: ")
    if choose == "keep going":
      area_calculator == 1
    else:
      area_calculator = int(input("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n\nSo, What will it be? "))

  elif area_calculator == 3:
    uom = input("Unit of Measurement: ")
    side = float(input(f"Side Length in {uom}: "))
    area = side**2
    print(f"The Area of The Square is {area} {uom}")
    choose = input("Would you like to keep going or use a different area calculator? (keep going or different)\nPrompt Here: ")
    if choose == "keep going":
      area_calculator == 1
    else:
      area_calculator = int(input("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n\nSo, What will it be? "))

  elif area_calculator == 4:
    uom = input("Unit of Measurements: ")
    radius = float(input("Radius: "))
    area = (math.pi * (radius ** 2))
    print(f"The Area of The Circle is {area} {uom}")
    choose = input("Would you like to keep going or use a different area calculator? (keep going or different)\nPrompt Here: ")
    if choose == "keep going":
      area_calculator == 1
    else:
      area_calculator = int(input("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n\nSo, What will it be? "))

  elif area_calculator == 5:
    print("Thank you for using the area calculator!")
    break 
  else:
    print("I'm sorry, what?\nPlease pick again!")
    area_calculator = int(input("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n\nSo, What will it be? "))
