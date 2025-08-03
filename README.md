# AdaSemb: An Adaptive Knowledge-Driven Deep Learning Framework Integrating Cancer Protein Assemblies for Predicting PI3Kα Inhibitor Response and Resistance

Protein kinases regulate diverse cellular functions, including cell cycle progression, metabolism, differentiation, and survival, with their dysregulation implicated in multiple carcinogenic processes. Phosphatidylinositol 3-kinase alpha inhibitors (PI3Kαis) have revolutionized breast cancer treatment, but acquired resistance remains a major clinical challenge, with around 40% of patients experiencing progression within 4-6 months. Current drug response prediction (DRP) methods typically rely on individual pathways or biomarkers, limiting their ability to capture complex cancer-specific molecular interactions and predict resistance mechanisms. To overcome these limitations, we present AdaSemb, an adaptive, knowledge-driven deep learning framework that uses a multi-protein assembly map to predict responses and resistance to PI3Kαi. AdaSemb comprises two modules: the AdaSemb-PA module incorporates tumor genomic variations into a biological structural neural network. In contrast, the AdaSemb-DRP module uses conditional domain adversarial networks (CDAN) to enhance gene-drug distribution generalization. By combining genomic data with drug molecular structures, AdaSemb identifies critical protein combinations linked to drug resistance. In validation with 1244 cancer cell lines and patient-derived xenografts (PDX), AdaSemb outperformed existing DRP models. In a cohort of 116 breast cancer patients from TCGA, it predicted significantly longer survival for sensitive patients, surpassing traditional biomarkers in accuracy. Furthermore, we identified seven key assemblages that integrate mutations from 93 genes, which distinguish alpelisib-sensitive and -resistant cell lines. These results are applicable to breast cancer patient samples and PDX models, demonstrating AdaSemb’s significant clinical potential in personalized treatment and prediction of resistance for breast cancer.
![Model Image](model/model.png)

## The environment of AdaTrans
```
cudatoolkit=11.1
torchaudio=0.8.0=py37
torchvision=0.9.0=py37_cu111
optuna
python=3.7
pytorch=1.8.0=py3.7_cuda11.1_cudnn8.0.5_0
scikit-learn
networkx
pandas

```

## Dataset description
The datasets used in this study are all publicly available. GDSC version 1: https://www.cancerrxgene.org/downloads/bulk_download; 
GDSC version 2: https://www.cancerrxgene.org/downloads/bulk_download; 
CTRP version 1: https://portals.broadinstitute.org/ctrp.v1/; 
CTRP version 2: https://portals.broadinstitute.org/ctrp.v2.1/; 


## Run the moedel  in a GPU server, execute the following:
```sh
python predict.py   -gene2id gene2ind.txt
                    -cell2id cell2ind.txt
                    -mutations cell2mutation.txt
                    -cn_deletions cell2cndeletion.txt
                    -cn_amplifications cell2amplification.txt
                    -predict test_data.txt
                    -hidden <path_to_directory_to_store_hidden_values>
                    -result <path_to_directory_to_store_prediction_results>
                    -load <path_to_model_file>
                    -std <path to standarization file >
                    -cuda <GPU_unit_to_use>
                    -batchsize 100 (or any other value)
```

# Acknowledgments
The authors sincerely hope to receive any suggestions from you! If you have any questions, please contact us at 2231829@s.hlju.edu.cn. 

