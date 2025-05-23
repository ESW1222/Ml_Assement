from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the pre-trained model
with open('model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    temp_input = data.get("temperature")
    
    # Assuming model takes temperature as input
    prediction = model.predict([[temp_input]])
    return jsonify({"prediction": prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/')
def home():
    return "Welcome to my ML API!"
