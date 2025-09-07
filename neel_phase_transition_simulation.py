#Antiferromagnetic
#Neel_Temprature_Simulation.py

'''
=======================================================================
   1D Ising Model Simulation of a Magnetic Phase Transition
=======================================================================
Author:Prathamesh Deshmukh
Date: 2025-09-07

Description:
-----------
This script simulates the behavior of a one-dimensional chain of magnetic 
spins using a simplified Ising-like model. It demonstrates how an ordered 
magnetic state (like antiferromagnetism) transitions into a disordered 
paramagnetic state as thermal noise increases.

The net magnetization (represented by the 'Sum / Size') is plotted 
against the 'Noise Level,' which acts as an analog for temperature.

Methodology:
-----------
1.  An initial spin configuration is created (e.g., 'alternating' for an
    antiferromagnetic ground state).
2.  In each iteration, random noise is added to every spin in the chain,
    simulating thermal fluctuations. An external 'field' is also applied,
    which biases the spins in one direction.
3.  The total net magnetization of the system is calculated.
4.  The noise level is incrementally increased, and the process is repeated,
    plotting the net magnetization at each step.

Interpretation of the Plot:
---------------------------
The resulting plot shows the system's net magnetization as a function of
noise (temperature). For an antiferromagnetic starting state, the net 
magnetization should be near zero at low noise levels. As noise increases,
the spins flip more randomly, and the external field's influence becomes
more dominant, causing the net magnetization to rise towards the field
direction, simulating the transition to a paramagnetic phase.

Key Parameters:
---------------
- size: The number of spins in the 1D chain.
- initial_noise_level: The starting "temperature."
- field: Represents an external magnetic field.
- initial_list_type: The ground state of the spin system ('alternating' 
  for antiferromagnetic, 'ones' for ferromagnetic).

'''

import numpy as np
import matplotlib.pyplot as plt

def generate_noisy_list(size, noise_level, field, initial_list_type=None, existing_noisy_list=None):
    if existing_noisy_list is None:
        # Initialize with the specified initial list type
        if initial_list_type == 'ones':
            noisy_list = np.ones(size)
        elif initial_list_type == 'alternating':
            noisy_list = np.ones(size)
            noisy_list[1::2] = -1
        elif initial_list_type == 'zeros':
            noisy_list = np.zeros(size)
        elif initial_list_type == 'custom':
            noisy_list = [1, -0.5] * (size // 2) + [1] * (size % 2)
        else:
            raise ValueError("Invalid initial_list_type. Choose 'ones', 'alternating', 'zeros', or 'custom'.")
    else:
        # Increase randomness for existing noisy_list
        noisy_list = [np.clip(element - np.random.normal(0, noise_level * 2), -1, 1) if element == 1 else np.clip(element + np.random.normal(0, noise_level * 2), -1, 1) for element in existing_noisy_list]

    # Add constant positive noise (field)
    noisy_list = [element + field for element in noisy_list]
    
    return noisy_list

# Parameters
size = 5000
initial_noise_level = 0.1
increment_noise_level = 0.01
field = 0.1  # Adjust the strength of the constant positive noise
#Field =0.1 (Antiferromagetic) ,=0.5 Ferromagetic , 0.1 for Paramanetic 

iterations = 150  # Adjust the number of iterations

sums = []
noise_levels = []

initial_list_type = 'alternating'  # Choose 'ones', 'alternating', 'zeros', or 'custom'
existing_noisy_list = None

# Generate noisy lists for different noise levels
for i in range(iterations):
    noise_level = initial_noise_level + i * increment_noise_level  # Increase noise level slightly with each iteration
    noisy_list = generate_noisy_list(size, noise_level, field, initial_list_type, existing_noisy_list)
    existing_noisy_list = noisy_list  # Update existing noisy list for the next iteration
    
    # Clip each element in the noisy list
    noisy_list = np.clip(noisy_list, -1, 1)
    
    noisy_sum = sum(noisy_list)
    list_sum = noisy_sum / size  # Calculate the sum divided by size
    sums.append(list_sum)
    noise_levels.append(noise_level)

# Plotting
plt.plot(noise_levels, sums, marker='o')
plt.xlabel('Noise Level')
plt.ylabel('Sum of Noisy List / Size')
plt.title('Noise Level vs Sum of Noisy List / Size')
plt.show()
