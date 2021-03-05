from flask import Flask,render_template,request
import pickle,joblib
model=pickle.load(open('profit.pkl','rb'))
trans=joblib.load('column')
app=Flask(__name__)

@app.route('/') #When the browser is routed towards this local server URL then execute below function
def hello_world():
    return render_template("index.html")

@app.route('/login',methods=["POST"])
def func2():
   ad=request.form['ad']
   ms=request.form['ms']
   rs=request.form['rs']
   state=request.form['s']
   
   """During Prediction we are giving it in form of 2D array 
   [[165349.2........]] .So we would create a variable data 
   and in that data we pass all the value in ordered fashion
   """
   data=[[int(rs),int(ad),int(ms),state]]
   """Transform data to one hot encoding"""
   test=trans.transform(data)
   print(test)
   """Predict on one hot encoded data"""
   pred=model.predict(test)
   print(pred[0])
   return render_template("index.html",y="The Profit is "+str(pred[0]))



if __name__=="__main__":
    app.run(debug=True) #WSGI gives local Server URL
    
 #Whenever we use debug=True we cannot use IDE to run the code we will have to use Anaconda Prompt
 #We will have to run the file from anaconda prompt ..Go to the path where the app folder is saved 
 # with help of cd command
 #Once on reaching required path of app folder just use commmand"