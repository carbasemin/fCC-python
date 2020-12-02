import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & 
       (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(df, 'r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # We need years and months columns to produce a pivot table.
    # Well, not exactly to get a pivot table per se, but to get 
    # a pivot table in the way that would produce the plot we're aiming for. 
    df_bar.reset_index(inplace=True)
    df_bar['Years'] = [d.year for d in df_bar.date]
    df_bar['Months'] = [d.strftime('%B') for d in df_bar.date]

    df_bar = df_bar.pivot_table(values='value', index=['Years', 'Months'])
    
    # Years and Months are set as indexes, as expected, but that's not useful.
    # To plot the way we're plotting, we need them as columns.
    df_bar.reset_index(inplace=True)

    # Months are not ordered, we need them ordered for plotting though, so: 
    months = ['January', 'February', 'March', 'April',
            'May', 'June', 'July', 'August', 'September',
            'October', 'November', 'December']
    
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Setting the argument ax=ax to be able to use the 
    # object orianted interface of matplotlib.
    g = sns.barplot(x='Years', y='value', hue='Months',
                hue_order=months,
                data=df_bar, ax=ax)
    
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(loc='upper left')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))

    sns.boxplot(x='year', y='value', data=df_box, ax=ax[0])

    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[0].set_title('Year-wise Box Plot (Trend)')

    sns.boxplot(x='month', y='value', data=df_box,
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                ax=ax[1])

    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig