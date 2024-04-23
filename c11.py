import matplotlib.pyplot as plt

# Sample data
nodes = [100, 200, 300, 400, 500]
throughput = [50, 75, 100, 125, 150]

# Plot the curve
plt.plot(nodes, throughput, marker='o')

# Add labels and title
plt.xlabel('Number of Nodes')
plt.ylabel('Throughput (Mbps)')
plt.title('Throughput vs. Number of Nodes')

# Display the curve
plt.show()
