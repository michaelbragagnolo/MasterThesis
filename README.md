## Continual learning technologies for tiny ML
Repository that is intended to keep track of my thesis work and that contains all the reference material and the scripts developed to this end.

### Overleaf project
Draft of the final dissertation (ongoing): [Thesis-Overleaf project](https://www.overleaf.com/read/cxcxbjznmrxx)


### Description
Comprehensive research that compares the performance of different continuos learning algorithms on small images dataset for tinyML applications involving on-device, low-power image recognition and classification, and investigates (in a simulated scenario) the trade-offs between performance, storage, computational costs and memory footprint.

Main references | link         
---|---------------------
Avalanche library for CL | https://arxiv.org/abs/2104.00405
Performance of CL for embedded sensing applications | https://arxiv.org/abs/2110.13290
Online CL in Image Classification | https://arxiv.org/abs/2101.10423
CL in Single Incremental Task-Scenarios | https://arxiv.org/abs/1806.08568

In consequence of the *catastrophic forgetting* problem, enabling deep learning models to train continuously is extremely difficult in practice. Many approaches have been proposed but most of the existing CL techniques do not take into account the resource requirements, so it's unsure if they'd work in severly resource constrained devices, such as embedded systems.

For these reasons, to **further investigate whether an approach could be relevant to resource-constrained devices**, I'll start from the findings discussed in the aforementioned papers and, as main part of the work, try to complete a comprehensive survey and simulated comparison of these state of the art algorithms.

### Avalanche - end-to-end library for Continual Learning
ref: https://avalanche.continualai.org

Open-source end-to-end library for continual learning based on Pytorch, devised to ease the implementation, assessment and replication of continual learning algorithms across different settings.

#### Reproducibility of continual learning frameworks
ref: https://github.com/ContinualAI/reproducible-continual-learning

## Research objectives and methods
This thesis contributes to the study of different Continual Learning algorithms, focused on continual supervised learning for vision tasks, that could best suit resource-constrained devices.  
Through the development of some simulated experiments, **the goal** is to better understand the specific configuration needed to achieve optimal results in resource-constrained devices, which means in turn to play with different hyper-parameters and such.

### Action plan

#### 1. EXPERIMENT  
The very first step of this thesis-project is to **provide a set of experiments validating and reproducing existing works in continual learning.**
To guarantee fair implementations, I rely on the `Avalanche` library, developed and maintained by ContinualAI.  
> A critical design objective of Avalanche is in fact to allow experimental results to be seamlessly reproduced; continual learning algorithms today are often
designed and implemented from scratch with different assumptions, settings, and benchmarks that make them difficult to compare among each other or even port to slightly different contexts.

**Continuous Learning strategies:**  
Recently, a growing number of approaches have been presented on CL based on both variations of already existing and well known strategies or completely novel approaches with different degrees of success.  
Here I propose a list of experiments based on some of the most popular, yet interesting, CL techniques inspired by the state of the art.

In order to improve its performance or expand its set of capabilities, the target system powered by a continual learning strategy is required to learn from a non-stationary stream of experiences.  
The `benchmarks` are recipes that specify how this stream of data is created by defining the originating dataset and the contents of the stream.  
Benchmarks hereafter are (so far) based on reshaped versions of well-known datasets such as MNIST and CIFAR-100.

Technique | Benchmark | Implemented (Y/N)           
---|---------------------|-----
LwF | Split MNIST, Permuted MNIST | N
Elastic Weight Consolidation | Permuted MNIST | N 
iCaRL | Split CIFAR 100 | N 
Synaptic Intelligence | Split MNIST, Permuted MNIST | N       
CoPE | Split MNIST | N                      
GEM | Permuted MNIST, Split CIFAR 100 | N      
Average GEM | Permuted MNIST, Split CIFAR 100 | N      
GSS | Split MNIST | N          
     

#### 2. EVALUATE  
Given the fact that embedded systems are built for specific purposes and are optimized to meet different kind of constraints, such as memory, timing, power and cost, the performance of each **Continual Learning algorithm are to be evaluated by monitoring several aspects of the computation.**  
The `Evaluation` module of Avalanche offers a vast set of metrics to evaluate experiments, in particular the ones of main interest for this project are:  
&nbsp; - Accuracy  
&nbsp; - Loss  
&nbsp; - Catastrophic forgetting  
&nbsp; - Confusion matrix  
&nbsp; - Timing  
&nbsp; - Ram / Disk / CPU / GPU usage  

#### 3. LOG and DISPLAY RESULT
Logging tools are essential for **monitoring the activity of an ongoing experiment.**  
The `Logging` module of Avalanche is used to display each plugin metric during training and evaluation.
***
