Stock Market Prices 

Description:
    This website can be used to get prices and make price predictions about the Indian Stock Market Companies. It uses a framework called Django, which is based on Python programming language.<br>
            And for predicting the stock market prices it uses Simple linear Regression on the alpha_vantage API data to develop a Machine Learning Model using Scikit Learn Library and then by using that Model it predicts the next price and shows that price through a graph using Matplotlib library in Python. <br>
            This website uses a Python library in order to get all these information in the backend.<br>
        This Python library, when called gathers data from the Official NSE India website and then converts those data into Json file and sends that Json file back as response to the website. Then the website fecthes that Json file and converts it into usefull Information.<br>
    The biggest challange of this program was that there are no free API's for this kind of stuff which are free and provides data in real time. That's why i had to use this library in order to get that data.<br>

How to Run this project:<br>
    There are just four button on the header of the homepage. In order to search for the symbols of Differnt Companies, you can click on the Symbols button to get all the symbols of differnt companies.<br>
    And in order to search for a particular company, you can go to the search button. Where you can just enter the symbol of the company you want to search, then youwill ber provided with all the information available about that company. You will also be provided with a search property function to search for a particular field of information about that company.<br>

Credits:
    The python Library used on this website to get data from the NSE website is NSETOOLS. You can check their website if you want to check out about them, the link is "https://nsetools.readthedocs.io/en/latest/index.html". 
    
 Libraries Required:<br>
 Matplotlib<br>
 Numpy<br>
 Scikit Leanr<br>


