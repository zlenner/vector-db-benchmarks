import time
import numpy
from data.get_test_query_data import get_test_query_data
from data.load_vectors import load_vectors
from engines.BaseEngine import BaseEngine

def run_engine(engine: BaseEngine):
    vectors = load_vectors()
    test_data = get_test_query_data()

    step = len(vectors) // 10
    for offset in range(0, len(vectors), step):
        print(f"{offset}-{offset+step}")
        
        vector_slice = vectors[offset:offset+step]

        start = time.time()
        
        engine.save_vectors(vector_slice, ids=[i for i in range(offset, offset+step)])

        print(f"Storage time (avg): {(time.time() - start) / len(vector_slice)}")

        test_data_vectors = [numpy.array(vector) for _, _, vector in test_data]
        
        start = time.time()
        for vector in test_data_vectors:
            engine.query_vectors(vector)
        
        print(f"Query time (avg): {(time.time() - start) / len(test_data)}")

        print("")