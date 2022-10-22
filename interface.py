import re
from flask import Flask, jsonify,request
import config
from project_data.utils import Vehicle_Price

app = Flask(__name__)


@app.route('/') 
def hello_flask():
    return "WELCOME"
    
@app.route('/predict_charges')
def get_Vehicle_price():
    
    data=request.form
       
    AccelSec = eval(data['AccelSec'])
    TopSpeed_KmH = eval(data['TopSpeed_KmH'])
    Range_Km = eval(data['Range_Km'])
    Efficiency_WhKm = eval(data['Efficiency_WhKm'])
    FastCharge_KmH = eval(data['FastCharge_KmH'])
    RapidCharge = data['RapidCharge']
    PowerTrain = data['PowerTrain']
    Seats = eval(data['Seats'])
    PlugType = data['PlugType']
    BodyStyle = data['BodyStyle']
    Segment = data['Segment']

    price_vs = Vehicle_Price(AccelSec,TopSpeed_KmH,Range_Km,Efficiency_WhKm,FastCharge_KmH,RapidCharge,PowerTrain,
                 Seats,PlugType,BodyStyle,Segment)
    charges = price_vs.get_predicted_charges()
        
    return jsonify({"Result": f"Predicted vehicle cost are : {charges}"})

    


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = config.PORT_NUMBER,debug=False)
