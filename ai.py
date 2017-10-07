from flask import Flask, request
from structs import *
import json

app = Flask(__name__)

def create_action(action_type, target):
    actionContent = ActionContent(action_type, target.__dict__)
    return json.dumps(actionContent.__dict__)

def create_move_action(target):
    return create_action("MoveAction", target)

def deserialize_map(serialized_map):
    """
    Fonction utilitaire pour comprendre la map
    """
    serialized_map = serialized_map[1:]
    rows = serialized_map.split('[')
    column = rows[0].split('{')
    deserialized_map = {}

    for i in range(len(rows)):
        column = rows[i + 1].split('{')

        for j in range(len(column)):
            infos = column[j + 1].split(',')
            deserialized_map[i] = Tile(int(infos[0]), int(infos[1]), int(infos[2][:infos[2].find('}')]))

    return deserialized_map

def bot():
    """
    Main de votre bot.
    """
    #data = request.data
    #data = json.loads(data)
    #serialized_map = data["Map"]
    #deserialized_map = deserialize_map(serialized_map)

    return create_move_action(Point(0,1))

@app.route("/", methods=["POST"])
def reponse():
    """
    Point d'entree appelle par le GameServer
    """
    print "RECEIVED"
    return bot()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
