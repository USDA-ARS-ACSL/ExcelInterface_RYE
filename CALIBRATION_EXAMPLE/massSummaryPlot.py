# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 14:22:05 2023

@author: Zhuangji.Wang
"""

# biomass/N mass Summary
import pandas as pd

baseDir = 'D:\\Ryesim\\CALIBRATION_EXAMPLE\\'
siteList=['BARC2009','BARC2010','BARC2011','LARC2011','CRSK2011','PRSS2011']
treatmentList_BARC2009=['N_00','N_10','N_20','N_40','N_60']
treatmentList_other=['N_00','N_01','N_02','N_10','N_11','N_12','N_20','N_21','N_22','N_30','N_31','N_32','N_50','N_51','N_52']

shootbiomassBarc2009=[]
rootbiomassBarc2009=[]
nitrogenBarc2009=[]
for trt in treatmentList_BARC2009:
    TargetDir=baseDir+siteList[0]+'\\'+trt+'\\'+siteList[0]+'.g01'
    df=pd.read_csv(TargetDir)
    df.set_index(['date','       time'], inplace=True)
    shoot_biomass=df.loc[('03/25/2010',0)]['  ShootMass']*df.loc[('03/25/2010',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('03/25/2010',0)]['   RootMass']*df.loc[('03/25/2010',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('03/25/2010',0)]['     NitroMass']*df.loc[('03/25/2010',0)]['PltLivingFrac']*500.0
    shootbiomassBarc2009.append(shoot_biomass)
    rootbiomassBarc2009.append(root_biomass)
    nitrogenBarc2009.append(nitrogen_mass)
    
    shoot_biomass=df.loc[('04/20/2010',0)]['  ShootMass']*df.loc[('04/20/2010',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('04/20/2010',0)]['   RootMass']*df.loc[('04/20/2010',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('04/20/2010',0)]['     NitroMass']*df.loc[('04/20/2010',0)]['PltLivingFrac']*500.0
    shootbiomassBarc2009.append(shoot_biomass)
    rootbiomassBarc2009.append(root_biomass)
    nitrogenBarc2009.append(nitrogen_mass)
    
    shoot_biomass=df.loc[('05/11/2010',0)]['  ShootMass']*df.loc[('05/11/2010',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('05/11/2010',0)]['   RootMass']*df.loc[('05/11/2010',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('05/11/2010',0)]['     NitroMass']*df.loc[('05/11/2010',0)]['PltLivingFrac']*500.0
    shootbiomassBarc2009.append(shoot_biomass)
    rootbiomassBarc2009.append(root_biomass)
    nitrogenBarc2009.append(nitrogen_mass)


shootbiomassBarc2010=[]
rootbiomassBarc2010=[]
nitrogenBarc2010=[]
for trt in treatmentList_other:
    TargetDir=baseDir+siteList[1]+'\\'+trt+'\\'+siteList[1]+'.g01'
    df=pd.read_csv(TargetDir)
    df.set_index(['date','       time'], inplace=True)
    shoot_biomass=df.loc[('03/02/2011',0)]['  ShootMass']*df.loc[('03/02/2011',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('03/02/2011',0)]['   RootMass']*df.loc[('03/02/2011',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('03/02/2011',0)]['     NitroMass']*df.loc[('03/02/2011',0)]['PltLivingFrac']*500.0
    shootbiomassBarc2010.append(shoot_biomass)
    rootbiomassBarc2010.append(root_biomass)
    nitrogenBarc2010.append(nitrogen_mass)
    
    shoot_biomass=df.loc[('03/28/2011',0)]['  ShootMass']*df.loc[('03/28/2011',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('03/28/2011',0)]['   RootMass']*df.loc[('03/28/2011',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('03/28/2011',0)]['     NitroMass']*df.loc[('03/28/2011',0)]['PltLivingFrac']*500.0
    shootbiomassBarc2010.append(shoot_biomass)
    rootbiomassBarc2010.append(root_biomass)
    nitrogenBarc2010.append(nitrogen_mass)
    
    shoot_biomass=df.loc[('05/02/2011',0)]['  ShootMass']*df.loc[('05/02/2011',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('05/02/2011',0)]['   RootMass']*df.loc[('05/02/2011',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('05/02/2011',0)]['     NitroMass']*df.loc[('05/02/2011',0)]['PltLivingFrac']*500.0
    shootbiomassBarc2010.append(shoot_biomass)
    rootbiomassBarc2010.append(root_biomass)
    nitrogenBarc2010.append(nitrogen_mass)
    

shootbiomassBarc2011=[]
rootbiomassBarc2011=[]
nitrogenBarc2011=[]
for trt in treatmentList_other:
    TargetDir=baseDir+siteList[2]+'\\'+trt+'\\'+siteList[2]+'.g01'
    df=pd.read_csv(TargetDir)
    df.set_index(['date','       time'], inplace=True)
    shoot_biomass=df.loc[('03/01/2012',0)]['  ShootMass']*df.loc[('03/01/2012',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('03/01/2012',0)]['   RootMass']*df.loc[('03/01/2012',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('03/01/2012',0)]['     NitroMass']*df.loc[('03/01/2012',0)]['PltLivingFrac']*500.0
    shootbiomassBarc2011.append(shoot_biomass)
    rootbiomassBarc2011.append(root_biomass)
    nitrogenBarc2011.append(nitrogen_mass)
    
    shoot_biomass=df.loc[('03/22/2012',0)]['  ShootMass']*df.loc[('03/22/2012',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('03/22/2012',0)]['   RootMass']*df.loc[('03/22/2012',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('03/22/2012',0)]['     NitroMass']*df.loc[('03/22/2012',0)]['PltLivingFrac']*500.0
    shootbiomassBarc2011.append(shoot_biomass)
    rootbiomassBarc2011.append(root_biomass)
    nitrogenBarc2011.append(nitrogen_mass)
    
    shoot_biomass=df.loc[('04/20/2012',0)]['  ShootMass']*df.loc[('04/20/2012',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('04/20/2012',0)]['   RootMass']*df.loc[('04/20/2012',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('04/20/2012',0)]['     NitroMass']*df.loc[('04/20/2012',0)]['PltLivingFrac']*500.0
    shootbiomassBarc2011.append(shoot_biomass)
    rootbiomassBarc2011.append(root_biomass)
    nitrogenBarc2011.append(nitrogen_mass)


shootbiomassLarc2011=[]
rootbiomassLarc2011=[]
nitrogenLarc2011=[]
for trt in treatmentList_other:
    TargetDir=baseDir+siteList[3]+'\\'+trt+'\\'+siteList[3]+'.g01'
    df=pd.read_csv(TargetDir)
    df.set_index(['date','       time'], inplace=True)
    shoot_biomass=df.loc[('03/12/2012',0)]['  ShootMass']*df.loc[('03/12/2012',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('03/12/2012',0)]['   RootMass']*df.loc[('03/12/2012',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('03/12/2012',0)]['     NitroMass']*df.loc[('03/12/2012',0)]['PltLivingFrac']*500.0
    shootbiomassLarc2011.append(shoot_biomass)
    rootbiomassLarc2011.append(root_biomass)
    nitrogenLarc2011.append(nitrogen_mass)
    
    shoot_biomass=df.loc[('04/03/2012',0)]['  ShootMass']*df.loc[('04/03/2012',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('04/03/2012',0)]['   RootMass']*df.loc[('04/03/2012',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('04/03/2012',0)]['     NitroMass']*df.loc[('04/03/2012',0)]['PltLivingFrac']*500.0
    shootbiomassLarc2011.append(shoot_biomass)
    rootbiomassLarc2011.append(root_biomass)
    nitrogenLarc2011.append(nitrogen_mass)
    
    shoot_biomass=df.loc[('05/10/2012',0)]['  ShootMass']*df.loc[('05/10/2012',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('05/10/2012',0)]['   RootMass']*df.loc[('05/10/2012',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('05/10/2012',0)]['     NitroMass']*df.loc[('05/10/2012',0)]['PltLivingFrac']*500.0
    shootbiomassLarc2011.append(shoot_biomass)
    rootbiomassLarc2011.append(root_biomass)
    nitrogenLarc2011.append(nitrogen_mass)


shootbiomassCrsk2011=[]
rootbiomassCrsk2011=[]
nitrogenCrsk2011=[]
for trt in treatmentList_other:
    TargetDir=baseDir+siteList[4]+'\\'+trt+'\\'+siteList[4]+'.g01'
    df=pd.read_csv(TargetDir)
    df.set_index(['date','       time'], inplace=True)
    shoot_biomass=df.loc[('03/07/2012',0)]['  ShootMass']*df.loc[('03/07/2012',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('03/07/2012',0)]['   RootMass']*df.loc[('03/07/2012',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('03/07/2012',0)]['     NitroMass']*df.loc[('03/07/2012',0)]['PltLivingFrac']*500.0
    shootbiomassCrsk2011.append(shoot_biomass)
    rootbiomassCrsk2011.append(root_biomass)
    nitrogenCrsk2011.append(nitrogen_mass)
    
    shoot_biomass=df.loc[('05/10/2012',0)]['  ShootMass']*df.loc[('05/10/2012',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('05/10/2012',0)]['   RootMass']*df.loc[('05/10/2012',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('05/10/2012',0)]['     NitroMass']*df.loc[('05/10/2012',0)]['PltLivingFrac']*500.0
    shootbiomassCrsk2011.append(shoot_biomass)
    rootbiomassCrsk2011.append(root_biomass)
    nitrogenCrsk2011.append(nitrogen_mass)
    
shootbiomassPrss2011=[]
rootbiomassPrss2011=[]
nitrogenPrss2011=[]
for trt in treatmentList_other:
    TargetDir=baseDir+siteList[5]+'\\'+trt+'\\'+siteList[5]+'.g01'
    df=pd.read_csv(TargetDir)
    df.set_index(['date','       time'], inplace=True)
    shoot_biomass=df.loc[('02/28/2012',0)]['  ShootMass']*df.loc[('02/28/2012',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('02/28/2012',0)]['   RootMass']*df.loc[('02/28/2012',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('02/28/2012',0)]['     NitroMass']*df.loc[('02/28/2012',0)]['PltLivingFrac']*500.0
    shootbiomassPrss2011.append(shoot_biomass)
    rootbiomassPrss2011.append(root_biomass)
    nitrogenPrss2011.append(nitrogen_mass)
    
    shoot_biomass=df.loc[('03/19/2012',0)]['  ShootMass']*df.loc[('03/19/2012',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('03/19/2012',0)]['   RootMass']*df.loc[('03/19/2012',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('03/19/2012',0)]['     NitroMass']*df.loc[('03/19/2012',0)]['PltLivingFrac']*500.0
    shootbiomassPrss2011.append(shoot_biomass)
    rootbiomassPrss2011.append(root_biomass)
    nitrogenPrss2011.append(nitrogen_mass)
    
    shoot_biomass=df.loc[('05/21/2012',0)]['  ShootMass']*df.loc[('05/21/2012',0)]['PltLivingFrac']*500.0
    root_biomass=df.loc[('05/21/2012',0)]['   RootMass']*df.loc[('05/21/2012',0)]['PltLivingFrac']*500.0
    nitrogen_mass=df.loc[('05/21/2012',0)]['     NitroMass']*df.loc[('05/21/2012',0)]['PltLivingFrac']*500.0
    shootbiomassPrss2011.append(shoot_biomass)
    rootbiomassPrss2011.append(root_biomass)
    nitrogenPrss2011.append(nitrogen_mass)
    
shootbiomassTotal=shootbiomassBarc2009+shootbiomassBarc2010+shootbiomassBarc2011+shootbiomassLarc2011+shootbiomassCrsk2011+shootbiomassPrss2011
rootbiomassTotal=rootbiomassBarc2009+rootbiomassBarc2010+rootbiomassBarc2011+rootbiomassLarc2011+rootbiomassCrsk2011+rootbiomassPrss2011
nitrogenTotal=nitrogenBarc2009+nitrogenBarc2010+nitrogenBarc2011+nitrogenLarc2011+nitrogenCrsk2011+nitrogenPrss2011