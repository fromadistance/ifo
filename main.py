name = input ("Hello! Welcome to programme centre! What is your name?")
print "OK,%s ,nice to meet you! what else can I help you with?" % (name) 
help = int(input ("enter 1: Check age / enter 2: Check company info / enter 3: Wechat Pay / enter 4: make letters all caps "))
if help == 1:
  age = int(input( "How old are you?" ))
  print "%s, All right,let me see..." %(age)
  if age >0 and age <= 15 : 
         print ("Sorry,%s,You are too young to join us.")% (name)
  elif age > 15 and age <= 40 :
          print ("Cool! you are just old enough to join us!")
  elif age > 40: 
         print ("Hmmmm, I think you are too old, sorry!")
  else: 
    print ("I'm sorry, I cannnot understand.")
elif help == 2:
      print "We are Universal XXX programming Co. "
elif help == 3:
     shop = input ("Which shop you want to pay?")
     print "ok, shop:%s" %(shop)
     money = int(input ("How much yuan you want to pay? "))
     print "Let me check...%s and pay for %s" % (shop , money)
     print "OK, paid. "
elif help == 4:
     letters = input ("enter letters you want to be capped: ")
     print "here is the letters: " + letters.upper()
else:
  print "ERROR, try again please"

