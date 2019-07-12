#!/bin/sh
## set tagNTuple value from crab submit jobs and then ./create_fileList_test_TauAnalyzer.sh tagNTuple

tagNTuple=$1
#tagNTuple=20190505
fileListTag=(GluGluHToTauTau  NeutrinoGun)
fileAnalTag=(TallinnL1PFTauAnalyzer L1PFTauAnalyzer)

jobSubmitFile=submit_jobs_cmsRun.sh
rm $jobSubmitFile
echo \#!/bin/sh | cat >>$jobSubmitFile


for ((i_fileList=0; i_fileList<=1; i_fileList++))
do
    #echo $i_fileList
    #echo ${fileListTag[$i_fileList]}
    fileList=fileList_NTuple_${fileListTag[$i_fileList]}.list
    #echo $fileList

    count1=0
    while read -r line; do
	((count1+=1))
    done < $fileList
    echo $count1
    nLineToAFile=250
    nFileLine=$(($count1 / $nLineToAFile))
    nFileLine=$(($nFileLine+1))
    echo $nFileLine

    for ((i_fileLine=1; i_fileLine<=$nFileLine; i_fileLine++))
    do
	echo $i_fileLine
	lineStart=$(($nLineToAFile*($i_fileLine-1)))
	echo $lineStart
	lineEnd=$(($nLineToAFile*$i_fileLine))
	echo $lineEnd

	for ((i_fileAnal=0; i_fileAnal<=1; i_fileAnal++))
	do
	#echo $i_fileAnal
	#echo ${fileAnalTag[$i_fileAnal]}
	    fileOut=test_${fileAnalTag[$i_fileAnal]}_${fileListTag[$i_fileList]}_part_${i_fileLine}.py
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
	    
	    
	    echo $i_fileLine
	    lineStart=$(($nLineToAFile*($i_fileLine-1)))
	    echo $lineStart
	    lineEnd=$(($nLineToAFile*$i_fileLine))
	    echo $lineEnd
	    count2=0
	    while read -r line; do
		((count2+=1))
		if [ $count2 -gt $lineStart ] && [ $count2 -le $lineEnd ]; then
		    dataset=$line

		    printf "\t" test  | cat >>$fileOut
		    echo "'file:$dataset'," | cat >>$fileOut
		else
		    continue
		fi
	    done < $fileList
	    
	    

	    #while read -r line; do
		#dataset=$line
		#printf "\t" test  | cat >>$fileOut
		#echo "'file:$dataset'," | cat >>$fileOut
	    #done < $fileList
	    
	    printf "\t" test  | cat >>$fileOut
            echo ")" | cat >>$fileOut
	    echo ")" | cat >>$fileOut
	    
	    
	    echo "process.load(\"L1TauAnalyzer.L1PFTauAnalyzer.${fileAnalTag[$i_fileAnal]}_cff\")" | cat >>$fileOut
	    
	    echo "process.${fileAnalTag[$i_fileAnal]}.histRootFileName = cms.string(\"hist_test_${fileAnalTag[$i_fileAnal]}_${fileListTag[$i_fileList]}_${tagNTuple}_part_${i_fileLine}.root\")" | cat >>$fileOut
	    
	    echo "process.p = cms.Path(" | cat >>$fileOut
	    printf "\t" test  | cat >>$fileOut
	    echo "process.AnalyzerSeq"  | cat >>$fileOut
	    echo ")" | cat >>$fileOut
	    
	    echo "process.schedule = cms.Schedule(process.p)" | cat >>$fileOut
	    
	    echo "process.TFileService=cms.Service('TFileService',fileName=cms.string(\"NTuple_test_${fileAnalTag[$i_fileAnal]}_${fileListTag[$i_fileList]}_${tagNTuple}_part_${i_fileLine}.root\"))" | cat >>$fileOut




	    echo "cmsRun -p $fileOut > out_${fileAnalTag[$i_fileAnal]}_${fileListTag[$i_fileList]}_part_${i_fileLine}.log &"  | cat >>$jobSubmitFile  
	done
    done
done

chmod 755 $jobSubmitFile