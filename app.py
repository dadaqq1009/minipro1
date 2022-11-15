from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://dadaqq1009:z10091214@cluster0.ooefn7z.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('name.html')

@app.route("/name", methods=["POST"])
def web_board_post():
    name_receive = request.form['name_give']
    message_receive = request.form['message_give']

    doc = {
        'name': name_receive,
        'message': message_receive
    }
    db.board.insert_one(doc)

    return jsonify({'msg': '기록 완료!'})



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)