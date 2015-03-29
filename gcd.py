import math
import sys

first_number = int(raw_input("Please enter first number:"));
second_number = int(raw_input("Please enter second number:"));

remainder = first_number%second_number;
while (remainder != 0):
	first_number = second_number;
	second_number = remainder;
	remainder = first_number%second_number;
	gcd = second_number;
print "GCD is", gcd;

