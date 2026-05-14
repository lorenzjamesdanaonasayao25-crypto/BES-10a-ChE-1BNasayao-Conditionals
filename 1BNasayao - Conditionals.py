#This project is a calculator that is based on the amount of moles needed from the user with the usual reagents used in laboratory experiments.
#The reagents that were commonly used in our laboratory experiments as a first year ChE Student are:
#NaOH, NH4OH, KOH, HCl, H2SO4, H3PO4, HNO3, KHP

inyou = input('Hello! Please state your name: ')
inREAG = input('Enter Name of Reagent Needed: ')
inMOL = input('Enter Amount of Moles Needed: ')
#input variables
#inyou is a variable that defines the user's name
#inREAG is a variable that states what reagent is needed by the user
#inMOL is the amount of moles needed from the said reagent


molNaOH = 39.997
molNH4OH = 35.046
molKOH = 56.110
molHCl = 36.458
molH2SO4 = 98.073
molH3PO4 = 97.994
molKHP = 204.22
#The list above shows the molar mass of the usual reagents used in laboratories, especially in titrations.



#conditional functions and calculations
if inREAG == "NaOH":
    xNaOH = float(inMOL)*float(molNaOH)
    print("The amount of grams needed for", inMOL, "M", inREAG, "is", xNaOH)

elif inREAG == "NH4OH":
    xNH4OH = float(inMOL)*float(molNH4OH)
    print("The amount of grams needed for", inMOL, "M", inREAG, "is", xNH4OH)

elif inREAG == "KOH":
    xKOH = float(inMOL)*float(molKOH)
    print("The amount of grams needed for", inMOL, "M", inREAG, "is", xKOH)

elif inREAG == "HCl":
    xHCl = float(inMOL)*float(molHCl)
    print("The amount of grams needed for", inMOL, "M", inREAG, "is", xHCl)

elif inREAG == "H2SO4":
    xH2SO4 = float(inMOL)*float(molH2SO4)
    print("The amount of grams needed for", inMOL, "M", inREAG, "is", xH2SO4)

elif inREAG == "H3PO4":
    xH3PO4 = float(inMOL)*float(molH3PO4)
    print("The amount of grams needed for", inMOL, "M", inREAG, "is", xH3PO4)

elif inREAG == "KHP":
    xKHP = float(inMOL)*float(molKHP)
    print("The amount of grams needed for", inMOL, "M", inREAG, "is", xKHP)

else:
    print("Invalid Reagent Name. Name does not correlate to Inventory")

#The output will show the amount of grams needed to achieve the amount of moles asked by the user for the reagent they needed.