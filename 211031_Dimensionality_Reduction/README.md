# Dimensionality Reduction

Cory Randolph
10/29/2021

This Notebook demonstrates various dimensionality reduction processes:
- PCA
- SVD
- LLE
- t-SNE
- ISOMAP
- UMAP

It is organized into two section, one with an image data set (EMNIST) and one with tabular data (Iris Dataset).

## Image Data Notes
The main observations come reviewing the plotted data for each method with 2 components.
PCA, SVD have similar graphs where the separation of categories is not very distinct.
LLE has a very different looking graph which contains spikes in different directions, but 
at least the spike have the same color implying that the particular letter/label was recognized.
t-SNE and UMAP seem to have the best category distinctions where groups of different colors/labels 
can be seen together.
ISOMAP stands out in that the groups are less defined but at least the colors are in the same general area.

One last observation comes from the amount of components that were needed to capture most (~95%) of the
data. While this notebook only demonstrates the cumulative explained variance for the PCA method, it
is interesting to note that at around 200 principle components 95% of the information is captured. This
means that we could use this as an image compression or noise reduction technique for the EMNIST dataset.


## Tabular Data
In the tabular dataset PCA and SVD again have very similar graphs, which make sense because the 
underlying decomposition process is very similar between the two methods.
LLE's graph is the most unique again in that the majority of the plots look like they were embeds into
a single line (probably to due with the "Linear" aspect of the algorithm.)
ISOMAP had an interesting curve fit to the graph of clusters, but the separation is still very good.
t-SNE and UMAP had very good graphs with tight clusters and good distance between the clusters showing 
that it had correctly extracted the main features with just 2 components.


## Notes
Additional work could be done to explore slowly increasing the number of components in the image dataset 
to find out where each method demonstrates further strengths.
Also, applications of these dimensionality reduction techniques on the EMNIST data will apply to future
classification algorithms and analysis.