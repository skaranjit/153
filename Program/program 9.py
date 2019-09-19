__author__ = "Suman Karanjit"
__date__ = "04/15/2019"
import sys
import datetime
from datetime import *
class Message:
    _numofMessage = 0
    _lastmessageID = 12320
    def __init__(self,DateTime,Sender,Content,Recipient):
        """
        Description: Initialize the attributes of message object 
        Precondition: DateTime needs to be date object, sender needs to be string,content needs to be string,Recipient needs to be string.
        PostCondition: Initialize the attributes 
        """
        Message._numofMessage += 1
        Message._lastmessageID += 1
        self._messageID = Message._lastmessageID
        self._DateReceived = DateTime
        self._content = Content
        self._From = Sender
        self._size = sys.getsizeof(Content)
        self._To = Recipient
        self._Read = False
    def __str__(self):
        """
        Description: Will return the formatted string of the attributes
        Precondition: NONE
        PostCondition: NONE
        """
        tmp = "Received: {}\nSize:{:^12}\nTO:{:^19s}\nFrom:{:^15s}\nContent:\n\
          {:}"\
              .format(self._DateReceived,\
                      self._size,self._From,\
                      self._To,self._content)
        return tmp
    def getdateTime(self):
        """
        Description: Will return dateTime atribute of message object
        Precondition: None
        PostCondition: None
        """
        return self._DateReceived
    def getsender(self):
        """
        Description: Will return sender attribute of message object
        Precondition: None
        PostCondition: None
        """
        return self._From
    def getrecipient(self):
        """
        Description: will return recipient attribute of message object.
        Precondition:None
        PostCondition: None
        """
        return self._To
    def getmessageID(self):
        """
        Description: Will return message id attribute
        Precondition:None
        PostCondition: None
        """
        return self._messageID
    def getcontent(self):
        """
        Description: will return content attribute
        Precondition: none
        PostCondition: none
        """
        return self._content
    def getSize(self):
        """
        Description:
        Precondition:
        PostCondition: 
        """
        return self._size
    def getnumofMessage():
        """
        Description:return numofMessage attribute
        Precondition:None
        PostCondition: None
        """
        return Message._numofMessage
    def getRead(self):
        """
        Description: returns Read (boolean value)
        Precondition: none
        PostCondition:  None
        """
        return self._Read
    def setRead(self):
        """
        Description:
        Precondition: none
        PostCondition: none
        """
        self._Read = True

class SMS_Inbox:
    
    def __init__(self):
        """
        Description:
        Precondition:
        PostCondition: 
        """
        self._MessageList = []
        self._numMessagesInBox = len(self._MessageList)
    def addToInbox(self,MessageObject):
        """
        Description:
        Precondition:
        PostCondition: 
        """
        self._MessageList.append(MessageObject)
        self._numMessagesInBox = len(self._MessageList)
    def deleteMessagebyphone(self,phone):
        """
        Description:
        Precondition:
        PostCondition: 
        """
        tmp = self._MessageList
        for msg in self._MessageList:
            if msg.getrecipient() == phone:
                tmp.remove[msg]
        self._MessageList = tmp
        self._numMessagesInBox = len(self._MessageList)
    def deleteMessagebydate(self,daysOld):
        """
        Description:
        Precondition:
        PostCondition: 
        """
        tmp = self._MessageList
        for msg in tmp:
            if msg.getdateTime().days <= daysOld:
                self._MessageList.remove[msg]
        self._numMessagesInBox = len(self._MessageList)
    def findMessagebyPhone(self,phone):
        """
        Description: finds the required phone
        Precondition: phone should be a string
        PostCondition: None
        """
        phone = input("Find Message From: ")
        tmp = []
        for msg in self._MessageList:
            if msg.getrecipient(self) == phone:
                tmp.append(msg)
        if tmp != []:
            return tmp
        else:
            return "None Found"
    def findMessagebyDate(self,dt):
        """
        Description:
        Precondition:
        PostCondition: 
        """
        tmp = []
        for msg in self._MessageList:
            if msg.getdateTime() == dt:
                print(msg)
        
    def allBeforeSomeNumDays(self,days):
        """
        Description:
        Precondition:
        PostCondition: 
        """
        tmp = []
        for msg in self._MessageList:
            if msg.getdateTime(self).days <= daysOld:
                tmp.append(msg)
        return tmp
     
        
    def __str__(self):
        """
        Description:
        Precondition:
        PostCondition: 
        """
        tmp = ""
        for msg in self._MessageList:
            tmp += "\nFrom: {}{:^40s}{}".format(msg.getrecipient()\
                                                  ,msg.getcontent()\
                                                  ,msg.getdateTime())
        return tmp
            
        




