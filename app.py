from flask import Flask, request, render_template
from joblib import load
from preprocessing import preprocessing

app = Flask(__name__)

model = load('modelo_treinado_fake_recogna.joblib')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        text = request.form['text']
        
        pre_processed_text = preprocessing(text)

        prediction = model.predict_proba([pre_processed_text])

        first_row_percentages = [f"{prob * 100:.0f}%" for prob in prediction[0]]

        return {"Chance de ser fake news": first_row_percentages[1]}

if __name__ == '__main__':
    app.run(debug=True)
