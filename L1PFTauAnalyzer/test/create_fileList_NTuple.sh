#!/bin/sh

#### set tagNTuple value from crab submit jobs and then ./create_fileList_NTuple.sh tagNTuple

pathCrab_GluGluHToTauTau=$1
pathCrab_NeutrinoGun=$2

#tagNTuple='20190505'
#pathCrab_GluGluHToTauTau='/cms/store/user/sbhowmik/GluGluHToTauTau_M125_14TeV_powheg_pythia8_correctedGridpack/PhaseIIMTDTDRAutumn18MiniAOD_'${tagNTuple}'/*/*'
#pathCrab_NeutrinoGun='/cms/store/user/sbhowmik/NeutrinoGun_E_10GeV/PhaseIIMTDTDRAutumn18MiniAOD_'${tagNTuple}'/*/*'

unset JAVA_HOME

hdfs dfs -ls $pathCrab_GluGluHToTauTau/*root | awk '{print $8}' | grep root | sed 's/^\//\/hdfs\//g' > fileList_NTuple_GluGluHToTauTau.list

hdfs dfs -ls $pathCrab_NeutrinoGun/*root | awk '{print $8}' | grep root | sed 's/^\//\/hdfs\//g' > fileList_NTuple_NeutrinoGun.list


