from tester import testAll

def deploy():
    try:
        testAll()
    except AssertionError:
        raise Exception("Tests failed, didn't deploy")
    else:
        print("Deployed")
