import dotenv
dotenv.load_dotenv()
import os
import pinecone
import numpy
from engines.BaseEngine import BaseEngine

class Pinecone(BaseEngine):
    def __init__(self):
        super().__init__()
        variables: dict[str, str] = {}
        for env_var in ["PINECONE_API_KEY", "PINECONE_ENVIRONMENT", "PINECONE_INDEX_NAME"]:
            if env_var is None:
                raise Exception("Missing environment variable: " + env_var)
            variables[env_var] = os.environ[env_var]

        pinecone.init(
            api_key=variables["PINECONE_API_KEY"],
            environment=variables["PINECONE_ENVIRONMENT"],
            name=variables["PINECONE_INDEX_NAME"]
        )

        self.index = pinecone.Index(variables["PINECONE_INDEX_NAME"])
    
    def save_vectors(self, vectors: numpy.ndarray):
        upsert_rows: list[tuple[str, list[float]]] = []
        for i, vector in enumerate(vectors):
            upsert_rows.append((str(i), vector.tolist()))

        self.index.upsert(upsert_rows, batch_size=100)
    
    def query_vectors(self, vector: numpy.ndarray):
        return self.index.query(vector.tolist(), top_k=self.number_of_results)
    
