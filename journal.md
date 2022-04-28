# February 2, 2022

Today I have begun conducting a literature review, which I would like to use to be able to make more concrete
the specific goals of my project, refine my abstract, and be able to construct some sort of an outline of steps
that would be needed so I can give myself a proper timeline for the project.

Here are some of the links to the papers I have been reading:

* https://ftp.cs.ucla.edu/pub/stat_ser/r451-reprint.pdf
* https://www.pnas.org/content/108/42/17296
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1239917/
* https://pubs.acs.org/doi/pdf/10.1021/acs.est.1c02204
* https://journals.ametsoc.org/view/journals/clim/25/17/jcli-d-11-00387.1.xml
* https://www.nature.com/articles/s41467-020-15195-y.pdf
* https://ftp.cs.ucla.edu/pub/stat_ser/r481-reprint.pdf
* https://arxiv.org/pdf/1605.09370.pdf
* https://arxiv.org/pdf/2104.04008.pdf
* https://dl.acm.org/doi/pdf/10.1145/3397269
* https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2017GL075888
* https://iopscience.iop.org/article/10.1088/1748-9326/aba3d4/meta
* https://wcd.copernicus.org/articles/1/313/2020/wcd-1-313-2020.html#&gid=1&pid=1
* https://assets.researchsquare.com/files/rs-1068304/v1_covered.pdf?c=1641935495


# February 11, 2022

Last week I read over several papers, mostly the ones listed above plus a couple more recent ones that are to be added, and began to construct a prelimiary outline. I am finishing up some notes on those papers as well. I will aim to publish a more polished problem statement, with inputs, outputs, and outline by early next week.

# February 16, 2022

The paper listing has been updated. This week has been a rather busy one for me so I do not have much in the way of updates.

# February 20, 2022

Problem Statement: We want to determine a quantified degree of attribution that humans have had on the last two Atlantic hurricane seasons, some of the most active in history. We can use counterfactual causal inference theory in order to deem this, provided we can acquire the appropriate data. In order to come up with the "counterfactual" side of the data to attempt an evaluation, we can use simulation software and modelling such as FLOR by allow us to tinker with some of the atmospheric signals of climate change. The factual data to provide the intensity of the actual hurricane seasons is readily present. 

Input: Data representing key statistics to inform of the overall intensity of the 2020 and 2021 Atlantic Hurricane seasons, such as ACE, as well as model simulated data from AOML to represent hurricane seasons with lesser degrees of climate change

Output: Degree of attribution anthropogenic climate change claims for these hurricane seasons.


Rough Outline:

March 5 - Complete formalization of methodology of inference process, may try to make novel method that builds on top of methods I have read in papers in addition to what I have learned in class. Also, upload abstract.

March 21 - Complete usage and training of simulation software to generate desired counterfactual output of choice (the factual data is already present and available)

March 30 - Run full counterfactual analysis and consider trying alternate/refining methodology if needed

April 15 - Extra time to re-run experiments, make adjustments, etc, Complete video.

May 1 (?) - Complete paper. 

# March 2, 2022

Updated and uploaded the abstract, got responses from contacts in aerosols and climate research regarding simulation software suggestions for my intended use case, looked a bit into NCAR's MPAS and FLOR's GFDL. Starting to write down and compile notes of the methodologies from papers and math behind them to start trying to form my own.

# March 5, 2022

Here is my revised list of literature sources that are being combed:

## 2022-03-07 check in: alp

Looking solid. Would encourage you to try out existing methods and get some initial simulations before exploring novel approaches.

## Paper Categories

### Counterfactual Causal Analysis and Climate Effects
* https://ftp.cs.ucla.edu/pub/stat_ser/r451-reprint.pdf
* https://www.pnas.org/doi/10.1073/pnas.1104268108
* https://arxiv.org/pdf/2104.04008.pdf
* https://assets.researchsquare.com/files/rs-1068304/v1_covered.pdf?c=1641935495
* https://www.science.org/doi/full/10.1126/sciadv.aaw9253
* https://iopscience.iop.org/article/10.1088/1748-9326/aa9ef2
* https://cpb-us-e1.wpmucdn.com/you.stonybrook.edu/dist/4/945/files/2018/09/climate_change_Florence_0911201800Z_final-262u19i.pdf

### Hurricanes and Climate Change Connection Studies
* https://climatemodeling.science.energy.gov/presentations/climate-change-attribution-extreme-rainfall-throughout-hurricane-season
* https://www.gfdl.noaa.gov/global-warming-and-hurricanes/
* https://www.climatesignals.org/events/atlantic-hurricane-season-2020
* https://www.gfdl.noaa.gov/bibliography/related_files/tk0401.pdf
* https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2006GL026869
* https://link.springer.com/article/10.1007/s00382-013-1713-0

### Non-(Pearl Causal) General Climate Phenomena Attribution Studies
* https://pubs.acs.org/doi/pdf/10.1021/acs.est.1c02204
* https://www.nature.com/articles/s41467-020-15195-y.pdf
* https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2017GL075888
* https://wcd.copernicus.org/preprints/wcd-2021-64/wcd-2021-64.pdf
* https://ascmo.copernicus.org/articles/6/177/2020/
* https://www.worldweatherattribution.org/pathways-and-pitfalls-in-extreme-event-attribution/
* https://www.cell.com/one-earth/fulltext/S2590-3322(20)30247-5

### Non Counterfactual Climate Change Causal Analysis
* https://journals.ametsoc.org/view/journals/clim/25/17/jcli-d-11-00387.1.xml
* https://arxiv.org/pdf/1605.09370.pdf
* https://iopscience.iop.org/article/10.1088/1748-9326/aba3d4/meta
* https://wcd.copernicus.org/articles/1/313/2020/wcd-1-313-2020.html#&gid=1&pid=1

### General Causal Inference and Counterfactual Analysis
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1239917/
* https://ftp.cs.ucla.edu/pub/stat_ser/r481-reprint.pdf
* https://dl.acm.org/doi/pdf/10.1145/3397269


I have also uploaded the datasets and plots of some metrics for the factual world.

# March 14, 2022

I have been able to acquire some data regarding simulations done using aforementioned simulation softwa re, as actual usage of them requires supercomputing power far beyond the scope of what is offered through GCP or my research group even.

# March 20,2022
I have compiled several current methodologies to try in regards to the counterfactual analysis of data. I will work on seeing how I can coalescing the data I have and doing some data processing to get it into a useable form. I will complete the uploading of my revised literature sources as well as methodology notes next week, seeing as I have many other deadlines this week I need to get past first before refocusing on this project.

# March 29,2022

I have done some initial data anaylsis of the distributions of my data and the counterfactual data as well.

# April 3, 2022

I have used time series forecasting and several regression techniques to come up with a couple possible possible sets of values for the counterfactual values of my current features

# April 11, 2022
I have spent some time experimenting with using AutoML, considering predictions on the yearly and monthly scales, considering using PCA and LLE, a water mask to make sure I am only using sea locations for predictions, etc.

# April 12, 2022
I have spent some time writing up a CNN as an alternative to the LGBM AutoML suggested.

# April 13, 2022
I have spent some time developing the necessary distribution to model my problem in the same vein as the Hannart/Pearl paper to generate a result about the attribution!

# April 15, 2022
I have worked on uploading a video with my current progress!

# April 24, 2022
I have made some simplifications and alterations to my time series regression forecasting strategy. I have also located the factual simulations from the same source as my counterfactual ones, to use as well.
