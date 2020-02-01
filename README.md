# keiba-BTmodel

The Bradley–Terry model is a probability model that can predict the outcome of a paired comparison. Given a pair of individuals i and j drawn from some population,
it estimates the probability that the pairwise comparison i > j turns out true, as

<img width="187" alt="スクリーンショット 2020-01-31 23 23 10" src="https://user-images.githubusercontent.com/36298285/73546512-b4eaa280-4480-11ea-8c7b-d081d6e4abf8.png">

where pi is a positive real-valued score assigned to individual i. The comparison i > j can be read as "i is preferred to j", "i ranks higher than j", or "i beats j", depending on the application.
For example, pi may represent the skill of a team in a sports tournament, estimated from the number of times i has won a match. 
P(i>j) then represents the probability that i will win a match against j. 
Another example used to explain the model's purpose is that of scoring products in a certain category by quality. 
While it's hard for a person to draft a direct ranking of (many) brands of wine, it may be feasible to compare a sample of pairs of wines and say, for each pair, which one is better. 
The Bradley–Terry model can then be used to derive a full ranking. by [wikipedia](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model)
