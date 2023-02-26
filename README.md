# Borehole-Dilution-Test


1.  Code description (purpose, motivation goals)
2. usage/run instructions
3. requirements (incl all non standard python libraries)
4. code diagram (uml/activity diagram)
5. usage of all functions incl classes (input arguements and output incl data types)


## Theoretical Background
The borehole dilution test or point dilution test is a single-well technique for estimating horizontal flow velocity in the
aquifer surrounding a well. The test is conducted by introducing a tracer into a well section and
monitoring its decreasing concentration over time. A tracer is instantaneously injected into a borehole and is perfectly mixed within the borehole for
the duration of testing in order to fulfil the ideal mixing condition. The mixing intensity should be
adjusted to limit any turbulence it might induce to the well tube area and should not affect flow in
the surrounding aquifer. The dilution of the tracer in the well due to the inflow of fresh water and
the outflow of tracer-laced water from the well is then measured over time.

![alt text](PrincipleBehindBDT.jpg)
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


![alt text](WellScreenEffect.jpg)

*Fig 2: Illustration showing the flowlines around the well and the well screen effect*

The correction factor $\alpha$ can be evaluated using potential theory as:

$$ {\alpha} = {4 \over {1 + ({r_{1} \over r_{2}})^2 + {k_{1} \over k_{2}}{[1 - ({r_{1} \over r_{2}})^2]}}} $$

with screen radii r1 and r2, screen permeability k1, and formation permeability k2. For the wells at
the site in Horkheim, the dimensions of the gravel filter and the screen/filter tube can be neglected,
and $\alpha = 2$. Considering:

$$ {v_{app}} = {v_{f} \alpha} $$

with Darcy velocity vf and assuming other complicating factors related to insufficient mixing, vertical
flow, density effects, etc. can be neglected, the following relationship follows:

$$ {v_{f}} = -{V \over \alpha.F.t} ln{c \over c_{0}} $$

### Purpose and motivation

Through this program, we want


The structure of the code is as follows:

![alt text](flowchart(new).jpg)

### Software Requirements

The software requirements to successfully run this program and obtain the Darcy Velocity are:

Link to git repository to get the code:

```
git clone https://github.com/Mohammed-Fadul/Borehole-Dilution-Test.git
```
    

1. Anaconda navigator
2. Integrated Development Environments (IDEs): PyCharm or Visual Studio Code (im not entirely sure)
3. Python 3.9.16 or more recent versions
4. Numpy and pandas

### Obtaining results

Upon meeting software requirements and getting all the python files in the local device, run the main script to get the velocity.
Also, the graphs generating from the given data are saved in the folder SamplePlots.


