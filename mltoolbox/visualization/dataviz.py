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

    def plot_boxplot(self,
                     df:pd.DataFrame,
                     column:str,
                     ylabel:str=None,
                     title:str=None)->None:
        """
        Plots a boxplot from a dataframe.

        Parameters:
        ----------

        df: pd.DataFrame
            Dataframe to plot boxplot from.

        column: str
            Column to plot boxplot from.

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
        >>> dv.plot_boxplot(df, 'a')
        """

        # Use seaborn to plot the boxplot
        sns.set(rc={'figure.figsize': self.figsize})
        sns.boxplot(y=column,
                    data=df,
                    width=0.5,
                    palette='Set2',
                    fliersize=5,
                    linewidth=1.5)


        # If some of the parameters are not set, set them
        if ylabel is None:
            ylabel = column
        if title is None:
            title = 'Boxplot of ' + column

        plt.ylabel(ylabel)
        plt.title(title)

        # Show the plot
        plt.show()

    def plot_scatterplot(self,
                         df:pd.DataFrame,
                         x:str,
                         y:str,
                         xlabel:str=None,
                         ylabel:str=None,
                         title:str=None)->None:
        """
        Plots a scatterplot from a dataframe.

        Parameters:
        ----------

        df: pd.DataFrame
            Dataframe to plot scatterplot from.

        x: str
            Column to plot on the x-axis.

        y: str
            Column to plot on the y-axis.

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
        >>> df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        ...                    'b': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
        >>> dv = DataViz()
        >>> dv.plot_scatterplot(df, 'a', 'b')
        """

        # Use seaborn to plot the scatterplot
        sns.set(rc={'figure.figsize': self.figsize})
        sns.scatterplot(x=x,
                        y=y,
                        data=df)

        # If some of the parameters are not set, set them
        if xlabel is None:
            xlabel = x
        if ylabel is None:
            ylabel = y
        if title is None:
            title = 'Scatterplot of ' + x + ' and ' + y

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)

        # Show the plot
        plt.show()