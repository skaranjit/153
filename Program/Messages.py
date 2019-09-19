__author__ = "Suman Karanjit"
__date__ = "04/15/2019"
import sys
import datetime
class Message:
    _numofMessage = 0
    _lastmessageID = 12320
    def __init__(self,DateTime,Content,Recipient):
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
        self._size = sys.getsizeof(Content)
        self._To = Recipient
        self._Read = False
    def __str__(self):
        """
        Description: Will return the formatted string of the attributes
        Precondition: NONE
        PostCondition: NONE
        """
        if self._Read == True:
            status = "Read"
        else:
            status = "Unread"
        strDate = self._DateReceived.strftime("%A,%b %d,%Y %I:%M %p")
        tmp = "\nReceived: {}\nSize:{:^12}\nTO:{:^19s}\nStatus:{:^12}\nContent:\n\
          {:}\n"\
              .format(strDate,\
                      self._size,\
                      self._To,status,self._content)
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
        Description: updates the read attribute to True 
        Precondition: none
        PostCondition: updates the read attribute to True
        """
        self._Read = True

class SMS_Inbox:
    
    def __init__(self):
        """
        Description: Initialize SMS_INBOX object
        Precondition: none
        PostCondition: Initialize messageLists to empty
        """
        self._MessageList = []
        self._numMessagesInBox = len(self._MessageList)
    def addToInbox(self,MessageObject):
        """
        Description: It will append message object to messages list.
        Precondition: MessageObject needs to message Object created from Message class.
        PostCondition: MessageList will be updated  
        """
        
        if MessageObject.getSize() >80:
            sender = MessageObject.getrecipient()
            dateTime = MessageObject.getdateTime()
            tmpContent = MessageObject.getcontent()[0:79]
            tmpContent2 = MessageObject.getcontent()[79:]
            self._MessageList.append(Message(dateTime,tmpContent,sender))
            self._MessageList.append(Message(dateTime,tmpContent2,sender))
        else:
            self._MessageList.append(MessageObject)
        self._numMessagesInBox = len(self._MessageList)
    def deleteMessagebyphone(self,phone):
        """
        Description:  Updates Message List
        Precondition: phone needs to be string
        PostCondition: update messageList and numMessageeInbox
        """
        tmp = []
        for msg in self._MessageList:
            if msg.getrecipient() != phone:
                tmp.append(msg)
        if tmp != []:
            self._MessageList = tmp
        self._numMessagesInBox = len(self._MessageList)
    def deleteMessagebydate(self,daysOld):
        """
        Description:  Updates Message List
        Precondition: daysold needs to be number of days
        PostCondition: update messageList and numMessageeInbox
        """
        print(self._MessageList)
        tmp = []
        today = datetime.datetime.now()
        for msg in self._MessageList:
            
            tmpdays = msg.getdateTime()
            if (today - tmpdays).days <= daysOld:
                tmp.append(msg)
        if tmp != []:
            self._MessageList = tmp        
        self._numMessagesInBox = len(self._MessageList)
    def findMessagebyPhone(self,phone):
        """
        Description: finds the messages by phone
        Precondition: phone should be a string
        PostCondition: None
        """
        tmp = ""
        for msg in self._MessageList:
            if msg.getrecipient() == phone:
                tmp += "\n" + msg.__str__()
        
        if tmp != "":
            return tmp
        else:
            return "None Found"
    def findMessagebyDate(self,dt):
        """
        Description: finds the messages by date
        Precondition: dt needs to be date object 
        PostCondition: none
        """
        tmp = ""
        for msg in self._MessageList:
            if msg.getdateTime() == dt:
                tmp += "\n" + msg.__str__()
        if tmp != "":
            return tmp
        else:
            return "None Found"
    def allBeforeSomeNumDays(self,daysOld):
        """
        Description: finds the messages befor specific days. Returns newlist of found messages
        Precondition: days needs to be number of days
        PostCondition: none 
        """
        tmp = " "
        today = datetime.datetime.now()
        for msg in self._MessageList:
            tmpdays = msg.getdateTime()
            if (today - tmpdays).days >= daysOld:
                tmp += "\n" + msg.__str__()
        if tmp != "":
            return tmp
        else:
            return "None Found"

    def sortedInboxbyDate(self):
        """
        Description: Sort out the messages list by latest date
        Pre Condition: none
        Post Condition: Messages list will be updated.
        """
        self._MessageList.sort(key=lambda x: x.getdateTime(),reverse=True)
        

    def __str__(self):
        """
        Description: Prints out the formatted attributes of sms inbox object.
        Precondition: NONE
        PostCondition: None
        """
        tmp = ""
        for msg in self._MessageList:
            #tmp += msg.__str__()
            tmp += "\nFrom: {} {:^40s}  {}".format(msg.getrecipient()\

                                                  ,msg.getcontent()\
                                                  ,msg.getdateTime())
        return tmp
            
        




