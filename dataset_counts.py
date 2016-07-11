# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:21:55 2016

@author: Monika
"""
#import arcpy python site package
import arcpy

#Call the GetCount_management module.
#Count the number of records in a feature class by adding the location.
count = arcpy.GetCount_management(raw_input("Please enter the Feature Class Location below\n-->"))

#Print the total number of records in the feature class. 
print count

