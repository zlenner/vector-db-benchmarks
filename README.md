# vector-db-benchmarks

Compared Quadrant Cloud and Pinecone.

The results are in benchmark.txt, and the code used to generate the results in this repo. Hopefully simple enough to understand, starting from run.py.

The tests were done with vectors.npy, which is a dataset of 300,000 ada-002 embeddings (1536 dimensions). Not available to download as I don't want to end up with a massive egress bandwith bill.

## Conclusion

Quadrant is a little above thrice the storage (write) time, 60% percent the query time. Both seem to scale great.

I won't be responding to any issues or pull requests, take this repo is at it is.
