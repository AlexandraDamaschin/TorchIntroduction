# First, import PyTorch
import torch


def activation(x):
    """ Sigmoid activation function

        Arguments
        ---------
        x: torch.Tensor
    """
    return 1 / (1 + torch.exp(-x))


### Generate some data
torch.manual_seed(7)  # Set the random seed so things are predictable

# Features are 5 random normal variables
features = torch.randn((1, 5))  # 1 row and 5 columns
# True weights for our data, random normal variables again
weights = torch.randn_like(features)
# and a true bias term
bias = torch.randn((1, 1))  # creates a single value
y = activation(torch.sum(features * weights) + bias)
y = activation((features * weights).sum() + bias)

# 1.Calculate the output of this network using the weights and bias tensors
y = activation(torch.mm(features, weights.view(5, 1)) + bias)

# Calculate the output of this network using matrix multiplication
### Generate some data
torch.manual_seed(7)  # Set the random seed so things are predictable

# Features are 3 random normal variables
features = torch.randn((1, 3))

# Define the size of each layer in our network
n_input = features.shape[1]  # Number of input units, must match number of input features
n_hidden = 2  # Number of hidden units
n_output = 1  # Number of output units

# Weights for inputs to hidden layer
W1 = torch.randn(n_input, n_hidden)
# Weights for hidden layer to output layer
W2 = torch.randn(n_hidden, n_output)

# and bias terms for hidden and output layers
B1 = torch.randn((1, n_hidden))
B2 = torch.randn((1, n_output))

# 2.Calculate the output for this multi-layer network using the weights W1 & W2, and the biases, B1 & B2.
h = activation(torch.mm(features, W1) + B1)
output = activation(torch.mm(h, W2) + B2)
print(output)
