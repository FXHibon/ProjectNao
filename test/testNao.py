from naoqi import ALProxy

__author__ = 'fx'

NAO_ADDRESS = "127.0.0.1"
NAO_PORT = 52961

tts = ALProxy("ALTextToSpeech", NAO_ADDRESS, NAO_PORT)
motion = ALProxy("ALMotion", NAO_ADDRESS, NAO_PORT)
motion.setStiffnesses("Body", 1.0)


def say(text):
    """
    Make Nao say text
    :param text: Text to speak
    """
    print("say(", text, ")")
    tts.say(text)


def moveTo(x, y, theta, async=False):
    """
    Move Nao
    :param x: Distance along the X axis in meters
    :param y: Distance along the Y axis in meters
    :param theta: Rotation around the Z axis in radians [-3.1415 to 3.1415]
    :param async: background call or not
    """
    print("moveTo(", y, ", ", y, ", ", theta, ", ", async, ")")
    motion.moveInit()

    if async:
        taskId = motion.post.moveTo(x, y, theta)
        print("taskId = ", taskId)
        return taskId
    else:
        motion.moveTo(x, y, theta)


def stopMove():
    motion.stopMove()


if __name__ == '__main__':

    print("Enter stop to exit")
    input = raw_input("$ ")
    while input != "stop":
        input = raw_input("$ ")
        eval(input)