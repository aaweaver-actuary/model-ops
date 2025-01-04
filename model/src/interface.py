from abc import ABC, abstractmethod


class ModelInterface(ABC):
    """Abstract Base Class to define the required interface for all models."""

    @abstractmethod
    def load_model(self, model_path: str):
        """Load the model from the given path."""

    @abstractmethod
    def predict(self, input_data: dict) -> dict:
        """Perform inference on the input data and return the result."""
