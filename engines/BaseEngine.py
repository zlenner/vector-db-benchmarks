import numpy

class BaseEngine:
    def __init__(self):
        self.number_of_results = 10
    
    def save_vectors(self, vectors: numpy.ndarray):
        raise NotImplementedError

    def query_vectors(self, vector: numpy.ndarray):
        raise NotImplementedError
