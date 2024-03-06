import numpy as np
import matplotlib.pyplot as plt

# Parameters and Initial Conditions
S = 10000  # Total storage capacity
file_size_mean = 50  # Mean file size
file_size_std = 10  # Standard deviation of file size
T_critical = 2000  # Critical threshold for system operation
creation_rate = 0.5  # Probability of file creation
deletion_rate = 0.5  # Probability of file deletion
steps = 200  # Simulation steps

# Initialize Variables
files = np.random.normal(file_size_mean, file_size_std, int(S / (file_size_mean + file_size_std))).astype(int)
T_load, T_access, T_save = [], [], []
T_fragment = 0  # Simulated time since last defragmentation
T_reassemble = 0  # Time taken for defragmentation process

# Simulation
for step in range(steps):
    # Simulate file operations
    if np.random.rand() < creation_rate:
        new_file_size = int(np.random.normal(file_size_mean, file_size_std))
        if sum(files) + new_file_size <= S:
            files = np.append(files, new_file_size)
    
    if np.random.rand() < deletion_rate and len(files) > 0:
        files = np.delete(files, np.random.randint(len(files)))
    
    # Simplified fragmentation calculation
    fragmentation_level = np.random.rand()  # Placeholder for a dynamic calculation
    
    # Update performance metrics based on fragmentation
    current_load_time = fragmentation_level * 1000
    current_access_time = fragmentation_level * 1200
    current_save_time = fragmentation_level * 800
    T_load.append(current_load_time)
    T_access.append(current_access_time)
    T_save.append(current_save_time)
    
    # Check for critical performance threshold
    if current_load_time > T_critical or current_access_time > T_critical or current_save_time > T_critical:
        T_fragment += 1
        if T_fragment >= 10:  # Simplified condition for defragmentation
            T_reassemble += 5  # Simulated time for defragmentation
            T_fragment = 0  # Reset fragmentation timer
            # Simulate defragmentation effect
            fragmentation_level *= 0.5  # Reduce fragmentation level as a simple effect of defragmentation

# Plotting Results
plt.figure(figsize=(12, 8))

# Performance Metrics
plt.plot(T_load, label='Load Time')
plt.plot(T_access, label='Access Time')
plt.plot(T_save, label='Save Time')
plt.axhline(y=T_critical, color='r', linestyle='--', label='Critical Threshold')

plt.title('File System Performance Metrics')
plt.legend()
plt.xlabel('Step')
plt.ylabel('Time')
plt.tight_layout()
plt.show()
