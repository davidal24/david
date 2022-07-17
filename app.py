from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model_dt_tubes.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    Age, Job, Marital, Education, Default, Housing, Loan, Contact, Month, Day_of_week, Duration, Campaign, Pdays, Previous, Poutcome = [x for x in request.form.values()]

    data = []

    data.append(int(Age))
    data.append(int(Job))
    data.append(int(Marital))
    data.append(int(Education))
    data.append(int(Default))
    data.append(int(Housing))
    data.append(int(Loan))
    data.append(int(Contact))
    data.append(int(Month))
    data.append(int(Day_of_week))
    data.append(int(Duration))
    data.append(int(Campaign))
    data.append(int(Pdays))
    data.append(int(Previous))
    data.append(int(Poutcome))


    prediction = model.predict([data])
    if prediction==1 :
        output = "Bayar"
    else:
        output = " Gagal Bayar"

    return render_template('index.html', prediction=output, Age=Age, Job=Job, Marital=Marital, Education=Education, Default=Default, Housing=Housing, Loan=Loan, Contact=Contact, Month=Month, Day_of_week=Day_of_week, Duration=Duration, Campaign=Campaign, Pdays=Pdays, Previous=Previous, Poutcome=Poutcome)


if __name__ == '__main__':
    app.run(debug=True)
