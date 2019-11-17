# -*- coding: utf-8 -*-
# Moegamat Toffar - OROAFRICA 
# ORO-TOOLS v1.0.0 2019

import rhinoscriptsyntax as rs
import rhinoscript.userinterface as rd
import Rhino
import System.Drawing.Color as col

def ringSizes():
    fingerSizes = {}
    fingerChoice = []   
    startSize = 72
    endSize = 91
    start = 14.5
    h_incr = 0.2 
    
    for x in range(startSize, endSize):
        start += h_incr
        fingerSizes[str(chr(x))] = round(start,2)
        start += h_incr
        fingerSizes[str(chr(x)) + chr(189)] = round(start,2)
    
        fingerChoice.append(chr(x))
        fingerChoice.append(chr(x) + chr(189))
    #debug
    #print(fingerSizes)
    
    
    #listbox
    if fingerChoice:
        try:
            result = rd.ListBox(sorted(fingerChoice),"Select FingerSize","Finger Size","N")
            if result: 
                myLayer = "Finger Size: " + result
                rs.AddLayer(myLayer,col.Brown) 
                rs.CurrentLayer(myLayer)
                rs.CurrentView("front")
                rs.Command("_Circle 0 " + str(fingerSizes.get(result)))
                rs.CurrentLayer("Default")
                rs.LayerLocked(myLayer,True)
                rs.ClearCommandHistory()
                if rs.IsLayer(myLayer):
                    print("\nFinger rail added!")
            else:
                print("\nOperation Aborted")
        except:
           print "Aborted by user"     

if __name__ == "__main__":
    ringSizes()
