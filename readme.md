# MATH1222

This is a repo for the project of the course 
*MATH122: Introduction aux processus stochastiques*.

## Statement

The statement can be found [here](projet-math1222-2025.pdf). This project was done in groups of two.
The objective of the project was to model the mutations of ADN.

### Complementary informations

One of the usages of phylogenetic trees is to find relations between beings.

The first thing we need to model is the evolution of the ADN. 
We have a mutation when one of the nucleotide of the sequence changes over time.
We take in that the mutation is not influenced by the nucleotides and that it's without memory.

We can thus represent this with a Markov chain. We use the substitution model of Kimura.
We won't manipulate the markov chain of the whole sequence because there would be too many possibilities.
The chain is also reversible meaning the probability of doing one inversion is the same as doing the opposite.

Because we don't have the sequence of the nodes and the racine but only the leafs we need to use

$$P(s_1,\cdots,s_5\|T)=\sum_{s'_1, s'_2,\cdots} P(s_1, \cdots,s_5,s'_1,s'_2,\cdots,s'_{N-1}|T)$$

<span style="color:#FF0000">DEADLINE:</span> **09/05/2025**

