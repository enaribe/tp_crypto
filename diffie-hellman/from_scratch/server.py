import flask
import random

app = flask.Flask(__name__)
# app.run(host='10.153.68.235', debug=True)
#paramettres
p = 23
g = 5

#generer laa cle publique
xa = random.randint(1, p - 1)
PubA = pow(g, xa, p)

@app.route('/key_exchange', methods=['POST'])
def recuperation():
    data = flask.request.json
    # print("data:", data)
    pubC = data['public_key']
    share = pow(pubC, xa, p)
    print("addr : ",flask.request.remote_addr)
    print("share :", share)
    return flask.jsonify({'public_key': PubA})

if __name__ == '__main__':
    app.run(debug=True)
