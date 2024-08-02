from model import Final
import numpy as np
def test_valid_input():
    input_data = [
        0.5,
       1.2,
         3.4,
        2.1,
        0.8,
         2  # integer feature
    ]
    
    prediction = Final().predict([input_data])
    assert isinstance(prediction[0],np.int64)