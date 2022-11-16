from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://dadaqq1009:z10091214@cluster0.ooefn7z.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('board.html')

# @app.route("/board", methods=["GET"])
 #def web_board_get():
   # guest_list1 = list(db.member_1.find({}, {'_id': False}))

    #return jsonify({'guests1':guest_list1})

#@app.route("/board", methods=["GET"])
#def web_board_get():
    #guest_list2 = list(db.member_2.find({}, {'_id': False}))

    #return jsonify({'guests2':guest_list2})

#@app.route("/board", methods=["GET"])
#def web_board_get():
    #guest_list3 = list(db.member_3.find({}, {'_id': False}))

    #return jsonify({'guests3':guest_list3})


@app.route("/board", methods=["GET"])
def web_board_get():
    guest_list4 = list(db.member_4.find({}, {'_id': False}))

    return jsonify({'guests4':guest_list4})

#@app.route("/board", methods=["GET"])
#def web_board_get():
    #guest_list5 = list(db.member_5.find({}, {'_id': False}))

    #return jsonify({'guests5':guest_list5})



if __name__ == '__main__':
   app.run('0.0.0.0', port=5001, debug=True)