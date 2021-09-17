import paho.mqtt.client as mqtt

#connections params
mqttServer = "192.168.1.17" 
topic = "topic/topic"
#for save data into a .dat file
msgCount = 0
fileName = 'report.dat'
file = open(fileName,'w')
file.close()  

def on_connect(client, userdata, flags, rc): #connect function
    print("Connection/result code: "+str(rc))

    client.subscribe(topic)#subscribe topic

    return()

def on_message(client, userdata, msg): #when the topic has a message
    global msgCount
    print('\n'+'New message -> '+msg.topic+" "+str(msg.payload)) #print the topic and payload
    msgToFile = msg.topic+" "+str(msg.payload) +'\n' #msg to variable for write it in a file

    file = open(fileName,'a')#open the file for write
    file.write(msgToFile)
    
    msgCount += 1
    print('\nmessages recived: ', msgCount)

    return()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqttServer, 1883, 60)
client.username_pw_set(username="prueba", password="prueba") #set the user and pass of the broker
client.loop_forever()