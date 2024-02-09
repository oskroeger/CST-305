Compile this code in a Linux/Ubuntu environment.

----- Differential Equation Solver -----

This Python script solves a specific differential equation using two methods: the Runge-Kutta 4th order method (RK4) and the odeint method from SciPy, and then plots the results for comparison.


----- Requirements ------

Python 3
NumPy
SciPy
Matplotlib


----- Environment Setup -----

- Update Libraries

sudo apt update

- Ensure you have Python 3 installed on your Ubuntu system. You can check this by running:

python3 --version

- If Python 3 is not installed, install it using Ubuntu's package manager:

sudo apt install python3

- Next, install the required Python libraries:

sudo apt install python3-pip
pip3 install numpy scipy matplotlib


----- Running the Script -----

- Make sure all files are downloaded and unzipped

- Place all included files inside the same directory

- Open a terminal and navigate to the directory containing the files

- Run the script using Python 3:

python3 ProjectTwo.py


----- What the Script Does -----

- It defines a differential equation as a Python function.
- It implements a recursive function to solve this differential equation using the RK4 method.
- It also solves the same equation using the odeint method for comparison.
- It prints the first 6 solutions obtained with both RK4 and odeint.
- Finally, it plots the solutions from both methods alongside each other for visual comparison.


----- Output -----

- The script will output the first 6 solutions from both the RK4 and odeint methods in the terminal. It will also display a graphical plot with three subplots:
	- The solution using the RK4 method.
	- The solution using the odeint method.
	- A comparison of both solutions on the same plot.

