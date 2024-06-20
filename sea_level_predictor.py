import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(16, 6))
    plt.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)

    # Create first line of best fit
    fit1 = linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
    y_pred = fit1.intercept + fit1.slope * np.arange(df['Year'].min(),2051,1)

    plt.plot(np.arange(df['Year'].min(),2051,1), y_pred)

    # Create second line of best fit
    df2 = df[df["Year"] >= 2000]
    fit2 = linregress(df2["Year"],df2["CSIRO Adjusted Sea Level"])
    y_pred2 = fit2.intercept + fit2.slope * np.arange(df2['Year'].min(),2051,1)     

    plt.plot(np.arange(2000,2051,1), y_pred2)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()