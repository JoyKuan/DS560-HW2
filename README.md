# DSCI 560 - Visualization of the linear function


#### Author: Kuan-Hui Lin
Citing Visualization of the linear function:
If you want to cite the latest version of the software, you can do by using 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4042175.svg)](https://doi.org/10.5281/zenodo.4042175)

# Downloading the scripts
To download three Python scripts, you need to make sure you have Python3 on your Mac. If you have old Python version, please update it.
The latest release for donloading: https://github.com/JoyKuan/DS560-HW2/releases/latest

# Description
Visualization of the linear function is help you create a scatter chart including all the data points lie on the line given by equation y=3x+6 with all values of x from x dataset and all values of y from y dataset and save the graph of the result into the disk. 
Follow by following tasks:
1. Generate 1000 random numbers over the range 0-100
2. Generate new numbers from the original 1000 using the equation y=3x+6
3. Visualize the results
You will see two datasets(.csv) which are saved in your disk and the graph of the equation y=3x+6.

<iframe src="https://widgets.figshare.com/articles/12979160/embed?show_title=false" width="568" height="351"  frameborder="0"></iframe>

# Technologies
* Python 3.7
* Matplotlib 3.3.2

# Setup
Before to run plot_equation.py, you need to install Matplotlib:

+ Install Matplotlib with Anaconda Prompt
```bash
conda install matplotlib
```
+ Install Matplotlib with pip
##### Use the package manager pip to install matplotlib
```bash
pip install matplotlib
```

# How to run Python scripts
Open a command-line and type in the word python3 if you hava python3 version, and then run them in order, followed by the path to these three scripts:
```bash
$ python3 generate_input_x.py
$ python3 generate_output_y.py
$ python3 plot_equation.py
```

# Output Files
If there is no problem after you run all three scripts in order, you will see three output files in your disk.
1. x_dataset.csv
2. y_dataset.csv
3. equation_graph.png
If this does not work right, you will need to check your Python installation.

# Jupyter Notebook
This Python Notebook that calls the three scripts, generate_input_x.py, generate_output_y.py and plot_equation.py, in order. You can follow the instructions mentioned in Notebook, and then you will see the graph of a linear equation y=3x+6.
HW2.ipynb

# License
[![DOI](https://zenodo.org/badge/297493565.svg)](https://zenodo.org/badge/latestdoi/297493565)


