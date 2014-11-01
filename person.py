"""Person class."""
from collections import OrderedDict

class Person:
  @staticmethod
  def PersonDict(name, phone, birthday, email, address, postcode, remark):
    # return {"name":name, "phone":phone, "birthday":birthday, "email":email, 
    #   "address":address, "postcode":postcode, "remark":remark}
    return OrderedDict([("name",name), ("phone",phone), ("birthday",birthday), ("email",email), 
      ("address",address), ("postcode",postcode), ("remark",remark)])

  @staticmethod
  def PersonInfo(dict):
    info = "name\tphone\tbirthday\temail\taddress\tpostcode\tremark\r\n"
    info += "%s\t%s\t%s\t%s\t%s\t%s\t%s\r\n"\
      % (dict["name"], dict["phone"], dict["birthday"], dict["email"], 
         dict["address"], dict["postcode"], dict["remark"])
    return info  

  @staticmethod
  def PersonInfoEx(dict):
    return "%s\t%s\t%s\t%s\t%s\t%s\t%s"\
      % (dict["name"], dict["phone"], dict["birthday"], dict["email"], 
         dict["address"], dict["postcode"], dict["remark"])