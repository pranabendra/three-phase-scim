# Three Phase Squirrel Cage Induction Motor Design

## What does this Python package do?
This interactive package has a collection of modules, that performs individual design steps for a Squirrel Cage Induction Motor. 
The user has to input the full-load (nameplate) ratings and this package will generate the design sheet, considering the design constraints at hand. 

## Prerequisites
1. Python 3 (3.6+ preferred). Download [here](https://www.python.org/downloads/).  
2. Should be able to view/read Excel(.xlsx) files.

## Installation
Open terminal or command prompt, and run `pip install threephasescim` or `pip3 install threephasescim` depending on your OS.
This will download and install the latest release, along with the required libraries. 

## Before you run it
Should have the following full-load ratings. Take care of the units. 
- Power Rating (kW). Eg.: 5
- Power Factor (lagging). Eg.: 0.85
- Efficiency (per unit). Eg.: 0.9
- Speed (rpm). Eg.: 1500
- Line Voltage (V). Eg.: 110

## Expected Output
- 1. Average field flux (Wb/m<sup>2</sup>)
  2. Ampere conductor (ac)
  3. Expected efficiency (%)
  4. Obtained efficiency (%)
  5. Temperature rise (&deg;C)
  6. Current criterion satisfied? (yes/no)
- Design sheet containing all the design parameters of the machine to be designed (if a solution is present). 
- Else, it will show `Design sheet failed...`. In this case, it is advised to dive into the basics of machine design and tune the ratings accordingly. Then, retry. 

## How to get your design sheet?
### Running the package as a scipt
1. Open terminal or command prompt.
2. Naviagte to the directory/path where you want the design sheet to be saved.
3. Type `python -m threephasescim` or `python3 -m threephasescim` and run, depending on your OS.
4. Enter all the required ratings, as asked.
5. If the design sheet is successfully prepared, then, find it in the current working directory/path. 
### Running as an import
Open `ipython` or `ipython3` or Python shell.

`>>> import threephasescim.master as thd` <br />
When running the above line for first time, you will be asked to enter all the required ratings.

To show the saved ratings, <br />
`>>> thd.show_rating()`

To enter a new set of ratings, <br />
`>>> thd.set_rating()`

To get your design sheet, <br />
`>>> thd.design_your_machine()`

If the design sheet is successfully prepared, then, find it in the current working directory/path.

## What to do now?
- For more detailed analysis or insights, click [here](https://github.com/pranabendra/three-phase-scim/tree/master/threephasescim/threephasescim).
- If facing any design issues, open an issue.
- For any suggestions, open an issue.

## Reference
A Course in Electrical Machine Design  
A.K.Sawhney, A.Chakrabarti  
Dhanpat Rai & Co. 2006  

## Acknowledgement
Sincere thanks to Prof. Susanta Ray, Electrical Engineering Department, Jadavpur University for allowing the design of induction machines programmatically.
