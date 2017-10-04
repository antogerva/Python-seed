from flask import Flask
from structs import Tile
app = Flask(__name__)


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
            deserialized_map[i] = Tile(int(infos[0]), int(infos[1]), int(infos[2].[0, infos[2].find('}')]))

    return deserialized_map

def bot():
    """
    Main de votre bot.
    """
    return "TO BE IMPLEMENTED"

@app.route("/", methods=["POST"])
def reponse():
    """
    Point d'entree appelle par le GameServer
    """
    return bot()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5030)
