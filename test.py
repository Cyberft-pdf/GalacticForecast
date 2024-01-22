def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s[2:].isalnum():
        return False
    if s[-1] == "0":
        return False
    if any(char in ". ,;:'\"/\\!@#$%^&*()-_=+[]{}<>?" for char in s):
        return False

    return True

main()

