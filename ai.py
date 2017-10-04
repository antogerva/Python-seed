from flask import Flask
app = Flask(__name__)

def deserialize_map(serialized_map):
    """
    Fonction utilitaire pour comprendre la map
    """

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
