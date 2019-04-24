import FWCore.ParameterSet.Config as cms

process = cms.Process('Analyze')

process.maxEvents = cms.untracked.PSet(
    #input = cms.untracked.int32(-1)
    input = cms.untracked.int32(100)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1Trigger/TallinnL1PFTaus/test/NTuple_TallinnL1PFTauProducer.root',
        )
)

process.options = cms.untracked.PSet(

)

process.load("L1TauAnalyzer.L1PFTauAnalyzer.TallinnL1PFTauAnalyzer_cff")

process.p = cms.Path(
    process.AnalyzerSeq
)

process.schedule = cms.Schedule(process.p)

process.TFileService=cms.Service('TFileService',fileName=cms.string("NTuple_test_TallinnL1PFTauAnalyzer.root"))
