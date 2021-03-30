from flask import Flask,request,jsonify,render_template,url_for
from sthree import return_resource


app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return 'shree is working'

@app.route('/s3')
def hello_world():
    fname = request.args['surl']
    return jsonify(return_resource(fname))

@app.route('/s3g')
def s3_gui():
    return render_template('sthree.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000,debug=True)
