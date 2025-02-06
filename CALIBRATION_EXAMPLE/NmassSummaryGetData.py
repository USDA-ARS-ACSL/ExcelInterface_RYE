# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 20:32:35 2024

@author: Zhuangji.Wang
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:50:44 2024

@author: Zhuangji.Wang
"""

# NMass/N mass Summary
import pandas as pd
import numpy as np

baseDir = 'D:\\Ryesim\\CALIBRATION_EXAMPLE\\'
siteList=['BARC2010','BARC2011','LARC2011','CRSK2011','PRSS2011']
treatmentList=['N_00','N_01','N_02','N_10','N_11','N_12','N_20','N_21','N_22','N_30','N_31','N_32','N_50','N_51','N_52']


NMassBarc2010=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[0]+'\\'+trt+'\\'+siteList[0]+'.g01'
    df=pd.read_csv(TargetDir)
    NMass_number_1=np.array(np.multiply(df.loc[:,'     NitroMass'],df.loc[:,'PltLivingFrac'])*500.0)
    NMass_number_1=np.reshape(NMass_number_1,(NMass_number_1.shape[0],1))
    i=i+1
    if (i==1):
        NMassBarc2010=NMass_number_1
    else:          
        NMassBarc2010=np.append(NMassBarc2010,NMass_number_1,axis=0)

        
NMassBarc2011=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[1]+'\\'+trt+'\\'+siteList[1]+'.g01'
    df=pd.read_csv(TargetDir)
    NMass_number_1=np.array(np.multiply(df.loc[:,'     NitroMass'],df.loc[:,'PltLivingFrac'])*500.0)
    NMass_number_1=np.reshape(NMass_number_1,(NMass_number_1.shape[0],1))
    i=i+1
    if (i==1):
        NMassBarc2011=NMass_number_1
    else:          
        NMassBarc2011=np.append(NMassBarc2011,NMass_number_1,axis=0)


NMassLarc2011=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[2]+'\\'+trt+'\\'+siteList[2]+'.g01'
    df=pd.read_csv(TargetDir)
    NMass_number_1=np.array(np.multiply(df.loc[:,'     NitroMass'],df.loc[:,'PltLivingFrac'])*500.0)
    NMass_number_1=np.reshape(NMass_number_1,(NMass_number_1.shape[0],1))
    i=i+1
    if (i==1):
        NMassLarc2011=NMass_number_1
    else:          
        NMassLarc2011=np.append(NMassLarc2011,NMass_number_1,axis=0)

        
NMassCrsk2011=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[3]+'\\'+trt+'\\'+siteList[3]+'.g01'
    df=pd.read_csv(TargetDir)
    NMass_number_1=np.array(np.multiply(df.loc[:,'     NitroMass'],df.loc[:,'PltLivingFrac'])*500.0)
    NMass_number_1=np.reshape(NMass_number_1,(NMass_number_1.shape[0],1))
    i=i+1
    if (i==1):
        NMassCrsk2011=NMass_number_1
    else:          
        NMassCrsk2011=np.append(NMassCrsk2011,NMass_number_1,axis=0)

        
NMassPrss2011=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[4]+'\\'+trt+'\\'+siteList[4]+'.g01'
    df=pd.read_csv(TargetDir)
    NMass_number_1=np.array(np.multiply(df.loc[:,'     NitroMass'],df.loc[:,'PltLivingFrac'])*500.0)
    NMass_number_1=np.reshape(NMass_number_1,(NMass_number_1.shape[0],1))
    i=i+1
    if (i==1):
        NMassPrss2011=NMass_number_1
    else:          
        NMassPrss2011=np.append(NMassPrss2011,NMass_number_1,axis=0)        
        
NMassALL=np.concatenate((NMassBarc2010,NMassBarc2011,NMassLarc2011,NMassCrsk2011,NMassPrss2011),axis=0)
