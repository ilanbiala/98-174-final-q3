from tester import *

def deploy():
    if (testAll()):
        print("Deployed")
    else:
        raise Exception("Tests failed, didn't deploy")

deploy()
