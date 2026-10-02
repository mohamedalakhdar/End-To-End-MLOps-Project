from abc import ABC, abstractmethod


class BaseMLModel(ABC):
    @abstractmethod
    def predict(self):
        pass
