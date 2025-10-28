# Import the modules
import network2
import mnist_loader
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

# Load the MNIST data
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

# Create a neural network with 784 inputs, 30 hidden neurons, 10 outputs
net = network2.Network([784, 30, 10])

# Train the network and CAPTURE the results
eval_cost, eval_accuracy, train_cost, train_accuracy = net.SGD(
    training_data, 
    30,              # epochs
    10,              # mini_batch_size
    0.5,             # learning rate
    lmbda=5.0,       # regularization
    evaluation_data=validation_data,
    monitor_evaluation_cost=True,
    monitor_evaluation_accuracy=True,
    monitor_training_cost=True,
    monitor_training_accuracy=True
)

# Create a directory for your figures
output_dir = '../my_figures'
os.makedirs(output_dir, exist_ok=True)

# Create timestamped filename prefix
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# NOW create figures
epochs = range(30)

# Figure 1: Accuracy over time
plt.figure(figsize=(10, 6))
plt.plot(epochs, eval_accuracy, 'b-', label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy (out of 10000)')
plt.title('Network Accuracy Over Training')
plt.legend()
plt.grid(True)
accuracy_file = f'{output_dir}/{timestamp}_accuracy_plot.png'
plt.savefig(accuracy_file, dpi=300, bbox_inches='tight')
plt.show()

# Figure 2: Cost over time
plt.figure(figsize=(10, 6))
plt.plot(epochs, train_cost, 'r-', label='Training Cost')
plt.plot(epochs, eval_cost, 'b-', label='Validation Cost')
plt.xlabel('Epoch')
plt.ylabel('Cost')
plt.title('Training vs Validation Cost')
plt.legend()
plt.grid(True)
cost_file = f'{output_dir}/{timestamp}_cost_plot.png'
plt.savefig(cost_file, dpi=300, bbox_inches='tight')
plt.show()

print(f"\nFinal validation accuracy: {eval_accuracy[-1]}/10000")
print(f"Figures saved to: {output_dir}/")
print(f"  - {timestamp}_accuracy_plot.png")
print(f"  - {timestamp}_cost_plot.png")