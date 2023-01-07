from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from nsetools import Nse
from matplotlib.backends.backend_agg import FigureCanvasAgg
nse = Nse()
import requests

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def members(request):
    return render(request, 'members.html')

def contactus(request):
    return render(request, 'contact.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def codes(request):
    return render(request, 'codes.html')

def codesfunction(request):
    codes = nse.get_stock_codes()
    return JsonResponse(codes, safe=False)

def searchpage(request, code):
    s = nse.get_quote(code)
    return JsonResponse(s, safe=False)

def search(request):
    return render(request, 'search.html')

def gainers(request):
    return render(request, 'gainers.html')

def gainersfunction1(request):
    gainers = nse.get_top_gainers()
    s = gainers[0]
    return JsonResponse(s, safe=False)

def gainersfunction2(request):
    gainers = nse.get_top_gainers()
    s = gainers[1]
    return JsonResponse(s, safe=False)

def gainersfunction3(request):
    gainers = nse.get_top_gainers()
    s = gainers[2]
    return JsonResponse(s, safe=False)

def losers(request):
    return render(request, 'losers.html')

def losersfunction1(request):
    losers = nse.get_top_losers()
    s = losers[0]
    return JsonResponse(s, safe=False)

def losersfunction2(request):
    losers = nse.get_top_losers()
    s = losers[1]
    return JsonResponse(s, safe=False)

def losersfunction3(request):
    losers = nse.get_top_losers()
    s = losers[2]
    return JsonResponse(s, safe=False)

def predictions(request):
    if request.method == 'POST':
        try:
            code = request.POST.get('code').upper()
            #importing all the libraries for the program
            from alpha_vantage.timeseries import TimeSeries
            from alpha_vantage.techindicators import TechIndicators
            import matplotlib.pyplot as plt
            import numpy as np
            from sklearn.linear_model import LinearRegression
            from sklearn.model_selection import train_test_split
            from sklearn import metrics
            from sklearn.preprocessing import PolynomialFeatures
    
            #using the aplha vantage api to get the stockmarket data of a company
            key = "VIYRYDIX8IIRZP99"
            ts = TimeSeries(key, output_format='pandas')
            ti = TechIndicators(key)
            aapl_data, aapl_meta_data = ts.get_daily_adjusted(symbol=code) # you can change the company code to get the data of another company
            aapl_sma, aapl_met_sma = ti.get_sma(symbol=code)
            print('Data Collected Successfully from the Alpha Vantage API...')
    
            #reshaping and adjusting data into arrays to feed into the machine learning model
            price = aapl_data.iloc[:, 0]
            y = np.array(price).reshape((-1,1))
            numbers = list(range(1,101))
            x = np.array(numbers).reshape((-1,1))
            x_predict = np.array([101]).reshape((-1,1))
            latest_price = price.iloc[99]
    
            #splitting the data into training and testing data
            X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
            SEED = 42
            X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = SEED)
            
            # creating polynomial function for polynomial regression
            poly = PolynomialFeatures(degree=10, include_bias=False)
            poly_feature = poly.fit_transform(X_train)
            poly_feature1 = poly.fit_transform(x)
            poly_predict = poly.fit_transform(x_predict)
            
            # creating and training the linear regression model
            regressor = LinearRegression()
            regressor.fit(poly_feature, y_train)
            print('Model Created Successfully...')
            print('The Intercept is:', regressor.intercept_)
    
            # making predictions using the model
            predictions = regressor.predict(poly_predict)
            new_prediction_for_y = float(predictions)
            print(new_prediction_for_y)
            print('The Predicted Value is:',predictions)
            ynew1 = np.append(x, [101])
            ynew = np.array(ynew1).reshape((-1,1))
            predicted = np.append(y, [predictions])
    
            # creating array to store all the predicted values
            predicted_y = regressor.predict(poly_feature1)
            y_pred_1 = predicted_y
    
            #plotting the graph to show the values
            plt.plot(x, y_pred_1)
            plt.plot(ynew, predicted)
            plt.plot(x, y)
            plt.xlabel('Number')
            plt.ylabel('Stock Price')
            plt.legend(['Previously Predicted Values', 'Next Prediction', 'True Values'])
            plt.grid()
            plt.show()
            
            
        except:
            return HttpResponse("The given API does not have data for the following Company.")
            
            #check wheter the price will increase or decrease
            
        difference = predictions - latest_price
        if difference > 0 :
            return render(request, 'up.html', {"prediction": new_prediction_for_y})
            
        else: 
            return render(request, 'down.html', {"prediction": new_prediction_for_y})
        
    
    else:
        return render(request, 'predict.html')