def calculate(number):
    sum = 0
    for i in range(len(number)):
        sum += (i+1)*int(number[i])
    return sum%11

def solve_missing(number, checksum):
    sum = 0
    missing = 0
    if checksum == "X":
        checksum = 10
    else:
        checksum = int(checksum)
    
    for i in range(len(number)):
        if number[i] != "x":
            sum += (i+1)*int(number[i])
        else:
            missing = i
    return int((checksum - sum%11)/(missing+1))

if int(input("Isbn with one missing value (0) or a regular isbn without the checksum (1)? ")) == 1:
    num = input("Enter isbn: ")
    print(f"The checksum is: {calculate(num)}")
else:
    num = input("Enter isbn with x: ")
    checksum = input("Enter checksum: ")
    print(f"The missing number is: {solve_missing(num, checksum)}")
