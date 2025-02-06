# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:15:00 2023

@author: Zhuangji.Wang
"""

# Tiller Summary
import pandas as pd

baseDir = 'D:\\Ryesim\\CALIBRATION_EXAMPLE\\'
siteList=['BARC2009','BARC2010','BARC2011','LARC2011','CRSK2011','PRSS2011']
treatmentList_BARC2009=['N_00','N_10','N_20','N_40','N_60']
treatmentList_other=['N_00','N_01','N_02','N_10','N_11','N_12','N_20','N_21','N_22','N_30','N_31','N_32','N_50','N_51','N_52']

tillerBarc2009=[]
for trt in treatmentList_BARC2009:
    TargetDir=baseDir+siteList[0]+'\\'+trt+'\\'+siteList[0]+'.g01'
    df=pd.read_csv(TargetDir)
    df.set_index(['date','       time'], inplace=True)
    tiller_number=df.loc[('03/25/2010',0)]['TillerNum']*df.loc[('03/25/2010',0)]['PltLivingFrac']*500.0
    tillerBarc2009.append(tiller_number)


tillerBarc2010=[]
for trt in treatmentList_other:
    TargetDir=baseDir+siteList[1]+'\\'+trt+'\\'+siteList[1]+'.g01'
    df=pd.read_csv(TargetDir)
    df.set_index(['date','       time'], inplace=True)
    tiller_number=df.loc[('03/02/2011',0)]['TillerNum']*df.loc[('03/02/2011',0)]['PltLivingFrac']*500.0
    tillerBarc2010.append(tiller_number)
    tiller_number=df.loc[('03/28/2011',0)]['TillerNum']*df.loc[('03/28/2011',0)]['PltLivingFrac']*500.0
    tillerBarc2010.append(tiller_number)
    tiller_number=df.loc[('05/02/2011',0)]['TillerNum']*df.loc[('05/02/2011',0)]['PltLivingFrac']*500.0
    tillerBarc2010.append(tiller_number)


tillerBarc2011=[]
for trt in treatmentList_other:
    TargetDir=baseDir+siteList[2]+'\\'+trt+'\\'+siteList[2]+'.g01'
    df=pd.read_csv(TargetDir)
    df.set_index(['date','       time'], inplace=True)
    tiller_number=df.loc[('03/01/2012',0)]['TillerNum']*df.loc[('03/01/2012',0)]['PltLivingFrac']*500.0
    tillerBarc2011.append(tiller_number)
    tiller_number=df.loc[('03/22/2012',0)]['TillerNum']*df.loc[('03/22/2012',0)]['PltLivingFrac']*500.0
    tillerBarc2011.append(tiller_number)
    tiller_number=df.loc[('04/20/2012',0)]['TillerNum']*df.loc[('04/20/2012',0)]['PltLivingFrac']*500.0
    tillerBarc2011.append(tiller_number)

tillerLarc2011=[]
for trt in treatmentList_other:
    TargetDir=baseDir+siteList[3]+'\\'+trt+'\\'+siteList[3]+'.g01'
    df=pd.read_csv(TargetDir)
    df.set_index(['date','       time'], inplace=True)
    tiller_number=df.loc[('03/12/2012',0)]['TillerNum']*df.loc[('03/12/2012',0)]['PltLivingFrac']*500.0
    tillerLarc2011.append(tiller_number)
    tiller_number=df.loc[('04/03/2012',0)]['TillerNum']*df.loc[('04/03/2012',0)]['PltLivingFrac']*500.0
    tillerLarc2011.append(tiller_number)
    tiller_number=df.loc[('05/10/2012',0)]['TillerNum']*df.loc[('05/10/2012',0)]['PltLivingFrac']*500.0
    tillerLarc2011.append(tiller_number)


tillerCrsk2011=[]
for trt in treatmentList_other:
    TargetDir=baseDir+siteList[4]+'\\'+trt+'\\'+siteList[4]+'.g01'
    df=pd.read_csv(TargetDir)
    df.set_index(['date','       time'], inplace=True)
    tiller_number=df.loc[('03/07/2012',0)]['TillerNum']*df.loc[('03/07/2012',0)]['PltLivingFrac']*500.0
    tillerCrsk2011.append(tiller_number)
    
tillerPrss2011=[]
for trt in treatmentList_other:
    TargetDir=baseDir+siteList[5]+'\\'+trt+'\\'+siteList[5]+'.g01'
    df=pd.read_csv(TargetDir)
    df.set_index(['date','       time'], inplace=True)
    tiller_number=df.loc[('02/28/2012',0)]['TillerNum']*df.loc[('02/28/2012',0)]['PltLivingFrac']*500.0
    tillerPrss2011.append(tiller_number)
    tiller_number=df.loc[('03/19/2012',0)]['TillerNum']*df.loc[('03/19/2012',0)]['PltLivingFrac']*500.0
    tillerPrss2011.append(tiller_number)
    
tillerTotal=tillerBarc2009+tillerBarc2010+tillerBarc2011+tillerLarc2011+tillerCrsk2011+tillerPrss2011