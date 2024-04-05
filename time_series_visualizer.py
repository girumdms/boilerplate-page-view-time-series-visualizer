import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', usecols=['date', 'value'], parse_dates = ["date"], index_col="date")

# Clean data
df = df.value[(df.value > df.value.quantile(0.025)) & (df.value < df.value.quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(30,8))
    plt.plot(df['date'], df['value'], color='r')
    plt.title('Daily freecodecamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month_name()]).mean().value.unstack()
    g= df.groupby([df.index.month_name(), df.index.year]).mean().value.unstack()
    #df_bar1 = df_bar[list(calendar.month_name)[1:]]
    
    # Draw bar plot
    df_bar.columns.name = "Months"
    fig = df_bar.plot(kind= 'bar', figsize= (12,6), xlabel='Years', ylabel = 'Average page views')




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
    sns.boxplot(data=g, ax = ax[0]).set(xlabel = 'Year', ylabel = 'Page Views', title = 'Year-wise Box Plot (Trend)')
    sns.boxplot(data=df_bar1, ax = ax[1]).set(xlabel = 'Month', ylabel = 'Page Views',title = 'Month-Wise Box Plot (Seasonality)')





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
