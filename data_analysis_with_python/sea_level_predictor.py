import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    data = data[['Year', 'CSIRO Adjusted Sea Level']]

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    years = np.arange(1880, 2050)

    slope, intercept, rvalue, pvalue, stderr = linregress(data['Year'],
                                                            data['CSIRO Adjusted Sea Level'])

    plt.plot(years, intercept + slope*years, 'r')
    
    # Create second line of best fit
    years_2 = np.arange(2000, 2050)
    
    data_20th_cent = data[data['Year'] > 1999]
    
    slope_2, intercept_2, rvalue_2, pvalue_2, stderr_2 = linregress(data_20th_cent['Year'],
                                                                    data_20th_cent['CSIRO Adjusted Sea Level'])

    plt.plot(years_2, intercept_2 + slope_2*years_2, 'r')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()