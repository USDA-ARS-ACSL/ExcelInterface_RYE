# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 12:27:06 2024

@author: Zhuangji.Wang
"""


# root mass Summary
import pandas as pd
import numpy as np

baseDir = 'D:\\Ryesim\\CALIBRATION_EXAMPLE\\'
siteList=['BARC2010','BARC2011','LARC2011','CRSK2011','PRSS2011']
treatmentList=['N_00','N_01','N_02','N_10','N_11','N_12','N_20','N_21','N_22','N_30','N_31','N_32','N_50','N_51','N_52']


RootmassBarc2010=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[0]+'\\'+trt+'\\'+siteList[0]+'.g01'
    df=pd.read_csv(TargetDir)
    Rootmass_number_1=np.array(np.multiply(df.loc[:,'   RootMass'],df.loc[:,'PltLivingFrac'])*500.0)
    Rootmass_number_1=np.reshape(Rootmass_number_1,(Rootmass_number_1.shape[0],1))
    i=i+1
    if (i==1):
        RootmassBarc2010=Rootmass_number_1
    else:          
        RootmassBarc2010=np.append(RootmassBarc2010,Rootmass_number_1,axis=0)

        
RootmassBarc2011=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[1]+'\\'+trt+'\\'+siteList[1]+'.g01'
    df=pd.read_csv(TargetDir)
    Rootmass_number_1=np.array(np.multiply(df.loc[:,'   RootMass'],df.loc[:,'PltLivingFrac'])*500.0)
    Rootmass_number_1=np.reshape(Rootmass_number_1,(Rootmass_number_1.shape[0],1))
    i=i+1
    if (i==1):
        RootmassBarc2011=Rootmass_number_1
    else:          
        RootmassBarc2011=np.append(RootmassBarc2011,Rootmass_number_1,axis=0)


RootmassLarc2011=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[2]+'\\'+trt+'\\'+siteList[2]+'.g01'
    df=pd.read_csv(TargetDir)
    Rootmass_number_1=np.array(np.multiply(df.loc[:,'   RootMass'],df.loc[:,'PltLivingFrac'])*500.0)
    Rootmass_number_1=np.reshape(Rootmass_number_1,(Rootmass_number_1.shape[0],1))
    i=i+1
    if (i==1):
        RootmassLarc2011=Rootmass_number_1
    else:          
        RootmassLarc2011=np.append(RootmassLarc2011,Rootmass_number_1,axis=0)

        
RootmassCrsk2011=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[3]+'\\'+trt+'\\'+siteList[3]+'.g01'
    df=pd.read_csv(TargetDir)
    Rootmass_number_1=np.array(np.multiply(df.loc[:,'   RootMass'],df.loc[:,'PltLivingFrac'])*500.0)
    Rootmass_number_1=np.reshape(Rootmass_number_1,(Rootmass_number_1.shape[0],1))
    i=i+1
    if (i==1):
        RootmassCrsk2011=Rootmass_number_1
    else:          
        RootmassCrsk2011=np.append(RootmassCrsk2011,Rootmass_number_1,axis=0)

        
RootmassPrss2011=[]
i=0
for trt in treatmentList:
    TargetDir=baseDir+siteList[4]+'\\'+trt+'\\'+siteList[4]+'.g01'
    df=pd.read_csv(TargetDir)
    Rootmass_number_1=np.array(np.multiply(df.loc[:,'   RootMass'],df.loc[:,'PltLivingFrac'])*500.0)
    Rootmass_number_1=np.reshape(Rootmass_number_1,(Rootmass_number_1.shape[0],1))
    i=i+1
    if (i==1):
        RootmassPrss2011=Rootmass_number_1
    else:          
        RootmassPrss2011=np.append(RootmassPrss2011,Rootmass_number_1,axis=0)      
        
RootmassALL=np.concatenate((RootmassBarc2010,RootmassBarc2011,RootmassLarc2011,RootmassCrsk2011,RootmassPrss2011),axis=0)