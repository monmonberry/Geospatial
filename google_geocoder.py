# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:43:06 2016

@author: Monika
"""

import csv

from geopy.geocoders import GoogleV3 as google
#import the Google geocoding capability 

locator = google()
address = open(r"geocode.txt", 'r')

# Open Output File
outputFile = open('geocode_out.csv', 'wb')
outputWriter = csv.writer(outputFile)

for a in address:
    if a is None:
        print "Error ",a    
    else:
        result = locator.geocode(a)
        #print result
        if result is None:
            print "no result: ", a
            # write address with no geocode
            outputWriter.writerow([a, '0', '0'])
        else:
            # There is a result so write it to the file
            outputWriter.writerow([result.address, result.longitude, result.latitude])
            print [result.address, result.longitude, result.latitude]

# Close input file
address.close()
# Close output file
outputFile.close()