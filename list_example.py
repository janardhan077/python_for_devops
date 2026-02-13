a =[ 100, True,4.5 ] #this is one type of list 
print (type(a))
print(a)
a.append (False)
print(a)
clouds = list() #other type of the list make
print (type(clouds))
clouds.append("aws")
clouds.append("gcp")
clouds.append("utho")
clouds.append("azure")
clouds.append("imb")
print(clouds)
print (" the lenth of list is:",len(clouds))
print (" the leading cloud provider is :",clouds[0])
print ("the indian best cloud provider is : ",clouds[2])
print (clouds.pop.__doc__)
print (clouds.sort.__doc__)
print (dir(clouds))

for  clouds in clouds:
    if clouds== "utho":
       print ("this is a good indian cloud :",clouds)
    elif clouds == "aws":
        print("the leading one cloud:",clouds)
    elif clouds == ("gcp","azure"):
        print("one of the best clouds in the market :",clouds )
    else :
        print ("sry didnt get any knowledge about that clould : ",clouds)
       
print (clouds)
ans = input("enter the best cloud u think  in this ")
while ans!="aws":
    print("your anser is wrong plz try again")
    ans = input("enter the best cloud u think  in this :")
