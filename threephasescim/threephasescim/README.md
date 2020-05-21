# THREE PHASE SQUIRREL CAGE INDUCTION MOTOR DESIGN
Program has been written by Pranabendra Prasad Chandra and Anwesa Bhattacharya.  

## PROLOGUE
Dedicated to all the students who had to relentlessly iterate and reiterate to solve a machine design problem.

## MOTIVATION
This program intends to eliminate the mind numbing iterations usually involved in a design problem. (Please note: This program is capable of designing only an induction machine of the given rating. Please do not generalize. But, we hope that this program will become an inspiration/(or *source* :P ) for others who wish to design similar programs for other electrical machines).

**The Catch:** The designed SCIM might not be the most cost efficient compared to a manual design, but it's certainly way more time efficient. 

### (You win some, you lose some :P) 

## CODE STYLE
**"Freestyle"** (as long as enthusiastic developers do not disturb the functioning of the rest of the program :) )

---

## INSTALLATION

1. Python 3 (3.6+ preferred). Download [here](https://www.python.org/downloads/).  
2. Packages required - numpy, pandas, scipy, xlrd. In Windows, run `pip install numpy pandas scipy xlrd openpyxl --user`. In Linux/Mac, run `sudo pip3 install numpy pandas scipy xlrd openpyxl`.  
3. Download the repository as a `.zip` or `.tar.gz` file. Extract it in suitable location.
4. Open terminal/cmd and enter inside the **three_phase_scim** directory.
5. Run `python master.py` in Windows. In Linux/Mac, run `python3 master.py`

---

## INSTRUCTIONS FOR USE

### 1. Input

The following specifications are necessary:  
a) Line Voltage (in Volt)  
b) Power in kW (make sure you convert your hp ratings to kW. And if you do not know how to, here's how: 1hp = 0.746 kW)  
c) Synchronous speed(in rpm)  
d) Efficiency  
e) Power Factor  

### 2. How to get the output

After entering rating in the specified format, run the *master.py* file.

### 3. Output

A few hundred lines of results of calculation (very helpful for college students taking or having to take a course named machine design)
Also, a design sheet consisting of:  
a) Main Dimensions (D, L etc)  ----> To know what D, L mean, refer to the below mentioned book  
b) Stator Dimensions  
c) Rotor Dimensions  
d) Parameters of the IM equivalent circuit  
e) Temperature rise above ambient  
f) Last, but not the least (*pun intended*)...cost of the designed SCIM  

---

## REFERENCE

A Course in Electrical Machine Design  
A.K.Sawhney, A.Chakrabarti  
Dhanpat Rai & Co. 2006  

---

## EPILOGUE

Roses are red,  
Violets are blue.  
Machine Design -  
We ____ you.  

*(anyone familiar with machine design is free to fill in the blank)*

Before you move on, don't be disheartened to go ahead and explore the repository.
