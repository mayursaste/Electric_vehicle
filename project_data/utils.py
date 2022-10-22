import pickle
import json
import config 
import numpy as np

class Vehicle_Price():
    def __init__(self,AccelSec,TopSpeed_KmH,Range_Km,Efficiency_WhKm,FastCharge_KmH,
                 RapidCharge,PowerTrain,Seats,PlugType,BodyStyle,Segment):
        self.AccelSec          = AccelSec
        self.TopSpeed_KmH      = TopSpeed_KmH
        self.Range_Km          = Range_Km
        self.Efficiency_WhKm   = Efficiency_WhKm
        self.FastCharge_KmH    = FastCharge_KmH
        self.RapidCharge       = RapidCharge
        self.PowerTrain        = PowerTrain
        self.Seats             = Seats
        self.PlugType          = 'PlugType_'+ PlugType
        self.BodyStyle         = 'BodyStyle_'+ BodyStyle
        self.Segment           = 'Segment_'+ Segment
               

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_charges(self):
        self.load_model()
        
        
        PlugType_index  = self.json_data['columns'].index(self.PlugType) 
        BodyStyle_index = self.json_data['columns'].index(self.BodyStyle)
        Segment_index   = self.json_data['columns'].index(self.Segment)

        test_array = np.zeros(len(self.json_data['columns']))
        
        print("Test Array :",test_array) 

        test_array[0] = self.AccelSec
        test_array[1] = self.TopSpeed_KmH                                                         
        test_array[2] = self.Range_Km
        test_array[3] = self.Efficiency_WhKm
        test_array[4] = self.FastCharge_KmH
        test_array[5] = self.json_data['RapidCharge'][self.RapidCharge]
        test_array[6] = self.json_data['PowerTrain'][self.PowerTrain]
        test_array[7] = self.Seats
        test_array[PlugType_index] = 1
        test_array[BodyStyle_index] = 1
        test_array[Segment_index] = 1
        

        print("Test Array :",test_array) 

        predicted_charges = np.around(self.model.predict([test_array])[0],2)
        return predicted_charges

# if __name__ == "__main__":
#       AccelSec=4.6
#       TopSpeed_KmH=233.0
#       Range_Km=450.0
#       Efficiency_WhKm=161.0
#       FastCharge_KmH=940.0
#       RapidCharge=1.0
#       PowerTrain=0.0
#       Seats=5.0
#       PlugType='Type 2 CCS'
#       BodyStyle='Sedan'
#       Segment='D'

    #   price_vs = Vehicle_Price(AccelSec,TopSpeed_KmH,Range_Km,Efficiency_WhKm,FastCharge_KmH,RapidCharge,PowerTrain,
    #              Seats,PlugType,BodyStyle,Segment)
    #   price_vs.get_predicted_charges()