import pickle
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
import cv2


filename1 = "./static/finalized_model.sav"
filename2 = "./static/finalized_model2.sav"
def dyslexia(pred_list):
    loaded_model = pickle.load(open(filename1, 'rb'))
    #result = loaded_model.score(X_test, y_test)
    result = loaded_model.predict(pred_list)
    #print(result)
    return result

def dyscalculia(pred_list):
    loaded_model = pickle.load(open(filename1, 'rb'))
    #result = loaded_model.score(X_test, y_test)
    result = loaded_model.predict(pred_list)
    #print(result)
    return result
