# AdaSemb: An Adaptive Knowledge-Driven Deep Learning Framework Integrating Cancer Protein Assemblies for Predicting PI3Kα Inhibitor Response and Resistance

Phosphatidylinositol 3-kinase alpha inhibitors (PI3Kαis) have revolutionized breast cancer treatment, but acquired resistance remains a major clinical challenge, with around 40% of patients experiencing progression within 4-6 months. Current drug response prediction (DRP) methods typically rely on individual pathways or biomarkers, limiting their ability to capture complex cancer-specific molecular interactions and predict resistance mechanisms. To overcome these limitations, we present AdaSemb, an adaptive, knowledge-driven deep learning framework that uses a multi-protein assembly map to predict responses and resistance to PI3Kαi. AdaSemb comprises two modules: the AdaSemb-PA module incorporates tumor genomic variations into a biological structural neural network. In contrast, the AdaSemb-DRP module uses conditional domain adversarial networks (CDAN) to enhance gene-drug distribution generalization. By combining genomic data with drug molecular structures, AdaSemb identifies critical protein combinations linked to drug resistance. In validation with 1244 cancer cell lines and patient-derived xenografts (PDX), AdaSemb outperformed existing DRP models. In a cohort of 116 breast cancer patients from TCGA, it predicted significantly longer survival for sensitive patients, surpassing traditional biomarkers in accuracy. Furthermore, we identified seven key assemblages that integrate mutations from 93 genes, which distinguish alpelisib-sensitive and -resistant cell lines. This study provides a framework for the comprehensive evaluation of how tumor genomic profiles regulate resistance to PI3Kαi.



## The environment of AdaTrans
```
python==3.11.6
numpy==1.16.4
dgl==1.1.2+cu117
dgllife==0.3.2
pandas==2.1.1
rdkit==2023.9.1
torch==2.1.0+cu121
scikit-learn==1.3.2


```

## Dataset description
The datasets used in this study are all publicly available. GDSC version 1: \url{https://www.cancerrxgene.org/downloads/bulk_download}; 
GDSC version 2: {https://www.cancerrxgene.org/downloads/bulk_download}; 
CTRP version 1: {https://portals.broadinstitute.org/ctrp.v1/}; 
CTRP version 2: {https://portals.broadinstitute.org/ctrp.v2.1/}; 
PDX: {https://www.nature.com/articles/nm.3954}; 
Project GENIE: {https://genie.cbioportal.org/study/summary?id=brca_akt1_genie_2019}; 
cBioPortal: {https://www.cbioportal.org/datasets}.


## Run the moedel  in a GPU server, execute the following::
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
The authors sincerely hope to receive any suggestions from you!  

