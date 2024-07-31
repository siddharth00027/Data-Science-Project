# import json
# import  pickle
# import  numpy as np
# __location=None
# __data_columns=None
# __model=None

# def get_estimated_price(location,sqft,bhk,bath):
#     load_saved_artifacts()
#     try:
#         loc_index = __data_columns.index(location.lower())
#     except:
#         loc_index=-1
#     x = np.zeros(len(__data_columns))
#     x[0] = sqft
#     x[1] = bath
#     x[2] = bhk
#     if loc_index >= 0:
#         x[loc_index] = 1
#     return  round(__model.predict([x])[0],2)


# def load_saved_artifacts():
#     print("loading saved artifacts...start")
#     global __data_columns
#     global __location

#     with open("./artifacts/columns.json",'r') as f: #with open("./artifacts/columns.json",'r') as f:
#         __data_columns=json.load(f)['data_columns']
#         __location=__data_columns[3:]
#     global __model
#     with open("./artifacts/Banglore_home_prices_model.pickle",'rb') as f:
#         __model=pickle.load(f)
#     print("Loading save artifacts is done!")

# def get_location_name():
#     load_saved_artifacts()
#     return __location


# if __name__ == "__main__":
#     load_saved_artifacts()
#     print(get_location_name())
#     print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
#     print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
#     print(get_estimated_price('Kalhalli', 1000, 2, 2))
#     print(get_estimated_price('Ejipura', 1000, 2, 2))
import json
import pickle
import numpy as np

__location = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    # Ensure artifacts are loaded
    if __data_columns is None or __model is None:
        load_saved_artifacts()
    
    # Find location index
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1  # Location not found
    
    # Create feature array
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    
    # Predict price
    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    global __data_columns
    global __location
    global __model
    
    print("Loading saved artifacts...start")
    
    try:
        # Load columns
        with open("./artifacts/columns.json", 'r') as f:
            __data_columns = json.load(f)['data_columns']
            __location = __data_columns[3:]
        
        # Load model
        with open("./artifacts/Banglore_home_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)
        
        print("Loading saved artifacts is done!")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        __data_columns = []
        __location = []
        __model = None
    
    except json.JSONDecodeError:
        print("Error decoding JSON file.")
        __data_columns = []
        __location = []
        __model = None
    
    except pickle.PickleError:
        print("Error loading the model file.")
        __model = None
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        __data_columns = []
        __location = []
        __model = None

def get_location_name():
    if __location is None:
        load_saved_artifacts()
    return __location

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_name())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))
