"""
Class responsible for plotting graphs and charts from dataframes,
using matplotlib and seaborn.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class DataViz:
    def __init__(self, figsize=(8, 5)):
        """
        Constructor.

        Parameters:
        ----------
        figsize: tuple, default=(8, 5)
            Figure size.
        """
        self.figsize = figsize

    def set_figsize(self, figsize:tuple)->None:
        """
        Sets the figure size.

        Parameters:
        ----------
        figsize: tuple
            Figure size.

        Returns:
        -------
        None
        """
        self.figsize = figsize

    def plot_histogram(self,
                       df:pd.DataFrame,
                       column:str,
                       bins:int=10,
                       xlabel:str=None,
                       ylabel:str=None,
                       title:str=None)->None:
        """
        Plots a histogram from a dataframe.

        Parameters:
        ----------

        df: pd.DataFrame
            Dataframe to plot histogram from.

        column: str
            Column to plot histogram from.

        bins: int, default=10
            Number of bins to use.

        xlabel: str, default=None
            Label for the x-axis.

        ylabel: str, default=None
            Label for the y-axis.

        title: str, default=None
            Title of the plot.

        Returns:
        -------
        None

        Example:
        --------
        >>> import pandas as pd
        >>> from mltoolbox.visualization.dataviz import DataViz
        >>> df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
        >>> dv = DataViz()
        >>> dv.plot_histogram(df, 'a')
        """

        # Use seaborn to plot the histogram
        sns.displot(df,
                    x=column,
                    bins=bins,
                    kde=True,
                    height=self.figsize[1],
                    aspect=self.figsize[0]/self.figsize[1])

        # If some of the parameters are not set, set them
        if xlabel is None:
            xlabel = column
        if ylabel is None:
            ylabel = 'Frequency'
        if title is None:
            title = 'Histogram of ' + column

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)

        # Show the plot
        plt.show()
