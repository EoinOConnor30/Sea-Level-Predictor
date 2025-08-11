import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    best_fit = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    New_Years = pd.Series(range(1880,2050))
    plt.plot(New_Years, best_fit.intercept + best_fit.slope*New_Years, 'r')


    # Create second line of best fit
    df2000 = df[df['Year']>1999]
    New_Years2 = pd.Series(range(2000,2050))
    best_fit2 = linregress(df2000['Year'], df2000['CSIRO Adjusted Sea Level'])
    plt.plot(New_Years2, best_fit2.intercept + best_fit2.slope*New_Years2, 'y')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')

    return plt.gca()
