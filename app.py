from flask import Flask
from model import giverec,createmodels
from flask import request
from flask import render_template
import pickle
import json
app = Flask(__name__,template_folder='template')
try:
    model = pickle.load(open('model.pkl','rb'))
    dicte = pickle.load(open('dict.dic','rb'))

except:
    createmodels()
    model = pickle.load(open('model.pkl','rb'))
    dicte = pickle.load(open('dict.dic','rb'))



@app.route('/')
def hello():
    return "Introduce a query!"


@app.route('/',methods=['POST'])
def hello_name():
    data = request.get_json(force=True)
    name=data['name']
    #print(name)
    res  =giverec(model,name,dicte)
    #print(list(res))
    return render_template('template.html', res=res,query=name)


if __name__ == '__main__':
     app.run(debug=True)#, host='0.0.0.0')
