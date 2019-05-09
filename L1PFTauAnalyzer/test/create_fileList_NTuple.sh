#!/bin/sh

#### set tagNTuple value from crab submit jobs and then ./create_fileList_NTuple.sh tagNTuple

pathCrab_VBFHToTauTau=$1
pathTrees_VBFHToTauTau=$2
pathCrab_NeutrinoGun=$3
pathTrees_NeutrinoGun=$4

#tagNTuple='20190505'
#pathCrab_VBFHToTauTau='/cms/store/user/sbhowmik/VBFHToTauTau_M125_14TeV_powheg_pythia8_correctedGridpack/PhaseIIMTDTDRAutumn18MiniAOD_'${tagNTuple}'/*/*'
#pathTrees_VBFHToTauTau='/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_'${tagNTuple}''
#pathCrab_NeutrinoGun='/cms/store/user/sbhowmik/NeutrinoGun_E_10GeV/PhaseIIMTDTDRAutumn18MiniAOD_'${tagNTuple}'/*/*'
#pathTrees_NeutrinoGun='/local/sbhowmik/NTuple_Phase2/L1PFTau/NeutrinoGun_'${tagNTuple}''

unset JAVA_HOME
hdfs='/hdfs'

mkdir $hdfs$pathTrees_VBFHToTauTau
hdfs dfs -copyToLocal $pathCrab_VBFHToTauTau/*root $hdfs$pathTrees_VBFHToTauTau
hdfs dfs -ls $pathTrees_VBFHToTauTau/*root | awk '{print $8}' | grep root | sed 's/^\//\/hdfs\//g' > fileList_NTuple_VBFHToTauTau.list

mkdir $hdfs$pathTrees_NeutrinoGun
hdfs dfs -copyToLocal $pathCrab_NeutrinoGun/*root $hdfs$pathTrees_NeutrinoGun
hdfs dfs -ls $pathTrees_NeutrinoGun/*root | awk '{print $8}' | grep root | sed 's/^\//\/hdfs\//g' > fileList_NTuple_NeutrinoGun.list



