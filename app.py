from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the pre-trained model using pickle
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Crop mapping
crop_mapping = {
    'Arecanut': 0, 'Arhar/Tur': 1, 'Castor seed': 2, 'Coconut': 3, 'Cotton(lint)': 4,
    'Dry chillies': 5, 'Gram': 6, 'Jute': 7, 'Linseed': 8, 'Maize': 9,
    'Mesta': 10, 'Niger seed': 11, 'Onion': 12, 'Other Rabi pulses': 13, 'Potato': 14,
    'Rapeseed & Mustard': 15, 'Rice': 16, 'Sesamum': 17, 'Small millets': 18, 'Sugarcane': 19,
    'Sweet potato': 20, 'Tapioca': 21, 'Tobacco': 22, 'Turmeric': 23, 'Wheat': 24,
    'Bajra': 25, 'Black pepper': 26, 'Cardamom': 27, 'Coriander': 28, 'Garlic': 29,
    'Ginger': 30, 'Groundnut': 31, 'Horse-gram': 32, 'Jowar': 33, 'Ragi': 34,
    'Cashewnut': 35, 'Banana': 36, 'Soyabean': 37, 'Barley': 38, 'Khesari': 39,
    'Masoor': 40, 'Moong(Green Gram)': 41, 'Other Kharif pulses': 42, 'Safflower': 43,
    'Sannhamp': 44, 'Sunflower': 45, 'Urad': 46, 'Peas & beans (Pulses)': 47,
    'Other oilseeds': 48, 'Other Cereals': 49, 'Cowpea(Lobia)': 50, 'Oilseeds total': 51,
    'Guar seed': 52, 'Other Summer Pulses': 53, 'Moth': 54
}

# Season mapping
season_mapping = {
    'Whole Year': 0, 'Kharif': 1, 'Rabi': 2, 'Autumn': 3, 'Summer': 4, 'Winter': 5
}

# State mapping
state_mapping = {
    'Assam': 0, 'Karnataka': 1, 'Kerala': 2, 'Meghalaya': 3, 'West Bengal': 4,
    'Puducherry': 5, 'Goa': 6, 'Andhra Pradesh': 7, 'Tamil Nadu': 8, 'Odisha': 9,
    'Bihar': 10, 'Gujarat': 11, 'Madhya Pradesh': 12, 'Maharashtra': 13, 'Mizoram': 14,
    'Punjab': 15, 'Uttar Pradesh': 16, 'Haryana': 17, 'Himachal Pradesh': 18, 'Tripura': 19,
    'Nagaland': 20, 'Chhattisgarh': 21, 'Uttarakhand': 22, 'Jharkhand': 23, 'Delhi': 24,
    'Manipur': 25, 'Jammu and Kashmir': 26, 'Telangana': 27, 'Arunachal Pradesh': 28, 'Sikkim': 29
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    return render_template('prediction.html')

@app.route('/submit', methods=['POST'])
def submit():
    Crop = (request.form['Crop'])
    Crop_Year = int(request.form['Crop_Year'])
    Season = (request.form['Season'])
    State = (request.form['State'])
    Annual_Rainfall = float(request.form['Annual_Rainfall'])
    Fertilizer = float(request.form['Fertilizer'])
    Pesticide = float(request.form['Pesticide'])
    crop_encoded = crop_mapping.get(Crop)
    season_encoded = season_mapping.get(Season)
    state_encoded = state_mapping.get(State)

    prediction_input = [[crop_encoded, Crop_Year, season_encoded, state_encoded, Annual_Rainfall, Fertilizer, Pesticide]]


    prediction_result = model.predict(prediction_input)
    #Return the prediction result
    # return f"Crop yield prediction result: {prediction_result}"
    return render_template('prediction.html',prediction_text=prediction_result)



if __name__ == '__main__':
    app.run(port=8000)

