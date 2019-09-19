from Messages import *

Msg1 =Message(datetime.datetime(2019,3,29,1,14),"This is a test Message","Nepun")
print(Msg1)
Msg2 =Message(datetime.datetime(2019,3,30,11,14),"This is a test Message","218-790-1234")
Msg3 =Message(datetime.datetime(2019,3,10,15,14),"This is a test Message.This message is intended to be long so that the program will divide into two messages in the sms Inbox.","2187900592")
Msg4 =Message(datetime.datetime(2019,3,20,11,14),"This is a test Message","Suman")
Msg5 =Message(datetime.datetime(2019,3,20,11,14),"This is a test Message","Suman")
Msg6 =Message(datetime.datetime(2019,3,20,11,14),"This is a test Message","Suman")


MyInbox = SMS_Inbox()
MyInbox.addToInbox(Msg1)
print("#################SMS INBOX###############")

MyInbox.addToInbox(Msg2)
MyInbox.addToInbox(Msg3)
MyInbox.addToInbox(Msg4)
MyInbox.addToInbox(Msg5)
MyInbox.addToInbox(Msg6)


print(MyInbox)
print("#############################################")

print("\n##############Find Message by date###################")
print(MyInbox.findMessagebyDate(datetime.datetime(2019,3,11,12,14)))
print(MyInbox.findMessagebyDate(datetime.datetime(2019,3,10,11,14)))

print("###############################################################")


print("\n##############Find Message by Phone###################")
print(MyInbox.findMessagebyPhone("asd"))

print("###############################################################")

print("\n##############Find Message by befor x Days###################")

print(MyInbox.allBeforeSomeNumDays(30))



print("###############################################################")
MyInbox.sortedInboxbyDate()
print("\n\nSorted Inbox by date:")
print(MyInbox)
print("###############################################################")

print("\n##############Delete Message by Phone###################")

MyInbox.deleteMessagebyphone("Suman")
print(MyInbox)

print("###############################################################")
print("\n##############Delete Message that are x days old###################")

MyInbox.deleteMessagebydate(20)
print(MyInbox)

print("######################################################################")


