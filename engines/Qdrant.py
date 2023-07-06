import dotenv
dotenv.load_dotenv()
import os
import numpy
from engines.BaseEngine import BaseEngine
from qdrant_client import QdrantClient, models

class Qdrant(BaseEngine):
    def __init__(self):
        super().__init__()
        variables: dict[str, str] = {}
        for env_var in ["QDRANT_URL", "QDRANT_API_KEY"]:
            if env_var is None:
                raise Exception("Missing environment variable: " + env_var)
            variables[env_var] = os.environ[env_var]


        self.qdrant_client = QdrantClient(
            url=variables["QDRANT_URL"], 
            api_key=variables["QDRANT_API_KEY"]
        )
        self.collection_name = "benchmark"
        self.qdrant_client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
        )

    
    def save_vectors(self, vectors: numpy.ndarray):
        # Define batch size
        batch_size = 100

        # Generate batches
        num_batches = numpy.ceil(len(vectors) / batch_size).astype(int)
        batches = numpy.array_split(vectors, num_batches)

        # Process each batch
        for batch_num, batch in enumerate(batches):
            self.qdrant_client.upsert(
                collection_name=self.collection_name,
                points=[
                    models.PointStruct(
                        id=i + batch_num * batch_size,  # Adjust ID for batch offset
                        vector=vector.tolist()
                    )
                    for i, vector in enumerate(batch)
                ]
            )
            print(f"Inserted batch {batch_num + 1}/{num_batches}")
    
    def query_vectors(self, vector: numpy.ndarray):
        hits = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            limit=self.number_of_results
        )
        return hits
    
