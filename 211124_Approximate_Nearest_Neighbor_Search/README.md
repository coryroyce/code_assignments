# Approximate Nearest Neighbor Search

Demonstrate various Approximate Nearest Neighbor Search methods on image data of letters (EMNIST).

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

Search Vector/Image             |  Mislabeled Result
:-------------------------:|:-------------------------:
![](https://github.com/coryroyce/code_assignments/blob/main/211124_Approximate_Nearest_Neighbor_Search/reference/image_original_search_vector_A.png)  |  ![](https://github.com/coryroyce/code_assignments/blob/main/211124_Approximate_Nearest_Neighbor_Search/reference/image_K.png)



<img src="https://github.com/coryroyce/code_assignments/blob/main/211124_Approximate_Nearest_Neighbor_Search/reference/image_original_search_vector_A.png">

<br />

<img src="https://github.com/coryroyce/code_assignments/blob/main/211124_Approximate_Nearest_Neighbor_Search/reference/image_K.png">

Another interesting result was how each method found a letter "K" that looked similar to an "A" (original search vector). See the below images for reference: 




<br /> <br /> <br />
