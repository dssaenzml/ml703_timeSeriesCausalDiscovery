# Analysing Performance of Stocks using Causal Discovery

![alt text](https://mbzuai.ac.ae/application/themes/mbzuai/dist/images/mbzuai_logo.png)

Authors: Dhanalaxmi Gaddam*, Diego Saenz*, Rushali Grandhe*

![alt text](Causal-Learn/PC/pc_fisher_z_all_companies.png)

Stock prices data is considered by many as undecipherable and noisy due to its volatility and multi-variable interaction. There have been many attempts to understand stock market behaviour and reduce the uncertainty in their predictions. We aim to  analyse the influence and interaction amongst top performing companies' stock price and its social media exposure on Twitter. In specific, we are going to present results on any causal relation between companies' data if exists and discuss the relevance. To this end, several pre-processing transformations are applied on the data to suit the causal discovery algorithms'. Moreover, we explore how time series data can be modelled either with time-delayed or instantaneous assumptions. Our study shows that linear correlation could be translated to conditional dependence relations and causal graphs. This repo contains the code implementations for preprocessing data and causal discovery methods such as PC, FCI, GES and PCMCI.

# Dataset

[Tweets data](https://www.kaggle.com/omermetinn/tweets-about-the-top-companies-from-2015-to-2020)

[Stock price data](https://www.kaggle.com/omermetinn/values-of-top-nasdaq-copanies-from-2010-to-2020)

#  Installation steps for Causal-Learn (Pytrad) - PC,FCI, GES

```pip install causal-learn```

```pip install pygraphviz```

#  Installation steps for Tigramite - PCMCI

```pip install tigramite```


\* All authors contributed equally.

# Acknowledgements

[Causal-learn](https://github.com/cmu-phil/causal-learn)

[Tigramite](https://github.com/jakobrunge/tigramite/tree/master/tigramite)
