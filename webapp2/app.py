from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np


#model=pickle.load(open('RandomForestModel.pkl','rb'))
app = Flask(__name__)

#pickle_in= open('RandomForestModel.pkl', 'rb')
#Mymodel= pickle.load(pickle_in)



@app.route('/')
def form():
   return render_template('form.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
  # Mymodel.predict(df)
  if request.method == 'POST':
     result = request.form
   #  return render_template("result.html",result = result)

    return jsonify(result.form)

# @app.route('/display', methods=["GET", "POST"])
# def display():
#      return jsonify(request.form)

if __name__ == '__main__':
   app.run(debug = True)