# DSCI 560 - Visualization of the linear function

#### Author: Kuan-Hui Lin

**Citing Visualization of the linear function:**
If you want to cite the latest version of the software, you can do by using https://doi.org/10.5281/zenodo.4048948

# Downloading the scripts
To download three Python scripts, you need to make sure you have Python3 on your Mac. If you have old Python version, please update it. 
The latest release for downloading: https://github.com/JoyKuan/DS560-HW2/releases/latest

# Description
Visualization of the linear function is help you create a scatter chart including all the data points lie on the line given by equation y=3x+6 with all values of x from x dataset and all values of y from y dataset and save the graph of the result into the disk. 
Follow by following tasks:
1. Generate 1000 random numbers over the range 0-100
2. Generate new numbers from the original 1000 using the equation y=3x+6
3. Visualize the results

You will see two datasets(.csv) which are saved in your disk and the graph of the equation y=3x+6.

### Visualization of the linear function:
![image](https://user-images.githubusercontent.com/54604816/94120168-ad5b7d80-fe04-11ea-977c-5722a2e452b6.png)

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
  Use the package manager pip to install matplotlib
```bash
pip install matplotlib
```

# How to run Python scripts
System: Mac
Open a command-line and take note of the path of the Python script in Finder. Use the cd command to navigate to the folder containing the Python file. If you copied the pathname, paste the pathname after the cd command. If you hava python3 version, and then run them in order. Type the following command to execute three scripts:
```bash
$ python3 generate_input_x.py
$ python3 generate_output_y.py
$ python3 plot_equation.py
```

# Output Files
If there is no problem after you run all three scripts in order, you will see three output files in your disk.
If there exists some problems, you will need to check your Python installation.

**Output Files:**
1. x_dataset.csv
2. y_dataset.csv
3. equation_graph.png

# Jupyter Notebook
See notebook [visualization_equation.ipynb](https://github.com/JoyKuan/DS560-HW2/blob/master/visualization_equation.ipynb).

This Python Notebook that calls the three scripts, generate_input_x.py, generate_output_y.py and plot_equation.py, in order. You can follow the instructions mentioned in Notebook, and then you will see the graph of a linear equation y=3x+6.

# License
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4048948.svg)](https://doi.org/10.5281/zenodo.4048948)


