# CS6704 Basic Workshop Coding.md
# Partners: Huayu Liang, Hunter Leary

# Method-level comments from Hunter Leary
# Works from Hunter Leary: roman_to_int: converts a string to integer value
# IDE / Text editor Hunter Leary used: VIM

# Method-level comments from Huayu Liang
# Works from Huayu Liang: int_to_roman: converts a integer to string value
# IDE / Text editor Huayu Liang used: Visual Studio Code

import os

def roman_to_int(roman:str) -> int:
    """Converts roman numeral to integer value"""
    convert = roman
    total = 0
    
    for vals in convert:
        if vals.__contains__("I"):
            total += 1
        elif vals.__contains__("V"):
            total += 5
        elif vals.__contains__("X"):
            total += 10
        elif vals.__contains__("L"):
            total += 50
        elif vals.__contains__("C"):
            total += 100
        elif vals.__contains__("D"):
            total += 500
        elif vals.__contains__("M"):
            total += 1000
        else:
            print("Error")
            
    return total

def int_to_roman(num: int) -> str:
        Roman = ""
        storeIntRoman = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        for i in range(len(storeIntRoman)):
            while num >= storeIntRoman[i][0]:
                Roman += storeIntRoman[i][1]
                num -= storeIntRoman[i][0]
        return Roman

def main():
    
    print("Roman value is LVI")
    num_value1 = "LVI"
    integer1 = roman_to_int(num_value1)
    print(f"Integer value is {integer1}")

    print("Roman value is IV")
    num_value2 = "IV"
    integer2 = roman_to_int(num_value2)
    print(f"Integer value is {integer2}")

    print("Numerical value is 5")
    rom_value1 = 5
    roman1 = int_to_roman(rom_value1)
    print(f"Integer value is {roman1}")

    print("Numerical value is 12")
    rom_value2 = 12
    roman2 = int_to_roman(rom_value2)
    print(f"Integer value is {roman2}")
    

main()