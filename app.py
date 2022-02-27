import joblib
from flask import Flask,redirect,url_for,render_template,request

model = joblib.load(r"model")

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    buy = request.form['buy']
    maint = request.form['maint']
    doors = request.form['doors']
    people = request.form['people']
    lug = request.form['lug']
    safty = request.form['safty']
    prediction = model.predict([[buy,maint,doors,people,lug,safty]])
    prediction = int([prediction][0])
    prediction = ['accurate' ,'good', 'unaccurate', 'very good'][prediction]
    return render_template('predict.html',prediction = prediction)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=2000,debug=True)
