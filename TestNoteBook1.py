# Databricks notebook source
# This code generates a list of 5 random integers between 1 and 10 and prints the maximum value
import random

numbers = []
for i in range(5):
    numbers.append(random.randint(1, 10))
    print(i)

print(f"The maximum value in the list is {max(numbers)}")

