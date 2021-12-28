## Continual learning technologies for tiny ML
Repository that is intended to keep track of my thesis work and that contains all the reference material and the scripts developed to this end.

### Overleaf link
Draft of the written report:
https://www.overleaf.com/read/cxcxbjznmrxx

### Description: ###
Comprehensive research that compares the performance of different continuos learning algorithms on small images dataset for tinyML applications involving on-device, low-power image recognition and classification, and investigates (in a simulated scenario) the trade-offs between performance, storage, computational costs and memory footprint.

> Main references:
- Avalanche library for CL: https://arxiv.org/abs/2104.00405
- Performance of CL for embedded sensing applications: https://arxiv.org/abs/2110.13290
- Online CL in Image Classification: https://arxiv.org/abs/2101.10423

In consequence of the *catastrophic forgetting* problem, enabling deep learning models to train continuously is extremely difficult in practice. Many approaches have been proposed but most of the existing CL techniques do not take into account the resource requirements, so it's unsure if they'd work in severly resource constrained devices, such as embedded systems.

For these reasons, to **further investigate whether an approach could be relevant to resource-constrained devices**, I'll start from the findings discussed in the aforementioned papers and, as main part of the work, try to complete a comprehensive survey and simulated comparison of these state-of-art algorithms.

### Avalanche - end-to-end library for Continual Learning
ref: https://avalanche.continualai.org
Open-source end-to-end library for continual learning based on Pytorch, devised to ease the implementation, assessment and replication of continual learning algorithms across different settings.


***
