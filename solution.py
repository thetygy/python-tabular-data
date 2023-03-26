#!/c/Users/ctw28/anaconda3/python.exe
"A module for creating a png scatterplot of petal vs sepal length for individula flower species"

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def plot_flower_lengths():
    """
    Returns a .png scatterplot with regression line for species denoted in the "species" list
    
    Parameters
    ----------
    Input .csv file to be read into data frame

    Returns
    --------
    One .png scatterplot per listed species
    """
    #Define species
    species=["Iris_setosa","Iris_virginica","Iris_versicolor"]
    # Read data frame
    dataframe= pd.read_csv("iris.csv")
    for flower_name in species:
        # Species specific data frame
        flower=dataframe[dataframe.species==flower_name]
         # Define graphing variables
        x = flower.petal_length_cm
        y = flower.sepal_length_cm
        # Regress
        regression = stats.linregress(x, y)
        # Generate the scatterplot info using regression info
        slope = regression.slope
        intercept = regression.intercept
        # Create new plot for new species
        plt.figure()
        # Define plot type and plot variable sources
        plt.scatter(x, y, label = 'Data')
        plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
        # Labels for axes and title
        plt.title("Petal Length vs. Sepal Length of "+flower_name)
        plt.xlabel("Petal length (cm)")
        plt.ylabel("Sepal length (cm)")
        plt.legend()
        # Save plot file as .png
        plt.savefig(flower_name+"petal_v_sepal_length_regress.png")
        # Output progress statement to the command line
        print("Analyzed "+flower_name)

if __name__ == '__main__':
    plot_flower_lengths()