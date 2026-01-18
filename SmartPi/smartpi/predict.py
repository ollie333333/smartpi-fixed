import numpy as np
try:
    from tensorflow import keras
except ImportError:
    keras = None

class SmartPiPredict:
    """Load and use a saved model."""
    def __init__(self, model_file):
        if keras is None:
            raise RuntimeError("TensorFlow not installed")
        self.model = keras.models.load_model(model_file)

    def predict(self, data):
        """Run prediction on new data."""
        data = np.array(data, dtype=float)
        return self.model.predict(data)
