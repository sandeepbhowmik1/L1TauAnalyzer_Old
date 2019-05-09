# L1 Tau Analyzer
L1TauAnalyzer  package for HL-HLC L1Tau trigger studies

# To checkout the code:

cmsrel CMSSW_10_5_0_pre1

cd CMSSW_10_5_0_pre1/src

cmsenv

git cms-init

git remote add cms-l1t-offline https://github.com/cms-l1t-offline/cmssw

git fetch cms-l1t-offline phase2-l1t-integration-CMSSW_10_5_0_pre1

git cms-merge-topic -u cms-l1t-offline:l1t-phase2-v2.17.15.1

git cms-addpkg L1Trigger/L1TCommon

cp /home/veelken/public/classes.h $CMSSW_BASE/src/DataFormats/Phase2L1ParticleFlow/src

cp /home/veelken/public/classes_def.xml $CMSSW_BASE/src/DataFormats/Phase2L1ParticleFlow/src

cp /home/veelken/public/PFCandidateFwd.h $CMSSW_BASE/src/DataFormats/Phase2L1ParticleFlow/interface

git clone https://github.com/HEP-KBFI/l1trigger-phase2l1pftaus $CMSSW_BASE/src/L1Trigger/TallinnL1PFTaus

git clone https://github.com/HEP-KBFI/dataformats-phase2l1pftaus $CMSSW_BASE/src/DataFormats/TallinnL1PFTaus

git clone https://github.com/sandeepbhowmik1/L1TauAnalyzer

scram b -j 8


# To run the L1Tau Analyzer

cd L1TauAnalyzer/L1PFTauAnalyzer/test

# To make plots

cd L1TauAnalyzer/L1PFTauAnalyzer

python commandsToMakePlots.py

Modify 2 lines to get plots in L1TauAnalyzer/L1PFTauAnalyzer/plots/

pathNTuple_TallinnL1PFTau = '/home/sbhowmik/NTuple_Phase2/TallinnL1PFTau'
pathNTuple_L1PFTau = '/home/sbhowmik/NTuple_Phase2/L1PFTau'

