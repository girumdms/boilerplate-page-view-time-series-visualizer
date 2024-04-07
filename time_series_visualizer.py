import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import calendar

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=["date"], index_col='date')

# Clean data
df = df.value[(df.value > df.value.quantile(0.025)) & (df.value < df.value.quantile(0.975))]
df = df.reset_index(['date'])

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(30,8))
    plt.plot(df['date'], df['value'], color='r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=["date"], index_col='date')
    df = df.value[(df.value > df.value.quantile(0.025)) & (df.value < df.value.quantile(0.975))]
    df = df.reset_index(['date'])
    df = df.set_index('date')
    df_bar = df.groupby([df.index.year, df.index.month_name()]).mean().value.unstack()
    df_barr = df_bar[list(calendar.month_name)[1:]]
    
    
    # Draw bar plot
    fig = plt.figure(figsize=(30,8))
    ax = df_barr.plot.bar(xlabel='Years', ylabel = 'Average page views')


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
    fig, axs = plt.subplot(1, 2, figsize = (20,4))
    sns.boxplot(data = df_box, x=df_box['year'], y= df_box['value'], axs = [1,1]).set(xlabel = 'Year', ylabel = 'Page Views', title = 'Year-wise Box Plot (Trend)')
    sns.boxplot(data= df_box, x = df_box['month'], y= df_box['value'], axs = [1,2]).set(xlabel = 'Month', ylabel = 'Page Views',title = 'Month-Wise Box Plot (Seasonality)')





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
