# L1 Tau Analyzer
L1TauAnalyzer  package for HL-HLC L1Tau trigger studies

# It has two packages : 
Old one (L1TauAnalyzer/L1PFTauAnalyzer) is still there

But new one is L1TauAnalyzer/L1HPSPFTauAnalyzer


# ------------ To run in Tallinn T2 --------------

singularity exec --home $HOME:/srv --bind /cvmfs --bind /hdfs --bind /home --pwd /srv --contain --ipc --pid /cvmfs/singularity.opensciencegrid.org/bbockelm/cms:rhel7 bash

source /cvmfs/cms.cern.ch/cmsset_default.sh

export SCRAM_ARCH=slc7_amd64_gcc700


# ------------- Install CMSSW ---------------------

cmsrel CMSSW_10_6_1_patch2

cd CMSSW_10_6_1_patch2/src

cmsenv

git cms-init

git remote add cms-l1t-offline https://github.com/cms-l1t-offline/cmssw.git

git fetch cms-l1t-offline phase2-l1t-integration-CMSSW_10_6_1_patch2

git cms-merge-topic -u cms-l1t-offline:l1t-phase2-v2.23.2

git cms-addpkg L1Trigger/L1TCommon

scram b -j 8


# ------------- Check out L1TauAnalyzer ---------------------

git clone https://github.com/sandeepbhowmik1/L1TauAnalyzer

cd L1TauAnalyzer/L1HPSPFTauAnalyzer

scram b -j 8


# ------------- Checkout old cmssw version  ----------------

cmsrel CMSSW_10_5_0_pre1

cd CMSSW_10_5_0_pre1/src

cmsenv

git cms-init

git remote add cms-l1t-offline https://github.com/cms-l1t-offline/cmssw

git fetch cms-l1t-offline phase2-l1t-integration-CMSSW_10_5_0_pre1

git cms-merge-topic -u cms-l1t-offline:l1t-phase2-v2.17.15.1

git cms-addpkg L1Trigger/L1TCommon

scram b -j 8

# ------ Add L1HPSTau package to old cmssw version  -------

https://github.com/sandeepbhowmik1/L1HPSTaus/blob/master/README.md


# -------- To run the L1HPSTau Analyzer ------------------

cd L1TauAnalyzer/L1HPSPFTauAnalyzer/test

# ------------- To make plots --------------------------

cd L1TauAnalyzer/L1HPSPFTauAnalyzer

python commandsToMakePlots.py

Modify 2 lines to get plots in L1TauAnalyzer/L1HPSPFTauAnalyzer/plots/

pathNTuple_L1HPSPFTau = '/home/sbhowmik/NTuple_Phase2/L1HPSPFTau'

pathNTuple_L1PFTau = '/home/sbhowmik/NTuple_Phase2/L1PFTau'

