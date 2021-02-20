# huichuanRecSys
a small implementation of recommend system
**项目特点：**

- 使用Tensorflow2.x进行复现；
- 每个模型都是相互独立的，不存在依赖关系（当然因为这也增加了很多重复工作）；
- 模型基本按照论文进行构建，实验尽量使用论文给出的的公共数据集；
- 模型都附有`README.md`，对于模型的训练使用有详细的介绍；
- 代码源文件参数、函数命名规范，并且带有标准的注释；


### 1. 召回模型（Top-K推荐）



|                         Paper\|Model                         |        Published in        |        Author         |
| :----------------------------------------------------------: | :------------------------: | :-------------------: |
| Matrix Factorization Techniques for Recommender Systems\|**[MF](MF)** | IEEE Computer Society,2009 | Koren\|Yahoo Research |
| BPR: Bayesian Personalized Ranking from Implicit Feedback\|**[MF-BPR](BPR)** |         UAI, 2009          |     Steﬀen Rendle     |
| Neural network-based Collaborative Filtering\|[**NCF**](NCF) |         WWW, 2017          |      Xiangnan He      |
| Self-Attentive Sequential Recommendation｜[**SASRec**](SASRec) |         ICDM, 2018         |         UCSD          |
| STAMP: Short-Term Attention/Memory Priority Model for Session-based Recommendation\| **[STAMP](STAMP)** |         KDD, 2018          |       Qiao Liu        |
| Personalized Top-N Sequential Recommendation via Convolutional Sequence Embedding｜[**Caser**](Caser) |         WSDM, 2018         |      Jiaxi Tang       |
| Next Item Recommendation with Self-Attentive Metric Learning\|[**AttRec**](AttRec) |        AAAAI, 2019         |      Shuai Zhang      |


### 2. 粗排模型（CTR预估）

|                         Paper｜Model                         | Published in |                            Author                            |
| :----------------------------------------------------------: | :----------: | :----------------------------------------------------------: |
|             Factorization Machines\|**[FM](FM)**             |  ICDM, 2010  |                        Steffen Rendle                        |
| Field-aware Factorization Machines for CTR Prediction｜[**FFM**](FFM) | RecSys, 2016 |                 Yuchin Juan｜Criteo Research                 |
| Wide & Deep Learning for Recommender Systems｜[**WDL**](WDL) |  DLRS, 2016  |                         Google Inc.                          |
| Deep Crossing: Web-Scale Modeling without Manually Crafted Combinatorial Features\|**[Deep Crossing](Deep_Crossing)** |  KDD, 2016   |                      Microsoft Research                      |
| Product-based Neural Networks for User Response Prediction\|[**PNN**](PNN) |  ICDM, 2016  |                Shanghai Jiao Tong University                 |
| Deep & Cross Network for Ad Click Predictions｜[**DCN**](DCN) | ADKDD, 2017  |               Stanford University｜Google Inc.               |
| Neural Factorization Machines for Sparse Predictive Analytics\|**[NFM](NFM)** | SIGIR, 2017  |                         Xiangnan He                          |
| Attentional Factorization Machines: Learning the Weight of Feature Interactions via Attention Networks\|**[AFM](AFM)** | IJCAI, 2017  |    Zhejiang University\|National University of Singapore     |
| DeepFM: A Factorization-Machine based Neural Network for CTR Prediction\|**[DeepFM](DeepFM)** | IJCAI, 2017  | Harbin Institute of Technology\|Noah’s Ark Research Lab, Huawei |
| xDeepFM: Combining Explicit and Implicit Feature Interactions for Recommender Systems\|**[xDeepFM](xDeepFM)** |  KDD, 2018   |        University of Science and Technology of China         |
| Deep Interest Network for Click-Through Rate Prediction\|**[DIN](DIN)** |  KDD, 2018   |                        Alibaba Group                         |
