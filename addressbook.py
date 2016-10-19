"""AddressBook class, and all basic operate.

Author:dijunzhou@gmail.com"""

import os
import pickle
from jsonutils import *
from person import Person

datafilename = "data.dat"
menu = {'a':'Add', 'm':'Modify', 'd':'Delete', 'v':'View', 'l':'List'}

class addrbook:
  """AddresBook main frame.

  Add,Save,Modify,Delete,List,etc      
  """
  def __init__(self):
    os.system("title AddressBook")
    if os.path.isfile(datafilename):
      try:
        self.ABDict = jsonfile2python(datafilename)
      except Exception, e:
        self.ABDict = {}
    else:
      self.ABDict = {}

  def ShowMenu(self):
    print "Menu:\r\n" \
          "a. Add a new person\r\n" \
          "m. Modify a person\r\n" \
          "d. Delete a person\r\n" \
          "v. View a person\r\n" \
          "l. List all person\r\n" \
          "q. Quit\r\n"
    c = raw_input("please enter your choice:")
    if c in menu.keys():
      getattr(self, menu[c])()
    elif c == "q":
      exit()
    else:
      print "No this choice"  

  def Add(self, modifyName=""):
    name = raw_input("Input name:")
    phone = raw_input("Input phone:")  
    birthday = raw_input("Input birthday:")  
    email = raw_input("Input email:")  
    address = raw_input("Input address:")  
    postcode = raw_input("Input postcode:")  
    remark = raw_input("Input remark:")
    if modifyName != "" and modifyName != name:
      print "delete " + modifyName
      del self.ABDict[modifyName]
    d = Person.PersonDict(name, phone, birthday, email, address, postcode, remark)
    self.ABDict.update({name:d})
    self.Save()

  def Modify(self):
    name = raw_input("input view name:")
    if name in self.ABDict.keys():
      self.Add(name)
    else:
      print('No person info about {0}'.format(name))

  def Delete(self):
    name = raw_input("input view name:")
    if name in self.ABDict.keys():
      p = self.ABDict[name]
      print Person.PersonInfo(p)
      del self.ABDict[name]
      self.Save()
      print "Delete " + name + " success!"
    else:
      print('No person info about {0}'.format(name))

  def View(self):
    name = raw_input("input view name:")
    if name in self.ABDict.keys():
      p = self.ABDict[name]
      print Person.PersonInfo(p)
    else:
      print('No person info about {0}'.format(name)) 

  def List(self):
    if len(self.ABDict) > 0:
      print "name\tphone\tbirthday\temail\taddress\tpostcode\tremark"
    for v in self.ABDict.values():
      print Person.PersonInfoEx(v)
        
  def Save(self):
    python2jsonfile(self.ABDict, datafilename)

if __name__ == "__main__":
  ab = addrbook()
  while True:
    ab.ShowMenu()
