#######################################################################################################################################################
# 
# Name: MANN RAMNANI 
# SID: 750001476
# Exam Date: 21 MARCH 2025
# Module: BEMM458 - Programming for Business Analytics
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/mock-test-2-mr9971
#
#######################################################################################################################################################
# Instruction 1. Read each question carefully and complete the scripts as instructed.

# Instruction 2. Only ethical and minimal use of AI is allowed. You may use AI to get advice on tool usage or language syntax, 
#                but not to generate code. Clearly indicate how and where you used AI.

# Instruction 3. Include comments explaining the logic of your code and the output as a comment below the code.

# Instruction 4. Commit to Git and upload to ELE once you finish.

#######################################################################################################################################################

# Question 1 - Loops and Lists
# You are given a list of numbers representing weekly sales in units.
weekly_sales = [120, 85, 100, 90, 110, 95, 130]

average_sales = sum(weekly_sales) / len(weekly_sales)
print("Average sales:", average_sales)

for sales in weekly_sales:
    if sales > average_sales:
        print("Above average:", sales)
    elif sales < average_sales:
        print("Below average:", sales)
    else:
        print("Equal to average:", sales)
        
# the code will print average sales as : 105.0 

# Write a for loop that iterates through the list and prints whether each week's sales were above or below the average sales for the period.
# Calculate and print the average sales.

#######################################################################################################################################################

# Question 2 - String Manipulation
# A customer feedback string is provided:
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""
# Given customer feedback string
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""

# List to store positions
positions = []

# Words to find
words = ["good", "improved"]

# initiating loop through each word and to find its first and last occurrence
for word in words:
    first_start = customer_feedback.find(word)  # First occurrence
    last_start = customer_feedback.rfind(word)  # Last occurrence

    # If the word exists in the string, calculate (start, end) positions
    if first_start != -1:
        first_end = first_start + len(word)
        positions.append((first_start, first_end))

    if last_start != -1 and last_start != first_start:  # Avoid duplicates if only one occurrence
        last_end = last_start + len(word)
        positions.append((last_start, last_end))

# Print the list of positions
print(positions)

# the code will print [(16, 20), (34, 42)]



# Find the first and last occurrence of the words 'good' and 'improved' in the feedback using string methods.
# Store each position in a list as a tuple (start, end) for both words and print the list.

#######################################################################################################################################################

# Question 3 - Functions for Business Metrics
# Define functions to calculate the following metrics, and call each function with sample values (use your student ID digits for customization).

# 1. Net Profit Margin: Calculate as (Net Profit / Revenue) * 100.
# 2. Customer Acquisition Cost (CAC): Calculate as (Total Marketing Cost / New Customers Acquired).
# 3. Net Promoter Score (NPS): Calculate as (Promoters - Detractors) / Total Respondents * 100.
# 4. Return on Investment (ROI): Calculate as (Net Gain from Investment / Investment Cost) * 100.

# 1. Net Profit Margin
def net_profit_margin(net_profit, revenue):
    """Calculate Net Profit Margin as (Net Profit / Revenue) * 100"""
    if revenue == 0:
        return "Revenue cannot be zero."
    return (net_profit / revenue) * 100

# 2. Customer Acquisition Cost (CAC)
def customer_acquisition_cost(total_marketing_cost, new_customers):
    """Calculate CAC as (Total Marketing Cost / New Customers Acquired)"""
    if new_customers == 0:
        return "New customers cannot be zero."
    return total_marketing_cost / new_customers

# 3. Net Promoter Score (NPS)
def net_promoter_score(promoters, detractors, total_respondents):
    """Calculate NPS as (Promoters - Detractors) / Total Respondents * 100"""
    if total_respondents == 0:
        return "Total respondents cannot be zero."
    return ((promoters - detractors) / total_respondents) * 100

# 4. Return on Investment (ROI)
def return_on_investment(net_gain, investment_cost):
    """Calculate ROI as (Net Gain from Investment / Investment Cost) * 100"""
    if investment_cost == 0:
        return "Investment cost cannot be zero."
    return (net_gain / investment_cost) * 100

# Sample values (Customize with digits from your student ID)
net_profit = 50000  
revenue = 200000  

total_marketing_cost = 10000  
new_customers = 200  

promoters = 120  
detractors = 30  
total_respondents = 200  

net_gain = 15000  
investment_cost = 50000  

# Calling the functions and printing the results
print(f"Net Profit Margin: {net_profit_margin(net_profit, revenue):.2f}%")
print(f"Customer Acquisition Cost (CAC): ${customer_acquisition_cost(total_marketing_cost, new_customers):.2f}")
print(f"Net Promoter Score (NPS): {net_promoter_score(promoters, detractors, total_respondents):.2f}")
print(f"Return on Investment (ROI): {return_on_investment(net_gain, investment_cost):.2f}%")


#######################################################################################################################################################

# Question 4 - Data Analysis with Pandas
# Using a dictionary sales_data, create a DataFrame from this dictionary, and display the DataFrame.
# Write code to calculate and print the cumulative monthly sales up to each month.
import pandas as pd

sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Sales': [200, 220, 210, 240, 250]}
#defining dataframe
df = pd.DataFrame(sales_data)

#calculating cumilitave sales, cumsum is cumilative sum function for monthly sales
df['Cumulative Sales'] = df['Sales'].cumsum()

#displaying the dataframe
print(df)

# the code will display the outcome as follows:
#   Month  Sales  Cumulative Sales
#0   Jan    200               200
#1   Feb    220               420
#2   Mar    210               630
#3   Apr    240               870
#4   May    250              1120

#######################################################################################################################################################

# Question 5 - Linear Regression for Forecasting
# Using the dataset below, create a linear regression model to predict the demand for given prices.
# Predict the demand if the company sets the price at £26. Show a scatter plot of the data points and plot the regression line.

# Price (£): 15, 18, 20, 22, 25, 27, 30
# Demand (Units): 200, 180, 170, 160, 150, 140, 130

# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

# Data
prices = np.array([15, 18, 20, 22, 25, 27, 30]).reshape(-1, 1)
demand = np.array([200, 180, 170, 160, 150, 140, 130])

# Linear regression model
model = LinearRegression()
model.fit(prices, demand)

#predicting the demand for price 26
price = np.array([26]).reshape(-1, 1)
predicted_demand = model.predict(price)
print("Predicted demand for price £26:", predicted_demand[0])

#generating regression line
regression_line = model.predict(prices)

#the probable outcome will be:
#Predicted demand for price £26: 145.71428571428572

#######################################################################################################################################################

# Question 6 - Error Handling
# You are given a dictionary of prices for different products.
prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}

# Write a function to calculate the total price of all items, handling any non-numeric values by skipping them.
# Include error handling in your function and explain where and why it’s needed.

#defining function to calculate total price
def total_price(prices):
    total = 0
    for product , price in prices.items():
        try:
            total += float(price)
        except (ValueError , TypeError):
            print(f"Skipping non-numeric value, price for product {product}: {price}")
    return total

#calculating total price of all items
total = total_price(prices)

#printing the total price
print ("Total price of all items:", total)

#the intended outcome will be:
#Skipping non-numeric value, price for product C: unknown
#Total price of all items: 155.0


#######################################################################################################################################################

# Question 7 - Plotting and Visualization
# Generate 50 random numbers between 1 and 500, then:
# Plot a histogram to visualize the distribution of these numbers.
# Add appropriate labels for the x-axis and y-axis, and include a title for the histogram.

import matplotlib.pyplot as plt
import random


# firstly generating 50 random numbers between 1 and 500
random_numbers = [random.randint(1, 500) for _ in range(50)]

#defining histogram figure size
plt.figure(figsize=(10, 5))

#plotting histogram
plt.hist(random_numbers, bins=10, color='skyblue', edgecolor='black')

#adding labels to x and y axis
plt.xlabel('Random Numbers')
plt.ylabel('Frequency')
plt.title('Distribution of 50 random numbers between 1 and 500')

#now show the plot
plt.show()

#the code will generate a histogram plot of 50 random numbers between 1 and 500



#######################################################################################################################################################

# Question 8 - List Comprehensions
# Given a list of integers representing order quantities.
quantities = [5, 12, 9, 15, 7, 10]

# Use a list comprehension to create a new list that doubles each quantity that is 10 or more.
# Print the original and the new lists.

#now defining the various list of quantities
quantities = [5, 12, 9, 15, 7, 10]

#using list comprehension to double each quantity that is 10 or more
new_quantities = [quantity * 2 for quantity in quantities if quantity >= 10]

#printing the original and new lists
print("Original list:", quantities)
print("New list with quantities doubled for quantities 10 or more:", new_quantities)

#the code will print the original list as [5, 12, 9, 15, 7, 10] and the new list as [24, 30, 20]


#######################################################################################################################################################

# Question 9 - Dictionary Manipulation
# Using the dictionary below, filter out the products with a rating of less than 4 and create a new dictionary with the remaining products.
ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}

#defining the dictionary
ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}

#filtering out the products with rating less than 4
filtered_ratings = {product: rating for product, rating in ratings.items() if rating >= 4}

#printing the new dictionary
print("Products with rating 4 or more:", filtered_ratings)
print("original ratings:", ratings)


#the code will print the new dictionary as {'product_A': 4, 'product_B': 5, 'product_E': 5}
#and the original dictionary as {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}
#######################################################################################################################################################

# Question 10 - Debugging and Correcting Code
# The following code intends to calculate the average of a list of numbers, but it contains errors:


# Identify and correct the errors in the code.
# Comment on each error and explain your fixes.


#defining the list of values
values = [10, 20, 30, 40, 50]

#initializing total to 0
total = 0

#iterating through the list of values
for i in values:
    total = total + i

#calculating the average
average = total / len(values)

#printing the average
print("The average is" + str(average))

#the code will print the average as 30.0


#######################################################################################################################################################
