# Project3RandomForestML

Repository to project 3 in the BERN01 computational science course, HT23 at Lund university. Note that to run the code you need to add the Project_datasets folder locally.

# TODO
- Questions 3,4: Theo, Anna
  - Recall and precision do not work as intended in 4
  - It would be nice to have a function that given a region (in the format of region_test / region_train) plots statistics for this region, a map of this region (That one is for Carmen), the distribution of biomes in this region, perhaps a climate graph, etc. Essentially a localised version of the statistical evaluation done in part 2. A lot of the nice plots in part 2 could then be produced with a call of this function with the whole world as the region. This function could then be used in parts 3 and 4 to understand our testing and training regions better.
  - Does the section 'Plot Impurity-based vs. Permutation importance' have performance issues?
  - Improve performance of the hyperparameter fitting in 4.3
  - Automatic plot and table generation: export plots and tables automatically to '../plots/experimentName_plotName.pdf' and '../plots/experimentName_tableName.tex'
  - Improve prediction accuracy in 4
- implementing Plotting of world map: Carmen
- reading in data: everybody
- plotting and statistical evaluation of the data: everybody
- plotting and statistical evaluation of the random tree: Carmen


# Commands to install the packages under anaconda
    > conda install numba scipy scikit-learn matplotlib shap graphviz seaborn statistics IPython
    > pip install ISLP graphviz

# Important pages
For model evaluation: binary classification. Common metrics include accuracy, precision, recall, and confusion matrix.

https://scikit-learn.org/stable/modules/model_evaluation.html#:~:text=In%20multilabel%20classification%2C%20the%20function,1.0%3B%20otherwise%20it%20is%200.0.

