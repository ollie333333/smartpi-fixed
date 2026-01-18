import numpy as np
try:
    from tensorflow import keras
    from tensorflow.keras import layers
except ImportError:
    keras = None

class SmartPiModel:
    """Train and save a simple model."""
    def __init__(self, input_size=3):
        if keras is None:
            raise RuntimeError("TensorFlow not installed")
        self.model = keras.Sequential([
            layers.Dense(10, activation='relu', input_shape=(input_size,)),
            layers.Dense(1)
        ])
        self.model.compile(optimizer='adam', loss='mse')

    def train(self, x, y, epochs=500):
        """Train on sequences of numbers."""
        self.model.fit(np.array(x, dtype=float), np.array(y, dtype=float), epochs=epochs)
        print("Training complete!")

    def save(self, filename='smartpi_model.h5'):
        """Save the trained model."""
        self.model.save(filename)
        print(f"Model saved to {filename}")
