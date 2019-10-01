import FWCore.ParameterSet.Config as cms
process = cms.Process('Analyze')
process.maxEvents = cms.untracked.PSet(
	input = cms.untracked.int32(100)
	)
process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring(
        'file:/hdfs/cms/store/user/sbhowmik/GluGluHToTauTau_M125_14TeV_powheg_pythia8_TuneCP5/GluGluHToTauTau_PhaseIITDRSpring19MiniAOD_20190924/190924_080944/0000/NTuple_L1HPSPFDiTauProducer_1.root',
	)
)
process.load("L1TauAnalyzer.L1PFTauAnalyzer.L1HPSPFDiTauAnalyzer_cff")
process.L1HPSPFDiTauAnalyzer.histRootFileName = cms.string("hist_test_L1HPSPFDiTauAnalyzer_GluGluHToTauTau_20190926_3_part_1.root")
process.L1HPSPFDiTauAnalyzer.bdtRootFileName = cms.string("bdt_test_L1HPSPFDiTauAnalyzer_GluGluHToTauTau_20190926_3_part_1.root")
process.p = cms.Path(
	process.AnalyzerSeq
)
process.schedule = cms.Schedule(process.p)
process.TFileService=cms.Service('TFileService',fileName=cms.string("NTuple_test_L1HPSPFDiTauAnalyzer_GluGluHToTauTau_20190926_3_part_1.root"))
