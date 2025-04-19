#THIS IS A UTILITY FUNCTION SCRIPT
def CheckIfItIsNumerical(num):
    while True:
        raw = input(num)
        if raw.strip().isdigit():
            return int(raw)
        print("That wasn't a number. Please enter a valid number! (e.g 3)")