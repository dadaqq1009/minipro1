from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://dadaqq1009:z10091214@cluster0.ooefn7z.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/name')
def lee():
   return render_template('name.html')

@app.route("/name", methods=["POST"])
def web_board_post():
    name_receive = request.form['name_give']
    message_receive = request.form['message_give']

    doc = {
        'name': name_receive,
        'message': message_receive
    }
    db.member_4.insert_one(doc)

    return jsonify({'msg': '기록 완료!'})

@app.route('/board')
def board():
    return render_template('board.html')

@app.route("/boards", methods=["GET"])
def web_board_get():
    guest_list4 = list(db.member_4.find({}, {'_id': False}))

    return jsonify({'guests4':guest_list4})











if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)