from flask import Flask, render_template, request
import numpy as np
import pickle
app=Flask(_name_)
model=pickle.load(open(r'rdf.pkl','rb'))
scale=pickle.load(open(r'scale1.pkl','rb'))
@app.route('/')#rendering the html template
def home():
  return render_template('home.html')
@app.route('/submit',methods=["POST","GET"])
def submit():
 input_feature=[int(x) for x in request.form.values()]
#input_feature=np.transpose(input_feature)
input_feature=[np.array(input_feature)]
print(input_feature)
names=['Gender','Married','Dependents','Education','Self_employed','ApplicantIncome','CoApplicantIncome','LoanAmount','Loan_Amount_term','Credit_History','Property_Area']
data=pandas.DataFrame(input_feature,columns=names)
print(data)
prediction=model.predict(data)
print(prediction)
prediction=int(prediction)
print(type(prediction))
if (prediction==0):
   print (render_template("output.html",result="loan will not be approved"));
else:
   print (render_template("output.html",result="loan will be approved"));
if_name_=="_main_";
#app.run(host='0.0.0.0',port=8000,debug=True)
port=int(os.environ.get('PORT',5000))
app.run(debug=False)