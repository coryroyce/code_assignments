# Approximate Nearest Neighbor Search

Demonstrate various Approximate Nearest Neighbor Search methods on image data of letters (EMNIST). See [Notebook](https://github.com/coryroyce/code_assignments/blob/main/211124_Approximate_Nearest_Neighbor_Search/Approximate_Nearest_Neighbors_Cory_Randolph.ipynb) for full code example that can be run in the browser with Colab.

## Summary of Results

Below are the results of each method and the index of the approximate match that was found:

|   LHS |   Exhaustive Search |   Product Quantization |   Trees and Graphs |   HNSW |
|------:|-------------------:|-----------------------:|-------------------:|-------:|
|     0 |                  0 |                      0 |                  0 |      0 |
|    61 |                 61 |                     61 |                 61 |     61 |
|    80 |                 80 |                     80 |                 80 |     80 |
|    94 |                 94 |                     94 |                 94 |     94 |
|  1016 |               1016 |                   1016 |               1016 |   1016 |

<br />

While all methods returned the same set of indices for similar vectors the it's important to not that during the process some methods would provide slightly different results based on the random state of the UMAP data reduction or the random state of the sampling method used to reduce the number of dimensions from 728 down to 100.

Another interesting result was how each method found a letter "K" that looked similar to an "A" (original search vector). See the below images for reference: 

Search Vector/Image             |  Mislabeled Result
:-------------------------:|:-------------------------:
![](https://github.com/coryroyce/code_assignments/blob/main/211124_Approximate_Nearest_Neighbor_Search/reference/image_original_search_vector_A.png)  |  ![](https://github.com/coryroyce/code_assignments/blob/main/211124_Approximate_Nearest_Neighbor_Search/reference/image_K.png)

## Methods Used
To demonstrate various Approximate Nearest Neighbor Search Methods, the notebook follows the below format:
1. Load EMNIST letter dataset
1. Reduce the dimensionality from 728 columns/pixels to 100 columns/pixels with [UMAP](https://github.com/lmcinnes/umap)
1. Apply Locality Sensitive Hashing (LHS) with [FAISS](https://github.com/facebookresearch/faiss) library
1. Apply Exhaustive Search with [FAISS](https://github.com/facebookresearch/faiss) library
1. Apply Product Quantization with [FAISS](https://github.com/facebookresearch/faiss) library
1. Apply Tree and Graph search methods with [ANNOY](https://github.com/spotify/annoy) library
1. Apply Hierarchical Navigable Small World Graphs (HNSW) with [NMSLIB](https://github.com/nmslib/nmslib) library
1. Summarize results

