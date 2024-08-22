# Curve fit for experiments
    #### Video Demo:  https://youtu.be/iSDY4vM7hKw
    #### Description: Creates a curve fit for experimental data
    The code can read a csv file and create a curve to model this data, it can does two type of adjustments: polynomial from order 1 to 10, and exponential adjustment. And its up to the user what kind of adjustment he wants and whats the order of adjustment.
    The code returns to user the parameters of the fit curve and plots the adjustment and the original data for the user in a chart.
    The data needs to be in a csv file, where the first columm is the x and second columm is F(x), don't need a header, but if it has a header, must be named as 't' and 'F(t)'. Be sure, that the first line is not empty, if its empty must be deleted because it can cause problems. Also, the code will raise a ValueError if the data has some problem, like some line has something that is not an integer or another problem with the data, be sure to check your experimental data.
    If you are using the exponential fit the code will return to you the parameters from lower to higher order [a + b * exp(c*x)], so the parameters will be returned as [a,b,c].
    If you are using the polynomial fit the parameters will be returned at higher order to lower order, so if 2 order [ax^2 + bx + c] the parameter will be returned as [a,b,c].
    The parameters returned are not rounded, so the user must evaluate the results by himself.
    The program don't judge the adjusment, so if you pick a bad adjustment to your data the program will do its best to fit the data, but it can be a bad fit, its up to you to evaluate those things.

    WARNING: attention to format of the data, it will be accepted dot or comma as decimal separator, but try to not use any thousands separator. [2.5 2,5 2500.4] OK [2,500.4 2.500,4] NOK. If it has some problem of this kind, the program will raise a ValueError, so attention to the data you are putting in it. You can use excel's or google sheet's data formating to avoid those errors.

    STEP BY STEP:
    1. Run the code
    2. Put the path of the csv file (you can copy the path by clicking with right botom in the file and selecting copy path)
    3. Choose your adjustment (it can be polynomial or exponential, code wil accept 'poly' or 'exp' too)
    4. Choose the order if needed, but the number digit and not typed so 1, 2, 3.... (if polynomial you need to choose the order betwen 1 to 10)
    5. Run it
    6. Read the results, code will plot a chart with experimental data and the adjustment curve, and the parameters will be printed for you
