#
# provide online L1 Trigger DQM input from file(s)
#
# V M Ghete 2010-07-09

import FWCore.ParameterSet.Config as cms

###################### user choices ######################

# choose one sample identifier from the list of data samples 
#
#sampleIdentifier = '165633-CAFDQM'
#sampleIdentifier = '195378'
#sampleIdentifier = '195390'
#sampleIdentifier = 'Commissioning2014'
#sampleIdentifier = '225461'
#sampleIdentifier = '226129'

sampleIdentifier = '226144'


#sampleIdentifier = '225602'
#sampleIdentifier = '225608'

maxNumberEvents = 100#0#0
#maxNumberEvents = 5000#0#0
#maxNumberEvents = 50000#0#0
#maxNumberEvents  = 500000
#maxNumberEvents = -1#0#0



###################### end user choices ###################

# initialize list of files, of secondary files, list of selected events and luminosity segments
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
selectedEvents = cms.untracked.VEventRange()
selectedLumis= cms.untracked.VLuminosityBlockRange()


maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(maxNumberEvents)
)



if sampleIdentifier == '195378' :
    runNumber = '195378'
    dataset = '/MinimumBias/Run2012B-v1/RAW'
    dataType = 'RAW'
    useDAS = True
    selectedLumis= cms.untracked.VLuminosityBlockRange(
                                                '195378:1275-195378:max'
                                                )
           
elif sampleIdentifier == '195379' :
    runNumber = '195379'
    dataset = '/MinimumBias/Run2012B-v1/RAW'
    dataType = 'RAW'
    useDAS = True
           
elif sampleIdentifier == '195390' :
    runNumber = '195390'
    dataset = '/MinimumBias/Run2012B-v1/RAW'
    dataType = 'RAW'
    useDAS = True
           
# high PU run 2011   
elif sampleIdentifier == '179828' :
    runNumber = '179828'
    dataset =  '/ZeroBiasHPF0/Run2011B-v1/RAW'
    dataType = 'RAW'
    useDAS = True
        
        
elif sampleIdentifier == '165633-CAFDQM' :
    runNumber = '165633'
    dataset = '/ZeroBiasHPF0/Run2011B-v1/RAW'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [ 
            'file:/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/DQMTest/MinimumBias__RAW__v1__165633__1CC420EE-B686-E011-A788-0030487CD6E8.root'                       
            ]);    

elif sampleIdentifier == '225461' :
    runNumber = '225461'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
            'file:/afs/cern.ch/work/p/peveraer/public/local_run_225461/csctf.root'
            ]);

elif sampleIdentifier == '225602' :
    runNumber = '225602'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
	    'file:/afs/cern.ch/work/p/peveraer/public/local_run_225602/csctf.root'
            ]);

elif sampleIdentifier == '225608' :
    runNumber = '225608'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
	    'file:/afs/cern.ch/work/p/peveraer/public/local_run_225608/csctf.root'
            ]);


elif sampleIdentifier == '226129' :
    runNumber = '226129'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
	    '/store/user/rewang/csctf/local_run_226129_csctf.root'
            ]);


elif sampleIdentifier == '226144' :
    runNumber = '226144'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
	    'file:/afs/cern.ch/work/p/peveraer/public/local_run_226144/csctf.root'
            ]);


elif sampleIdentifier == 'Commissioning2014' :
    runNumber = '225956'                                                                                                                                   
    dataset = '/Commissioning2014/Cosmics/RAW'                                                                                                              
    dataType = 'RAW'                                                                                                                                       
    useDAS = False  
    readFiles.extend( [ 
       #'/store/data/Commissioning2014/Cosmics/RAW/v3/000/225/930/00000/7604F4CA-9D33-E411-A11C-02163E008D1E.root',
       #'/store/data/Commissioning2014/Cosmics/RAW/v3/000/225/948/00000/06DDCD46-9E33-E411-89A3-02163E00EF65.root',
       #'/store/data/Commissioning2014/Cosmics/RAW/v3/000/225/949/00000/A2C2553D-9E33-E411-912B-02163E00F191.root',
       #'/store/data/Commissioning2014/Cosmics/RAW/v3/000/225/953/00000/1A0A48DE-A033-E411-9310-02163E00F11B.root',
       #'/store/data/Commissioning2014/Cosmics/RAW/v3/000/225/956/00000/640CC997-A633-E411-8432-02163E006E23.root'
       #'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/041F728D-A033-E411-8BC5-02163E007A48.root'
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/041F728D-A033-E411-8BC5-02163E007A48.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/104E624D-A133-E411-A31E-02163E00ED8B.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/188EDA50-A133-E411-93F8-02163E00CFD6.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/1C42F5A0-A133-E411-9256-02163E00F120.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/40736BB2-A133-E411-805A-02163E00D44D.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/4490CC4E-A133-E411-9D5E-02163E009F78.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/56DFD7AA-A633-E411-AB4D-02163E008EFB.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/5CC308B3-A133-E411-BDE3-02163E00A1B7.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/60554991-A633-E411-B321-02163E008E84.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/82CA7B9F-A633-E411-A0A9-02163E008E84.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/867E7D31-A133-E411-9CDF-02163E00CFD6.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/9AA49FB1-A133-E411-A607-02163E00F029.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/CA51E093-A633-E411-B34A-02163E008F58.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/E0E0774D-A133-E411-A072-02163E008C0A.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/F0EAB950-A133-E411-9DA5-02163E008CEF.root',

            ]);
                                                                                                           
elif sampleIdentifier == 'FileStream_105760' :
    runNumber = '105760'
    dataset = 'A_Stream'
    dataType = 'FileStream'
    useDAS = False
    readFiles.extend( [
            'file:/lookarea_SM/MWGR_29.00105760.0001.A.storageManager.00.0000.dat'       
            ] );
                
else :
    print 'Error: sample identifier ', sampleIdentifier, ' not defined.\n'
    errorUserOptions = True 
    runNumber = '0'
    dataset = 'None'
    dataType = 'None'
    useDAS = False
       
     
#            
# end of data samples 
#            

print "   Run number: ", runNumber
print "   Dataset: ", dataset
print "   Data type: ", dataType

if useDAS :
    import das_client
    import os

    # query DAS
    myQuery =  'file dataset=' + dataset + ' run=' + runNumber
    dasClientCommand = 'das_client.py --limit=0 --format=plain --query='+'"'+myQuery+'"'
    data = os.popen(dasClientCommand)
    filePaths = data.readlines()
            
       
    print '\n   das_client using the query'
    print '      ', myQuery
    print '   retrieved the following files\n'
        
    #newPath = []
    for line in filePaths :
        print '      ', line
	#newPath.append('root://eoscms//eos/cms'+line)
           
    readFiles.extend(filePaths);
    #readFiles.extend(newPath);
    #readFiles.extend('file:');
        
        
    # nothing added to secondary files by DAS 
    secFiles.extend([
            ])

        
# for RAW data, run first the RAWTODIGI 
if dataType == 'StreamFile' :
    source = cms.Source("NewEventStreamFileReader", fileNames=readFiles)
else :               
    source = cms.Source ('PoolSource', 
                            fileNames=readFiles, 
                            secondaryFileNames=secFiles,
                            lumisToProcess = selectedLumis,
                            eventsToProcess = selectedEvents
                            )

