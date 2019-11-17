# -*- coding: utf-8 -*-
# Moegamat Toffar - OROAFRICA 
# ORO-TOOLS v1.0.0 2019

import rhinoscriptsyntax as rs
import rhinoscript.userinterface as rd
import Rhino as rhino

def alloyWeight():
    #alloy density
    density = {"Sterling Silver":0.0105, "18K White":0.0176, "18K Yellow":0.0155,"9K White":0.014, "9K Yellow":0.012, "Platinum":0.0215}
    
    #create option list
    alloy = []
    for y in density:
        alloy.append(y)
    try:
        #select object
        objs = rs.GetObject("Select PolySurfaces",rs.filter.polysurface)
        #check for naked edges
        if not rs.IsObjectSolid(objs):
            rs.ClearCommandHistory() 
            print("\nPolySurface not solid")
            return
        #check for valid selection
        if objs:
            choice = rd.ListBox(alloy,"Select Alloy","Alloys")
            wgt = round(rs.SurfaceVolume(objs)[0] * density.get(choice),2) 
            rs.ClearCommandHistory() 
            print("\nVolume: " + str(round(rs.SurfaceVolume(objs)[0],2)) + " amounts to " + str(wgt) + "g of " + choice) 
        else:
            rs.ClearCommandHistory()
            print("\nNo valid PolySurface Selected!")   
    except:
        print "Operation Aborted"
        Rhino.Commands.Result.Cancel

if __name__ == "__main__":
    alloyWeight()
