# Borehole-Dilution-Test

Link to git repository to get the code:

```
git clone https://github.com/Mohammed-Fadul/Borehole-Dilution-Test.git
```

## Theoretical Background
The borehole dilution test or point dilution test is a single-well technique for estimating horizontal flow velocity in the aquifer surrounding a well. The test is conducted by introducing a tracer into a well section and monitoring its decreasing concentration over time. A tracer is instantaneously injected into a borehole and is perfectly mixed within the borehole for the duration of testing in order to fulfil the ideal mixing condition. The mixing intensity should be adjusted to limit any turbulence it might induce to the well tube area and should not affect flow in the surrounding aquifer. The dilution of the tracer in the well due to the inflow of fresh water and the outflow of tracer-laced water from the well is then measured over time.

![alt text](https://github.com/Mohammed-Fadul/media/blob/1f13edbffc3d495676f5e8564559efb2529ebdd6/PrincipleBehindBDT.jpg)
**Fig 1*: Principle behind borehole dilution test*

Traditionally, the horizontal Darcy velocity is calculated as a function of the rate
of dilution and is based on the simple assumption that the decreasing tracer concentration is
proportional both to the apparent velocity into the test section and to the Darcy velocity in the
aquifer.

The dilution rate of the tracer solution, which is assumed to be homogeneously distributed in
borehole volume V, can be described by a simple differential equation derived from a 0-dimensional
balance in an ideal mixing reactor:

$$ {V' \over V}({c \over c_{0}}) = {dc \over dt} $$

with flux through the reactor $V' = {v_{app}}·F$, where vapp is the apparent dilution velocity (i.e., specific
flux) in the borehole due to groundwater-flow (m/s) and F is the area perpendicular to the direction
of undisturbed flow (m<sup>2</sup>); volume in which dilution takes place V [m3]; time t [s]; and actual and
initial concentrations c and co (kg/m<sup>3</sup>).
Separating variables and applying an initial condition (instantaneous tracer injection) leads to the
following analytical solution of the differential equation:

$$ {c \over c_{0}} = exp({-v_{app}.F.t \over V}) $$

or 

$$ {v_{app}} = -{V \over F.t} ln({-v_{app}.F.t \over V}) $$


Horizontal flow patterns in an aquifer are distorted by boreholes due to the well screen effect. This
effect is caused by convergence of the flow field due to contrasts in hydraulic conductivity between
the aquifer and the inside of the well (Figure 7.2). A dimensionless correction factor $\alpha$ can be used
to account for this distortion:

$$\alpha = Q_{b}/Q{f}$$


![alt text](https://github.com/Mohammed-Fadul/media/blob/1f13edbffc3d495676f5e8564559efb2529ebdd6/WellScreenEffect.jpg)

*Fig 2: Illustration showing the flowlines around the well and the well screen effect*

The correction factor $\alpha$ can be evaluated using potential theory as:

$$ {\alpha} = {4 \over {1 + ({r_{1} \over r_{2}})^2 + {k_{1} \over k_{2}}{[1 - ({r_{1} \over r_{2}})^2]}}} $$

with screen radii r1 and r2, screen permeability k1, and formation permeability k2. For simpilification,
the dimensions of the gravel filter and the screen/filter tube can be neglected,
and $\alpha = 2$. Considering:

$$ {v_{app}} = {v_{f} \alpha} $$

with Darcy velocity vf and assuming other complicating factors related to insufficient mixing, vertical
flow, density effects, etc. can be neglected, the following relationship follows:

$$ {v_{f}} = -{V \over \alpha.F.t} ln{c \over c_{0}} $$


### Purpose and motivation

The flow of groundwater is not measured directly through the sensors. The results obtained from the borehole dilution test are of the change in concentration of the tracer recorder over time, from which the velocity is calculated for each time step to generate the plot of velocity, from which the average Darcy velocity is calculated. The aim of this program is to generate the required plots to enable the user calculate Darcy's velocity via a graphical solution wich is the standard method, and to give instant estimate of the Darcy velocity from the data as a 50% percentile range.
An example of the file can be seen in later sections.

### Software Requirements

The software requirements to successfully run this program and obtain the Darcy Velocity are:    

1. Python 3.9.16 or more recent versions
2. libraries/modules:
      - numpy
      - pandas
      - os (Miscellaneous operating system interfaces)
      - math
      - typing
      - sklearn
      - matplotlib
      - pathlib
       
### Obtaining results

Upon meeting software requirements and getting all the python files in the local device, run the main script to get the an estimation of the velocity on
the console or the log file. Also, a new folder named (Plots) will appear in the directory where the program is saved that contains graphs generated from the given data. A new excel file contains all the calculated velocities will appear in the directory also a logfile containing the details of your run.

There is already an excel file named (All_Data) in the folder (Input_data_workbook) containing a typical data from a field test as an example of how the user 
should prepare his excel input file for reusing this code for other experiments.


## Code 

### Scripts  

The object-oriented codes use custom classes that are called within a `main.py` script which calculates the Darcy´s 
velocity average. The code is based on custom classes and functions that are defined in the following files:

1-logging_parameters (package) that contains:
* `checker.py`: contains logging functions

2-tracer_tests (package) that contains:
* `tracertests.py`: contains a Tracer class to read the basic elements of borehole test from field data, and make the ordinary
calculations needed for the calculation of Darcy´s velocity.

3-file_utiles (package) that contains:
* `base_file(package)`: contains `__init__.py` file which contains class BaseFile to check if data files exist
* `sensor_data_file.py`: contains the DataSheet, Calibration and SensorPairData classes to read the data from the sensors.

4-plot_settings (package) that contains:
* `plotSensors2.py`: contains the functions for the plots calculation - sensors plot, time concentration plot and 
velocity plots;
* `plot_saver.py`: contains a function to create a file to save plots in.

The relation among the classes and functions are according to the following diagram:

![alt text](https://github.com/Mohammed-Fadul/media/blob/a6d5d1b5823e1d292d988a7080570c4075761b29/Untitled%20Diagram.jpg)

### LOGGING FUNCTIONS
```{admonition} Code Requirements
Code Requirements: necessary to import the logging.
```
The `checker.py` is made of two functions:
1. `log_parameters`: contains all the basic configurations of the logging;
2. `logger`: this is a function wrapper for the main() function that are going to execute logging messages throughout the code.

**Note** - The logging information are going to be saved in the file `logfile.log`.

### FIELD DATA 
```{admonition} 
Code Requirements: necessary to import numpy library, and the logging_parameters function from the checker.py file.
```
The `tracertests.py` file has the variables and the methods which are relevant to Darcy´s velocity calculation. 
In the class `Tracer`, all the constant data taken from the local site test is found. They include: 
* Drilling´s and well´s diameter;
* Well´s head above ground level;
* Top of gravel pack below ground level;
* Top of filter screen below ground level;
* Bottom of well below ground level;
* Depth of filter below well´s head;
* Water table below well´s head;
* Initial concentration of the tracer in the well;
* Permeability of the gravel pack;
* Permeability of the aquifer formation;
* Accuracy of the fluorescence sensor.

By these information, it is possible to execute calculations found in the different functions within the Tracer class.
* Top gravel pack (`top_gravel_pack`): returns the distance from the wellhead to the top of the gravel pack;
* Top filter screen (`top_filter_screen`): returns the distance from the wellhead to the top of the filter screen;
* Water head (`water_head`): returns the profile of the water in the well measured from the bottom of the well;
* Volume in well (`volume_in_well`): returns the volume of the water in the well;
* Area of flow (`area_of_flow`): returns the area perpendicular to the flow direction;
* Calculate alpha (`calculate_alpha`): returns the correction factor borehole horizontal flow rate Qb and aquifer horizontal flow rate Qf;
* Calculate vf (`calculate_vf`): returns the area of the screen filter.

### SENSORS DATA 
```{admonition} 
Code Requirements: necessary to import logging, pandas, numpy, typing and sklearn libraries, and to inherit the file_utils 
from the BaseFile in __init__.py (packet base_files).
```
The provided sensors data is stored in the xlsx workbook **All_Data.xlsx** which contains the following information:

| **dilution time(s)** | **fluorescense** |
|----------------------|------------------|
| 0                    | 2                |
| 5                    | 5                |
| 10                   | 7                |
| ...                  | ...              |


| **Flourescense** | **µg/L Uranine** |
|------------------|------------------|
| -3               | 0                |
| 8                | 10               |
| 23               | 25               |
| ...              | ...              |

In the excel file, the dilution time vs fluorescense table is located in the **Data DC** and **Data FC** sheet, giving information of each 
sensor test. While, Flourescense vs Uranine table is located in the **DC calibration** and **FC calibration** sheet with the information of each sensor´s calibration. 
* Basefile: checks if the file to be opened exists  
* DataSheet & CalibrationSheet: Two small classes are written to check the if the right column names exist in calibration and data files for both sensors. If the 
* SensorPairData: After reading from the excel files, the calibration data is checked for linear correlation and the coefficient of determination is calculated

### PLOTS 
```{admonition} 
Code Requirements: necessary to import logging, matplot and os libraries, and to inherit from the file plot_saver the function 
save_plot.
```

The `plotSensors2.py` contains three functions with different outputs each: 

1. `sensors_plot` - the parameters of this function are the calibration data from each type of sensor, in which returns the plot of flourescence vs uranine;

![alt text](https://github.com/Mohammed-Fadul/media/blob/1f13edbffc3d495676f5e8564559efb2529ebdd6/SensorsPlot.png)

**Fig 4*: Sensors Plot*

2. `time_concentration_plot`- function that returs the plot of the Time vs Fluorescence for each sensor. The parameters are the tests results from each sensor.

![alt text](https://github.com/Mohammed-Fadul/media/blob/1f13edbffc3d495676f5e8564559efb2529ebdd6/TimevsConcentration.png)

**Fig 5*: Time vs Fluorescence Plot*

3. `velocity_plot` - function that returns the plot of Darcy´s Velocity vs Time vs Fluorescence concentration for each sensor. The parameters are also the tests results frome each sensors plus the calculated Darcy´s velocity. 

![alt text](https://github.com/Mohammed-Fadul/media/blob/1f13edbffc3d495676f5e8564559efb2529ebdd6/VelocityvsConcentration.png)

**Fig 6*: Darcy´s Velocity vs Time vs Fluorescence Plot*

The `plotSensors2.py` inherits the `plot_saver.py` which contains the function `save_plot` that allows the plot to be correctly saved in the -named given - folder. It also returns logging information in case of exceptions. The arguments for the save_plot are the folder path, plot and the name of the image which are given when calling this function inside of each plot function. 


### DARCY´S VELOCITY CALCULATION 
```{admonition} 
Code Requirements: necessary to import pandas and math libraries, and to inherit functions from the tracertests, sensor_data_file, 
plotSensors2 and checker. 
```
The Darcy´s velocity is calculated in the `main.py` script. In this file we can find: 
* `darcys_velocity_each_second`: this function returns the data frame containing the final darcy´s velocity of each time. 
It receives the field_data, the slope of the sensor´s equation and intercept of the sensor´s equation as parameters. 

* `darcys_velocity_averaged`: this function returns the Darcy´s velocity averaged, and 25% of the lower and upper values 
are excluded giving a 50% of range.

* `main`: the main function is responsible for calling the functions in the correct order: 
1. This fuction sets the document´s information (**All_Data.xlsx**), as parameters to the `sensor_data_file.py`;
2. The instantiation of the objects and attributes are saved in variables which take the information also from 
`sensor_data_file.py` (eg: regression line information, calibration information and sensors information);
3. After having all the necessary inputs, it is called `darcys_velocity_each_second` with the required parameters for each type of sensor;
4. The `darcys_velocity_averaged` is executed with a logging message that allows to know which type of sensor is this Darcy´s velocity result;

![alt text](https://github.com/Mohammed-Fadul/media/blob/5af71239841c4bf1abf50a0fa0eb77d416d22d93/seccessful_run.jpg)

**Fig 7*: Logging messages after running code*

![alt text](https://github.com/Mohammed-Fadul/media/blob/5af71239841c4bf1abf50a0fa0eb77d416d22d93/final_results.jpg)

**Fig 8*: Logging messages after running code*

5. When successfully runned, the information is saved in a excel file named **Results.xlsx** that looks like this:

|    | Time | Flourescense | Uranine(mg/l) | ln(c/c0) | vf(m/s)   |
|----|------|-------------|---------------|----------|-----------|
| 0  | 0    | 2           | 0,001         |  -13,71  | 837038,04 |
| 1  | 5    | 5           | 0,001         | -13,71   | 0,16      |
| 2  | 10   | 7           | 0,001         | -13,71   | 0,083     |
| 3  | 20   | 39          | 40,07         | -3,11    | 0,012     |
| 4  | 25   | 51          | 52,11         | -2,84    | 0,008     |
| ...| ...  | ...         | ...           | ...      |   ...     |

6. Last, the plots are executed when calling the functions `velocity_plot`, `time_concentration_plot` and `sensors_plot` with the corrected parameters.
and the new files for the results and logging will be generated.

![alt text](https://github.com/Mohammed-Fadul/media/blob/5df8364cf511e0f014c6c672aee74ba4981d6af4/generatedfiles.jpg)
**Fig 9*: New generated files*

### Troubleshooting:
This code is provided with many (safety) code lines that prevent your code run from crashing, for example division by zero errors, natural logarithms of negative values errors, etc. and the logging will provide you with details for each error,these errors are fixed within the code to provide the user with reliable results.

Listed below are the major errors that you might run into:

1. (Module_Not_Found ); this error happens when you are working in an environment that doesn’t contain all the required modules to run the code
2. (Invalid inputs that track information from excel. Check them again) ; this message error appears when your input file doesn’t match the name or the location of the input file, this setup is the most important in this code because if the input file is not formatted properly the code will not be able to do any calculations
3. Other errors (while the code is able to run); details can be found in the log file
4. to make sure that your results are valid please check the generated curves and compare them with the samples provided in this README documentation or any previous tests that you trust.
5. BaseFileERROR: if file does not exist or exists in a different name. Check the names of column and file names for spelling.

