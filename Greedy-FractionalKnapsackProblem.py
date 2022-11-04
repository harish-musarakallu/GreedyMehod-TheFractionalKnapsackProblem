#!/usr/bin/env python
# coding: utf-8

# In[38]:


import sys

#Ammunation object contain the fields
class Ammunation:  
  def __init__(self, name, weight, damage):
    self.name = name
    self.weight = int(weight)
    self.damage = int(damage)
    self.ratio = self.damage/self.weight
    self.fraction = 0


# In[39]:


weapons = 0
MaxWeight = 0
WeaponList = []
fileUpdate = open("inputPS07Q2.txt","r")
lines = fileUpdate.readlines();
for line in lines:
    tagFetch = line.split(":")
    weaponInfo = line.split("/")
    if len(weaponInfo) == 3:       
        ammu = Ammunation (weaponInfo[0].strip(), weaponInfo[1].strip(), weaponInfo[2].strip())
        WeaponList.append(ammu)       
    elif len(tagFetch) == 2 and tagFetch[0].strip() == "Weapons":
        weapons = int(tagFetch[1].strip())
    elif len(tagFetch) == 2 and tagFetch[0].strip()  == "MaxWeight":
        MaxWeight = int(tagFetch[1].strip())


# In[40]:


def greedyAlgorithm ( weaponsList, maxWeight ) :
    fileOut = open("outputPS07Q2.txt","a")
    #sorting
    newlist = sorted(weaponsList, key=lambda x: x.ratio, reverse=True)
    rc = MaxWeight
    totaldamage = 0
    for weapon in newlist:
        if weapon.weight <= rc:
            weapon.fraction = 1
            totaldamage = totaldamage + weapon.damage
            rc = rc - weapon.weight
        elif weapon.weight >= rc:
            weapon.fraction = rc/weapon.weight
            totaldamage = totaldamage + weapon.damage * weapon.fraction
            rc = 0
        
    fileOut.write("Total Damage: {}\n".format( totaldamage ))
    fileOut.write("Ammunation Packs Selection Ratio\n")
    for weapon in weaponsList:
        fileOut.write("{0} > {1}\n".format( weapon.name, weapon.fraction ))
    


# In[41]:


greedyAlgorithm (WeaponList, MaxWeight)


# In[ ]:




