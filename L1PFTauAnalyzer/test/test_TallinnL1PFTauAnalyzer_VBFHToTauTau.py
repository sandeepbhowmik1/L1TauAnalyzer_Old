import FWCore.ParameterSet.Config as cms

process = cms.Process('Analyze')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    #input = cms.untracked.int32(100)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190423/NTuple_TallinnL1PFTauProducer_1.root',
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190423/NTuple_TallinnL1PFTauProducer_4.root',
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190423/NTuple_TallinnL1PFTauProducer_5.root',
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190423/NTuple_TallinnL1PFTauProducer_7.root',
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190423/NTuple_TallinnL1PFTauProducer_8.root',
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190423/NTuple_TallinnL1PFTauProducer_11.root',
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190423/NTuple_TallinnL1PFTauProducer_15.root',
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190423/NTuple_TallinnL1PFTauProducer_16.root',
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190423/NTuple_TallinnL1PFTauProducer_20.root',
        )
)

process.options = cms.untracked.PSet(

)

process.load("L1TauAnalyzer.L1PFTauAnalyzer.TallinnL1PFTauAnalyzer_cff")

process.p = cms.Path(
    process.AnalyzerSeq
)

process.schedule = cms.Schedule(process.p)

process.TFileService=cms.Service('TFileService',fileName=cms.string("NTuple_test_TallinnL1PFTauAnalyzer_VBFHToTauTau.root"))
