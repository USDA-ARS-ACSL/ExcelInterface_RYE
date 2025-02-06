# -*- coding: utf-8 -*-
"""
Created on Mon May  1 16:51:46 2023

@author: Zhuangji.Wang
"""

import concurrent.futures
import subprocess as sp
import os

os.chdir(r'D:\Ryesim\Soil Source\x64\release')


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:  
        files=[
#BARC2009
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2009\N_00\runBARC2009.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2009\N_10\runBARC2009.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2009\N_20\runBARC2009.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2009\N_40\runBARC2009.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2009\N_60\runBARC2009.dat',
#BARC2010
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_00\runBARC2010.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_01\runBARC2010.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_02\runBARC2010.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_10\runBARC2010.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_11\runBARC2010.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_12\runBARC2010.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_20\runBARC2010.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_21\runBARC2010.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_22\runBARC2010.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_30\runBARC2010.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_31\runBARC2010.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_32\runBARC2010.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_50\runBARC2010.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_51\runBARC2010.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2010\N_52\runBARC2010.dat',
#BARC2011
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_00\runBARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_01\runBARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_02\runBARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_10\runBARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_11\runBARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_12\runBARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_20\runBARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_21\runBARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_22\runBARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_30\runBARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_31\runBARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_32\runBARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_50\runBARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_51\runBARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\BARC2011\N_52\runBARC2011.dat',
#LARC2011
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_00\runLARC2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_01\runLARC2011.dat', 
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_02\runLARC2011.dat', 
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_10\runLARC2011.dat', 
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_11\runLARC2011.dat', 
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_12\runLARC2011.dat', 
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_20\runLARC2011.dat', 
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_21\runLARC2011.dat', 
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_22\runLARC2011.dat', 
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_30\runLARC2011.dat', 
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_31\runLARC2011.dat', 
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_32\runLARC2011.dat', 
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_50\runLARC2011.dat', 
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_51\runLARC2011.dat', 
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\LARC2011\N_52\runLARC2011.dat', 
#CRSK2011          
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_00\runCRSK2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_01\runCRSK2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_02\runCRSK2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_10\runCRSK2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_11\runCRSK2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_12\runCRSK2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_20\runCRSK2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_21\runCRSK2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_22\runCRSK2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_30\runCRSK2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_31\runCRSK2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_32\runCRSK2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_50\runCRSK2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_51\runCRSK2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\CRSK2011\N_52\runCRSK2011.dat',              
#PRSS2011
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_00\runPRSS2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_01\runPRSS2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_02\runPRSS2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_10\runPRSS2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_11\runPRSS2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_12\runPRSS2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_20\runPRSS2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_21\runPRSS2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_22\runPRSS2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_30\runPRSS2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_31\runPRSS2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_32\runPRSS2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_50\runPRSS2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_51\runPRSS2011.dat',
               r'2DRyeSim.exe D:\Ryesim\CALIBRATION_EXAMPLE\PRSS2011\N_52\runPRSS2011.dat'
               ]
        results=executor.map(sp.run, files)
        
        

        
        