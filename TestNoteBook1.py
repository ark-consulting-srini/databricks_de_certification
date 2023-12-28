# Databricks notebook source
# This code generates a list of 5 random integers between 1 and 10 and prints the maximum value
import random

numbers = []
for i in range(5):
    numbers.append(random.randint(1, 10))
    print(i)

print(f"The maximum value in the list is {max(numbers)}")


# COMMAND ----------

# Import necessary packages
from pyspark.sql.functions import *




# Load the sample data from Databricks
df = spark.read.format('csv').option('header', 'true').load('/databricks-datasets/samples/population-vs-price/data_geo.csv')

# Show the first 5 rows of the DataFrame
df.show(5)



