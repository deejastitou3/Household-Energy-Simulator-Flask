#  Household Energy Consumption Simulator

An interactive web application built with Flask that simulates and analyzes the daily electrical energy consumption of a household. The project applies numerical integration methods—specifically the **Trapezoidal Rule**—to calculate total energy consumption from discrete hourly power profiles, and visualizes the results dynamically.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey)
![NumPy](https://img.shields.io/badge/NumPy-2.x-yellow)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange)

##  About the Project
Managing residential energy consumption is crucial for both economic and environmental reasons. This application allows users to input the characteristics of their household appliances (power rating and daily usage hours) to generate a realistic 24-hour power consumption profile $P(t)$. 

Instead of simple multiplication, the total energy is calculated by numerically integrating the power curve using the **Trapezoidal Rule**, demonstrating the practical application of numerical methods in engineering.

##  Key Features
- **Full-Stack Web App:** Built with Flask, featuring a clean HTML/CSS frontend and a robust Python backend.
- **Numerical Methods:** Implements the Trapezoidal Rule via NumPy to accurately approximate the integral of discrete power data.
- **Dynamic Visualization:** Generates real-time Matplotlib graphs to visualize the $P(t)$ profile and energy distribution.
- **Cost Estimation:** Calculates the daily and monthly energy costs based on user-defined electricity tariffs.

##  The Math: Trapezoidal Rule
Since power consumption $P(t)$ is sampled at discrete hourly intervals ($\Delta t = 1$ hour), the total energy $E$ is calculated by approximating the area under the curve:

$$
E \approx \sum_{i=0}^{n-1} \frac{P_i + P_{i+1}}{2} \Delta t
$$

This is efficiently implemented using `np.trapezoid()` (or `np.trapz()`), ensuring high precision for slowly varying residential load profiles.

##  Architecture (MVC-inspired)
- **`app.py`**: Controller. Handles web routes, user input, and orchestrates the simulation.
- **`simulation.py`**: Model. Generates realistic 24-hour power profiles based on typical household usage patterns.
- **`calculs.py`**: Model. Contains the numerical integration logic and cost calculations.
- **`templates/`**: View. HTML5/CSS3 files for the user interface.

## Results & Analysis
The simulator accurately reflects typical residential load curves:
Low consumption: 00:00 - 06:00 (Night)
Morning Peak: 06:00 - 09:00 (Breakfast, showers)
Evening Peak: 18:00 - 22:00 (Cooking, lighting, entertainment)
## Author
Khadija Stitou
Engineering Student in Intelligent Embedded Systems & Telecommunications
LinkedIn : (https://www.linkedin.com/in/khadija-stitou-b42792293)

   ```bash
   git clone https://github.com/deejastitou3/Household-Energy-Simulator-Flask.git
   cd Household-Energy-Simulator-Flask
