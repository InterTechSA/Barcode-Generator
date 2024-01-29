import barcode
from barcode.writer import ImageWriter
import os

filename = input("Please provide name for your file: ")

number = input("Please enter the number you wish to print barcode for: ")

ean = barcode.get_barcode_class('ean13')
generated_code = ean(number, writer=ImageWriter())

generated_code.save(filename)



