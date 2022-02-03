from torch import nn

# Class used to define NN model
# Multilayer perceptron model (feedforward network)
class MLP(nn.Module):
    # flatten the input image
    # linear layers (fully connected)
    # dropout and activation function
    def __init__(self, input_size=28 * 28, hidden_size=256, hidden_layers=2,
                 output_size=10, drop_rate=0, relu_act=True):
        super().__init__()
        self._input_size = input_size

        layers = nn.Sequential(*(nn.Linear(input_size, hidden_size),                # weighted sum of the inputs
                                 nn.ReLU(inplace=True) if relu_act else nn.Tanh(),  # apply ReLU activation function elementwise (or hyperbolic tan)
                                 nn.Dropout(p=drop_rate)))  # Dropout rate (randomly selected neurons ignored during training)
        for layer_idx in range(hidden_layers - 1):
            layers.add_module(f"fc{layer_idx + 1}",
                              nn.Sequential(*(nn.Linear(hidden_size, hidden_size),
                              nn.ReLU(inplace=True) if relu_act else nn.Tanh(),
                              nn.Dropout(p=drop_rate))))

        self.features = nn.Sequential(*layers)                  # holds output of the model w/o last classification model
        self.classifier = nn.Linear(hidden_size, output_size)   # feedforward network

    # Define how to forward propagate input through the defined layers
    def forward(self, x): # [batch size, height, width]
        x = x.contiguous()
        x = x.view(x.size(0), self._input_size)
        x = self.features(x)
        x = self.classifier(x)
        return x


__all__ = ['MLP']
