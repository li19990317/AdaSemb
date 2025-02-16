#!/bin/bash

homedir="$1"

gene2idfile="${homedir}/sample/gene2ind.txt"
cell2idfile="${homedir}/sample/cell2ind.txt"
mutationfile="${homedir}/sample/cell2mutation.txt"
cn_deletionfile="${homedir}/sample/cell2cndeletion.txt"
cn_amplificationfile="${homedir}/sample/cell2cnamplification.txt"
testdatafile="${homedir}/sample/test_data.txt"

modeldir="${homedir}/sample/models/nutlin-3A_1"
modelfile="${modeldir}/model_nutlin-3A_1.pt"

stdfile="${modeldir}/std.txt"

resultfile="${modeldir}/predict"

hiddendir="${modeldir}/hidden"
if [ -d $hiddendir ]
then
	rm -rf $hiddendir
fi
mkdir -p $hiddendir

zscore_method="auc"

cudaid=0

pyScript="${homedir}/src/predict.py"

source activate cuda11_env

python -u $pyScript -gene2id $gene2idfile -cell2id $cell2idfile -std $stdfile -hidden $hiddendir -result $resultfile \
	-mutations $mutationfile -cn_deletions $cn_deletionfile -cn_amplifications $cn_amplificationfile \
	-batchsize 2000 -results $testdatafile -zscore_method $zscore_method -load $modelfile -cuda $cudaid > "${modeldir}/test.log"
