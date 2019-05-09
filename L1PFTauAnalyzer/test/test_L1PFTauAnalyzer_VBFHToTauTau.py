import FWCore.ParameterSet.Config as cms
process = cms.Process('Analyze')
process.maxEvents = cms.untracked.PSet(
	input = cms.untracked.int32(-1)
	)
process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring(
	'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190505/NTuple_TallinnL1PFTauProducer_16.root',
	'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190505/NTuple_TallinnL1PFTauProducer_20.root',
	'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190505/NTuple_TallinnL1PFTauProducer_4.root',
	'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190505/NTuple_TallinnL1PFTauProducer_7.root',
	)
)
process.load("L1TauAnalyzer.L1PFTauAnalyzer.L1PFTauAnalyzer_cff")
process.L1PFTauAnalyzer.histRootFileName = cms.string("hist_test_L1PFTauAnalyzer_VBFHToTauTau_20190508.root")
process.p = cms.Path(
	process.AnalyzerSeq
)
process.schedule = cms.Schedule(process.p)
process.TFileService=cms.Service('TFileService',fileName=cms.string("NTuple_test_L1PFTauAnalyzer_VBFHToTauTau_20190508.root"))
