'''
Created on 11 juni 2018

@author: thomasgumbricht
'''

import os
import zipfile
import gzip
import shutil
#import sys


def UnZip(zipFPN,compStr):    
    '''
    '''    
    zipFP = os.path.split(zipFPN)[0]
    tempFP = os.path.join(zipFP,'ziptmp')
    if not os.path.isdir(tempFP):
        os.makedirs(tempFP)
    zipF = zipfile.ZipFile(zipFPN, "r")
    fL =  zipF.namelist()
    dstFPN = False
    #compstr is the string to look for in the zipfile
    for item in fL:
        if compStr in item:
            fN = os.path.split(item)[1]
            source = zipF.open(item)
            dstFPN = os.path.join(tempFP, fN)
            if not os.path.isfile(dstFPN):
                #dest = file(dstFPN, "wb")
                print ('exploding',dstFPN)
                with open(dstFPN, 'wb') as dest:
                    #with source, dest:
                    shutil.copyfileobj(source, dest)
            break

    return dstFPN

def ExploreZip(zipFPN,compStr):    
    '''
    '''    
    zipFP = os.path.split(zipFPN)[0]
    tempFP = os.path.join(zipFP,'ziptmp')
    if not os.path.isdir(tempFP):
        os.makedirs(tempFP)
    zipF = zipfile.ZipFile(zipFPN, "r")
    fL =  zipF.namelist()
    '''
    for f in fL:
        print (f)

    BALLE
    '''
    dstFPN = False
    #compstr is the string to look for in the zipfile
    for item in fL:
        #print ('ext',os.path.splitext(item)[1])
        if os.path.splitext(item)[1] == '.xml':
            print (item)
        if compStr in item or compStr == item:

            fN = os.path.split(item)[1]
            source = zipF.open(item)
            dstFPN = os.path.join(tempFP, fN)
            if not os.path.isfile(dstFPN):
                #dest = file(dstFPN, "wb")
                print ('exploding',dstFPN)
                with open(dstFPN, 'wb') as dest:
                    #with source, dest:
                    shutil.copyfileobj(source, dest)
            break

    return dstFPN

def ExplodeCompleteGranuleZip(zipFPN):    
    '''
    '''    
    zipFP,zipFN = os.path.split(zipFPN)
    tempFP = os.path.join(zipFP,'ziptmp')

    if not os.path.isdir(tempFP):
        os.makedirs(tempFP)
    #Set the SAFE file that shoudl be the result of the explosions
    safeFN = '%(base)s.SAFE' %{'base':os.path.splitext(zipFN)[0]}
    safeFPN = os.path.join(tempFP,safeFN)
    if os.path.exists(safeFPN):
        print ('zipfile already exploded',safeFPN)
        return  safeFPN
    print ('exploding zipfile',zipFPN)
    zipF = zipfile.ZipFile(zipFPN, "r")   
    zipF.extractall(tempFP)
    if os.path.exists(safeFPN):
        return  safeFPN
    else:
        exit('Error in ExplodeCompleteGranuleZip')

def ExplodeGunZip(zipFPN):
    '''Gunzip unzipping
    '''
    dstFPN = os.path.splitext(zipFPN)[0]
    with gzip.open(zipFPN, 'r') as f_in, open(dstFPN, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)