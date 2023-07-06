from termcolor import colored
from engines.Pinecone import Pinecone
from engines.Qdrant import Qdrant
from run_engine import run_engine

if __name__ == "__main__":
    print(colored("Pinecone S1:", None, None, ["bold"]))
    run_engine(Pinecone())

    print("\n-----\n")

    print(colored("Qdrant mmapped:", None, None, ["bold"]))
    run_engine(Qdrant())
