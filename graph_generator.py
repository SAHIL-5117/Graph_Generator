"""
graph_generator.py is a GUI application that reads data from a .csv file and generates a graph from the data.

Usage: Python3 graph_generator.py

sample .csv file: 
x-axis,y-axis
1,4
2,5
3,2
4,8
5,3

author: Luke Billard
"""

import sys

import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Global variable to store the data from the CSV file
data = None

# Function for opening the CSV file and reading the data into the global variable
def open_csv():
    global data
    file = QFileDialog.getOpenFileName()
    file_path = file[0] # the first argument of the tuple returned by getOpenFileName is the file path
    data = pd.read_csv(file_path) # read the data from the csv file into the global variable
    
# Function for generating the graph from the provided data
def generate_graph():
    global data
    if data is not None:
        # Generate a graph depending on the type of graph selected by the user
        graph_type = graph_type_select.currentText()
        if graph_type == 'Line':
            canvas = FigureCanvas(plt.figure())
            plt.plot(data.iloc[:, 0], data.iloc[:, 1]) # The first column is the x-axis and the second column is the y-axis
            plt.xlabel(data.columns[0]) # The label of the x axis is the name of the first column in the .csv file
            plt.ylabel(data.columns[1]) # The label of the y axis is the name of the second column in the .csv file
            plt.title(graph_type + " Graph")
            layout.addWidget(canvas, 4, 0)

        elif graph_type == 'Bar':
            canvas = FigureCanvas(plt.figure())
            plt.bar(data.iloc[:, 0], data.iloc[:, 1])
            plt.xlabel(data.columns[0])
            plt.ylabel(data.columns[1])
            plt.title(graph_type + " Graph")
            layout.addWidget(canvas, 4, 0)

        elif graph_type == 'Histogram':
            canvas = FigureCanvas(plt.figure())
            plt.hist(data.iloc[:, 1])
            plt.xlabel(data.columns[0])
            plt.ylabel(data.columns[1])
            plt.title(graph_type + " Graph")
            layout.addWidget(canvas, 4, 0)

        elif graph_type == 'Scatter':
            canvas = FigureCanvas(plt.figure())
            plt.scatter(data.iloc[:, 0], data.iloc[:, 1])
            plt.xlabel(data.columns[0])
            plt.ylabel(data.columns[1])
            plt.title(graph_type + " Graph")
            layout.addWidget(canvas, 4, 0)
    else:
        print("No data to generate graph from")

# Initialize the gui 
app = QApplication([])
window = QWidget()
window.resize(640, 380)
window.setWindowTitle("Graph Generator")
layout = QGridLayout()


# Label for explaining the gui
explanation = QLabel('Select a .csv file containing data \n')

# Button for choosing the csv file
csv_button = QPushButton('choose csv file')
csv_button.setMaximumSize(150, 50)
csv_button.clicked.connect(open_csv) # Connect the csv button to the open_csv function

# Button for generating the graph
graph_button = QPushButton('Generate Graph')
graph_button.setMaximumSize(150, 50)
graph_button.clicked.connect(generate_graph) # Connect the graph buttonto the generate_graph function

# Label for choosing which type of graph to generate
graph_type_label = QLabel('Choose the type of graph to generate')
graph_type_select = QComboBox()
graph_type_select.addItem('Line')
graph_type_select.addItem('Scatter')
graph_type_select.addItem('Bar')
graph_type_select.addItem('Histogram')


# Render widgets
layout.addWidget(explanation, 0, 0) # Because of the grid layout, widgets are placed by stating the row and column
layout.addWidget(csv_button, 0, 1)
layout.addWidget(graph_button, 3, 1)
layout.addWidget(graph_type_label, 2, 0)
layout.addWidget(graph_type_select, 3, 0)

# Display the gui
window.setLayout(layout)
window.show()
sys.exit(app.exec()) # Begin the event loop and exit the application when the window is closed