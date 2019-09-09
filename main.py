import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def render():
    '''Display the Current Location'''
    return True

def update():
    '''Update the Game State'''
    return True

def checkInput():
    '''Check for User Input'''
    response = input("What will you do?")
    return response

def main():
    game = {}
    with open('zork.json') as json_file:
        game = json.load(json_file)
    # Your game goes here!

    current = 'WHOUS'


    quit = False
    while not quit:
        render()
        checkInput()
        update()

    return True



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()