import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def render(game, current):
    '''Display the Current Location'''
    print("you are at {}\n".format(game["rooms"][current]["name"]))
    print(game["rooms"][current]["desc"]+"\n")
    return True

def checkInput():
    '''Check for User Input'''
    response = input("What would you like to do?\n")
    return response

def update(response, game, current):
    '''Update the State of the Game'''
    for i in game["rooms"][current]["exits"]:
        if i["verb"] == response:
            current = i["target"]
    return current

def main():
    game = {}
    with open('zork.json') as json_file:
        game = json.load(json_file)
    # Your game goes here!

    current = 'WHOUS'


    quit = False
    while not quit:
        render(game, current)
        current = update(checkInput(),game,current)

    return True



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()