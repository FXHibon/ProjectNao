from naoqi import ALProxy

__author__ = 'fx'

NAO_ADDRESS = "172.16.6.117"
NAO_PORT = 9559
"""
This example shows how to use ALRedBallTracker.
It is launched for a little while, then stopped.
"""

from naoqi import ALProxy, ALModule, ALBroker


class BallDetector(ALModule):
    def __init(self, name):
        print("__init__")
        ALModule.__init__(self, name)

    def onBallDetected(self, key, value, message):
        print("ball detected: " + key + ", " + value + ", " + message)


IP = "172.16.6.117"
PORT = 9559

print "Connecting to", IP, "with port", PORT
myBroker = ALBroker("myBroker",
                    "0.0.0.0",  # listen to anyone
                    0,  # find a free port and use it
                    IP,  # parent broker IP
                    PORT)  # parent broker port

motion = ALProxy("ALMotion", IP, PORT)
redBallTracker = ALProxy("ALRedBallTracker", IP, PORT)
memory = ALProxy("ALMemory", IP, PORT)

ballDetector = BallDetector("BallDetector")
memory.subscribeToEvent("redBallDetected", "ballDetector", "onBallDetected")

# First, set Head Stiffness to ON.
motion.setStiffnesses("Head", 1.0)

# Then, start tracker.
redBallTracker.startTracker()

print "ALRedBallTracker successfully started, now show a red ball face !"

# Wait an input
input()

# Stop tracker and remove head stiffness.
redBallTracker.stopTracker()
motion.setStiffnesses("Head", 0.0)

print "ALRedBallTracker stopped."