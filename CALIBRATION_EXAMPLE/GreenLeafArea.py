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

# biomass/N mass Summary
import pandas as pd
import numpy as np

baseDir = 'D:\\Ryesim\\CALIBRATION_EXAMPLE\\'
siteList=['BARC2010','BARC2011','LARC2011','CRSK2011','PRSS2011']
treatmentList=['N_00','N_01','N_02','N_10','N_11','N_12','N_20','N_21','N_22','N_30','N_31','N_32','N_50','N_51','N_52']


GreenLfAreaBarc2010=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[0]+'\\'+trt+'\\'+siteList[0]+'.g01'
    df=pd.read_csv(TargetDir)
    GreenLfArea_number_1=np.array(np.multiply(df.loc[:,' GreenLfArea'],df.loc[:,'PltLivingFrac'])*500.0/10000.0)
    GreenLfArea_number_1=np.reshape(GreenLfArea_number_1,(GreenLfArea_number_1.shape[0],1))
    i=i+1
    if (i==1):
        GreenLfAreaBarc2010=GreenLfArea_number_1
    else:          
        GreenLfAreaBarc2010=np.append(GreenLfAreaBarc2010,GreenLfArea_number_1,axis=0)

        
GreenLfAreaBarc2011=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[1]+'\\'+trt+'\\'+siteList[1]+'.g01'
    df=pd.read_csv(TargetDir)
    GreenLfArea_number_1=np.array(np.multiply(df.loc[:,' GreenLfArea'],df.loc[:,'PltLivingFrac'])*500.0/10000.0)
    GreenLfArea_number_1=np.reshape(GreenLfArea_number_1,(GreenLfArea_number_1.shape[0],1))
    i=i+1
    if (i==1):
        GreenLfAreaBarc2011=GreenLfArea_number_1
    else:          
        GreenLfAreaBarc2011=np.append(GreenLfAreaBarc2011,GreenLfArea_number_1,axis=0)


GreenLfAreaLarc2011=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[2]+'\\'+trt+'\\'+siteList[2]+'.g01'
    df=pd.read_csv(TargetDir)
    GreenLfArea_number_1=np.array(np.multiply(df.loc[:,' GreenLfArea'],df.loc[:,'PltLivingFrac'])*500.0/10000.0)
    GreenLfArea_number_1=np.reshape(GreenLfArea_number_1,(GreenLfArea_number_1.shape[0],1))
    i=i+1
    if (i==1):
        GreenLfAreaLarc2011=GreenLfArea_number_1
    else:          
        GreenLfAreaLarc2011=np.append(GreenLfAreaLarc2011,GreenLfArea_number_1,axis=0)

        
GreenLfAreaCrsk2011=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[3]+'\\'+trt+'\\'+siteList[3]+'.g01'
    df=pd.read_csv(TargetDir)
    GreenLfArea_number_1=np.array(np.multiply(df.loc[:,' GreenLfArea'],df.loc[:,'PltLivingFrac'])*500.0/10000.0)
    GreenLfArea_number_1=np.reshape(GreenLfArea_number_1,(GreenLfArea_number_1.shape[0],1))
    i=i+1
    if (i==1):
        GreenLfAreaCrsk2011=GreenLfArea_number_1
    else:          
        GreenLfAreaCrsk2011=np.append(GreenLfAreaCrsk2011,GreenLfArea_number_1,axis=0)

        
GreenLfAreaPrss2011=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[4]+'\\'+trt+'\\'+siteList[4]+'.g01'
    df=pd.read_csv(TargetDir)
    GreenLfArea_number_1=np.array(np.multiply(df.loc[:,' GreenLfArea'],df.loc[:,'PltLivingFrac'])*500.0/10000.0)
    GreenLfArea_number_1=np.reshape(GreenLfArea_number_1,(GreenLfArea_number_1.shape[0],1))
    i=i+1
    if (i==1):
        GreenLfAreaPrss2011=GreenLfArea_number_1
    else:          
        GreenLfAreaPrss2011=np.append(GreenLfAreaPrss2011,GreenLfArea_number_1,axis=0)      
        
GreenLfAreaALL=np.concatenate((GreenLfAreaBarc2010,GreenLfAreaBarc2011,GreenLfAreaLarc2011,GreenLfAreaCrsk2011,GreenLfAreaPrss2011),axis=0)
