import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linregress1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = [y for y in range(df['Year'].min().item(), 2051)]
    y1 = [y * linregress1.slope + linregress1.intercept for y in x1]
    plt.plot(x1, y1)

    # Create second line of best fit
    df_reg2 = df.copy()
    df_reg2 = df.loc[(df_reg2['Year'] >= 2000)]
    linregress2 = linregress(df_reg2['Year'], df_reg2['CSIRO Adjusted Sea Level'])
    x2 = [y for y in range(2000, 2051)]
    y2 = [y * linregress2.slope + linregress2.intercept for y in x2]
    plt.plot(x2, y2)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()