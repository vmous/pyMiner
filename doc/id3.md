# Iterative Dichotomiser 3 - ID3
[ID3](http://en.wikipedia.org/wiki/ID3_algorithm) is an algorithm invented by [Ross Quinlan](http://en.wikipedia.org/wiki/Ross_Quinlan) for building learning systems by inductive inference from examples. The application domain of such systems, though not limited to any particular area of intellectual activity, all address classification problems. Aquired knowledge (classification rules) is represented as decision trees and the underlying strategy for this aquisition is non-incremental learning from examples (in this context, "non-incremental" means that the produced tree is not bound to the particular order in which the training examples are given). ID3 is the precursor of C4.5 algorithm.

## Design
The algorithm is designed for cases where there are many attributes and the training set contains many objects but a reasonably good decision tree is required without much computation. It has been found to produce simple decision trees but does not guarantee to find the best.

## Algorithm
The basic structure of ID3 is iterative. Using a randomly selected subset of the training set, called window, a decision tree is built. Then it is checked whether it can correctly classify the rest of the examples in the training set and if it can, the process terminates. If not, a selection of the incorrectly classified examples is added to the window and the process continues. Empirical evidence suggests that a correct decision tree is usually found more quickly using this iterative process than building the tree using the entire training set.

The choice of tests (branching) is very important if the ultimate goal is to create a simple tree. We restrict branching on the values of an attribute thus the choice boils down to selecting the attribute for the root of the tree (or subtree). ID3 adopts an information based method that depends on two assumptions. Let C contain p objects of class P and n objects of class N:
* Any correct decision tree will classify objects in the same proportion as their representation in C. An arbitrary object will be classified in P with probability p/(p+n) or in N with probability n/(p+n).
* When a decision tree is used to classify an object it returns a class. Thus, a decision tree can be regarded as a source of a message 'P' or 'N', with the expected information needed to generate this message given by:

  ![I(p,n)=-\frac{p}{p+n}log_2\frac{p}{p+n}-\frac{n}{p+n}log_2\frac{n}{p+n}](http://latex.codecogs.com/gif.latex?I%28p%2Cn%29%3D-%5Cfrac%7Bp%7D%7Bp%2Bn%7Dlog_2%5Cfrac%7Bp%7D%7Bp%2Bn%7D-%5Cfrac%7Bn%7D%7Bp%2Bn%7Dlog_2%5Cfrac%7Bn%7D%7Bp%2Bn%7D)

Assuming an attribute A with values {A1, A2, ..., Aν} is used for the root of the decision tree it will partition C in {C1, C2,..., Cν} where Ci will contain those objects in C that have value Ai of A. Let Ci contain pi objects of class P and ni objects of class N. The expected information required for the subtree for Ci is then I(pi, ni). The expected information required for the tree with A as root is then obtained as a weighted average:

![E(A)=\sum_{i=1}^{\nu}\frac{p_i+n_i}{p+n}I(p_i,n_i)](http://latex.codecogs.com/gif.latex?E%28A%29%3D%5Csum_%7Bi%3D1%7D%5E%7B%5Cnu%7D%5Cfrac%7Bp_i%2Bn_i%7D%7Bp%2Bn%7DI%28p_i%2Cn_i%29)

, where the weight for the ith branch is the proportion of objects in C that belong to Ci. The information gained by branching on A is therefore:

![gain(A)=I(p,n)-E(A)](http://latex.codecogs.com/gif.latex?gain%28A%29%3DI%28p%2Cn%29-E%28A%29)

An intutitive rule would then be to choose the attribute to branch on which gains the most information (since I(p,n) is constant for all attrbutes, maximizing the gain is equivalent to minimizing E(A), which is the mutual information of the attribute A and the class). ID3 examines all candidate attributes and chooses A to maximize gain(A), forms the tree, and then continues recursively to form decision trees for the residual subsets C1, C2, ..., Cν.

### Complexity
At each non-leaf node of the decision tree, the gain of each attribute A must be determined. This gain in turn is based on pi and ni for each value Ai of A, so every object in C must be examined to determine its class and its value of A. Concequently, at each node, the computational complexity of the procedure is O(|C|*|A|). ID3's total computational requirement per iteration is thus proportional to the product of the size of the training set, the number of the attributes and the number of non-leaf nodes in the decision tree. The same relationship appears to extend to the entire induction process, even when several iteration are performed. No exponential growth in time or space has been observed as the dimensions of the induction task increase, so the technique can be applied to large tasks.

## Noise
Non-systematic errors in either the values of the attributes or class information are usually referred to as noise. The following two modifications are required if the tree building algorithm is to be able to operate with a noise-affected training set:

1. The algorithm must be able to work with inadequate attributes, because noise can cause even the most comprehensive set of attributes to appear inadequate.
2. The algorithm must be able to decide that testing further attributes will not improve the predictive accuracy of the decision tree.

   Let C be the collection of objects containing representatives of both classes and let A be an attribute with random values that produces subsets {C1, C2, ..., Cν}. Unless the proportion of class P objects is exactly the same as the proportion of P objects in each of class P objects in C itself, branching on attribute A will give an apparent information gain. It will therefore appear that testing on attribute A is a reasonable choise, even though the values of A are random and cannot help to classify the objects in C. A solutions to the dilemma is based on the [chi-square test](https://en.wikipedia.org/wiki/Chi-squared_test) for stohastic independence.

   More specifically, suppose attribute A produces subsets {C1, C2, ..., Cν} of C, where Ci contains pi and ni objects of class P and N, respectively. If the value of A is irrelevant to the class of an object in C, the value p'i of pi should be:

   ![p'_i=p\cdot\frac{p_i+n_i}{p+n}](http://latex.codecogs.com/gif.latex?p%27_i%3Dp%5Ccdot%5Cfrac%7Bp_i%2Bn_i%7D%7Bp%2Bn%7D)

   If n'i is the corresponding expected value of ni, the statistic:

   ![\sum_{i=1}^{\nu}\frac{(p_i-p'_i)^{2}}{p'_i}+\frac{(n_i-n'_i)^{2}}{n'_i}](http://latex.codecogs.com/gif.latex?%5Csum_%7Bi%3D1%7D%5E%7B%5Cnu%7D%5Cfrac%7B%28p_i-p%27_i%29%5E%7B2%7D%7D%7Bp%27_i%7D%2B%5Cfrac%7B%28n_i-n%27_i%29%5E%7B2%7D%7D%7Bn%27_i%7D)

   is approximately chi-square with ν-1 degrees of freedom. Provided that non of the p'i and n'i are very small, this statistic can be used to determine the confidence with which one can reject the hypothesis that A is independent of the class of objects in C. The tree-building process can thus be modified to prevent testing any attribute whose irrelevance cannot be rejected with enough high confidence (e.g., 99%). 
