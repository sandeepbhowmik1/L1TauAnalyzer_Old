#!/bin/sh
## set tagNTuple value from crab submit jobs and then ./create_fileList_test_TauAnalyzer.sh tagNTuple

tagNTuple=$1
#tagNTuple=20190505
fileListTag=(VBFHToTauTau  NeutrinoGun)
fileAnalTag=(TallinnL1PFTauAnalyzer L1PFTauAnalyzer)

for ((i_fileList=0; i_fileList<=1; i_fileList++))
do
    #echo $i_fileList
    #echo ${fileListTag[$i_fileList]}
    fileList=fileList_NTuple_${fileListTag[$i_fileList]}.list
    #echo $fileList

    for ((i_fileOut=0; i_fileOut<=1; i_fileOut++))
    do
	#echo $i_fileOut
	#echo ${fileAnalTag[$i_fileOut]}
	fileOut=test_${fileAnalTag[$i_fileOut]}_${fileListTag[$i_fileList]}.py
	rm $fileOut
	echo $fileOut

	echo "import FWCore.ParameterSet.Config as cms" | cat >>$fileOut
	
	echo "process = cms.Process('Analyze')" | cat >>$fileOut
	
	echo "process.maxEvents = cms.untracked.PSet(" | cat >>$fileOut
	printf "\t" test  | cat >>$fileOut
	echo "input = cms.untracked.int32(-1)" | cat >>$fileOut
	printf "\t" test  | cat >>$fileOut
	echo ")" | cat >>$fileOut

	echo "process.source = cms.Source(\"PoolSource\"," | cat >>$fileOut
	printf "\t" test  | cat >>$fileOut
	echo "fileNames = cms.untracked.vstring(" | cat >>$fileOut



	while read -r line; do
	    dataset=$line
	    printf "\t" test  | cat >>$fileOut
	    echo "'file:$dataset'," | cat >>$fileOut
	done < $fileList

	printf "\t" test  | cat >>$fileOut
        echo ")" | cat >>$fileOut
	echo ")" | cat >>$fileOut


	echo "process.load(\"L1TauAnalyzer.L1PFTauAnalyzer.${fileAnalTag[$i_fileOut]}_cff\")" | cat >>$fileOut
	
	echo "process.${fileAnalTag[$i_fileOut]}.histRootFileName = cms.string(\"hist_test_${fileAnalTag[$i_fileOut]}_${fileListTag[$i_fileList]}_${tagNTuple}.root\")" | cat >>$fileOut
	
	echo "process.p = cms.Path(" | cat >>$fileOut
	printf "\t" test  | cat >>$fileOut
	echo "process.AnalyzerSeq"  | cat >>$fileOut
	echo ")" | cat >>$fileOut
	
	echo "process.schedule = cms.Schedule(process.p)" | cat >>$fileOut
	
	echo "process.TFileService=cms.Service('TFileService',fileName=cms.string(\"NTuple_test_${fileAnalTag[$i_fileOut]}_${fileListTag[$i_fileList]}_${tagNTuple}.root\"))" | cat >>$fileOut





	
    done
done
