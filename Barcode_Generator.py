import barcode
from barcode.writer import ImageWriter

filename = input("Please provide a name for your file: ")
number = input("Please enter the number you wish to print a barcode for: ")


def is_eligible(num):
    if len(num) == 13:
        return True
    else:
        return False


while not is_eligible(number):
    print("Invalid input! The number must be exactly 13 digits.")
    number = input("Please enter the number you wish to print a barcode for: ")

ean = barcode.get_barcode_class('ean13')
generated_code = ean(number, writer=ImageWriter())
generated_code.save(filename)
