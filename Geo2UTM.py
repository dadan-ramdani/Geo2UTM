#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 15:26:23 2022

@author: dell
"""

from osgeo import ogr,osr

Zone=48
S_N='S'
if S_N=='N':
    nEPSG=32600+Zone
else:
    nEPSG=32700+Zone
InSRS = osr.SpatialReference()
InSRS.ImportFromEPSG(4326)       # WGS84/Geographic
OutSRS = osr.SpatialReference()
OutSRS.ImportFromEPSG(nEPSG)     # WGS84 UTM Zone 48 South
Point = ogr.Geometry(ogr.wkbPoint)

Point.AddPoint(-6.1141, 105.4077) # use your coordinates here
Point.AssignSpatialReference(InSRS)    # tell the point what coordinates it's in
try:
    Point.TransformTo(OutSRS)
except:
    print("An exception occurred")              # project it to the out spatial reference
x1=Point.GetX()
y1=Point.GetY()
print('{}, {}'.format(x1,y1))