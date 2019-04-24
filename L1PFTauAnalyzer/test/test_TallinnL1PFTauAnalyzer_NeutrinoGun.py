import FWCore.ParameterSet.Config as cms

process = cms.Process('Analyze')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    #input = cms.untracked.int32(100)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/NeutrinoGun_20190423/NTuple_TallinnL1PFTauProducer_2.root',
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/NeutrinoGun_20190423/NTuple_TallinnL1PFTauProducer_3.root',
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/NeutrinoGun_20190423/NTuple_TallinnL1PFTauProducer_4.root',
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/NeutrinoGun_20190423/NTuple_TallinnL1PFTauProducer_6.root',
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/NeutrinoGun_20190423/NTuple_TallinnL1PFTauProducer_18.root',
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/NeutrinoGun_20190423/NTuple_TallinnL1PFTauProducer_25.root',
        'file:/hdfs/local/sbhowmik/NTuple_Phase2/L1PFTau/NeutrinoGun_20190423/NTuple_TallinnL1PFTauProducer_38.root',
        )
)

process.options = cms.untracked.PSet(

)

process.load("L1TauAnalyzer.L1PFTauAnalyzer.TallinnL1PFTauAnalyzer_cff")

process.p = cms.Path(
    process.AnalyzerSeq
)

process.schedule = cms.Schedule(process.p)

process.TFileService=cms.Service('TFileService',fileName=cms.string("NTuple_test_TallinnL1PFTauAnalyzer_NeutrinoGun.root"))
