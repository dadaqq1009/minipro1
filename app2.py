from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://dadaqq1009:z10091214@cluster0.ooefn7z.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('board.html')

@app.route("/board", methods=["POST"])
def web_board_post():

    return jsonify({'msg': '기록 완료!'})

@app.route("/board", methods=["GET"])
def web_board_get():
    guest_list = list(db.board.find({}, {'_id': False}))

    return jsonify({'guests':guest_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5001, debug=True)