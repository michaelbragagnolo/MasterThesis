## Continual learning technologies for tiny ML
Repository that contains all the reference material and the scripts developed for the practical part of my Master thesis.

### Description: ###
Comprehensive research that compares the performance of different continuos learning algorithms on small datasets for tinyML applications involving on-device, low-power image recognition and classification, and experiments a few techniques to help improving the training efficiency during the incremental learning phase.

Main reference: https://arxiv.org/abs/2110.13290

In consequence of the *catastrophic forgetting* problem, enabling deep learning models to train continuously is extremely difficult in practice. Many approaches have been proposed but most of the existing CL techniques do not take into account the resource requirements, so it's unsure if they'd work in severly resource constrained devices, such as embedded systems. 

For these reasons, to further investigate whether an approach could be relevant to resource-constrained devices, I'll start from the findings discussed in the aforementioned paper and, as suggested by the authors, try to **improve the training efficiency** (in a simulated scenario) in terms of computational costs, memory footprints and latency using:
  a. **Quantization** using 16 or 8-bit floating point representation
  b. **Mixed Precision Training**

***
