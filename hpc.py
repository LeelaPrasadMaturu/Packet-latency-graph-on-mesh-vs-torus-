import matplotlib.pyplot as plt

# Input the values manually
injection_rates_mesh = [0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.07]  # Include only those with values in mesh_avg
mesh_avg = [53.52, 68.5173, 189.388, 2612.26, 5976.71, 9311.2, 15044]

injection_rates_torus = [0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
torus_avg = [30.98, 30.9222, 31.1162, 31.1463, 31.2949, 31.0292, 31.1764, 31.1904, 31.2272, 31.255, 31.1764, 31.6715, 32.3689, 33.391, 35.3292, 40.4581, 61.984, 3322.75, 6138.99]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(injection_rates_mesh, mesh_avg, label='Mesh', marker='o')  # Plot Mesh values
plt.plot(injection_rates_torus, torus_avg, label='Torus', marker='s')  # Plot Torus values

# Add text annotations
# plt.text(0.03, 5000, "Mesh grows rapidly", fontsize=10, color="blue")  # Annotating Mesh behavior
plt.text(0.5, 9000, "Max compuation cycles : 50,000", fontsize=12, color="green") 

# Add labels, title, and legend
plt.xlabel("Injection Rates")
plt.ylabel("Average Latency")
plt.title("Injection Rates vs Latency (Dim_Order Routing, Uniform Traffic)")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()


