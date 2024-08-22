import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import sys
from scipy.optimize import curve_fit

def main():
    F_t,t= csv_reader(input("What's archive path? "))

    # Asks for adjustment type
    fit_type= input("What's the type of the fit: ")
    if fit_type not in ['Polynomial', 'poly', 'Poly', 'Exponential','exp','exponential']:
        sys.exit('Invalid adjustment type')

    # If linear fit, asks order and aplies the adjustment
    elif fit_type in ['Polynomial', 'poly', 'Poly']:
        order= input("What's the order of adjustment? ")
        if int(order) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            sys.exit('Invalid order, order needs do be between 1 and 10')
        else:
            F_t_fit,cte= fit_lin(t,F_t,order)
            plot(t,F_t,F_t_fit)
            print("Constants for adjust are: ",end='')
            print(cte)

    elif fit_type in ['exp', 'Exponential', 'exponential']:
        cte= fit_exp(t,F_t)
        print("Constants for adjust are (a + b exp(c*x)): ",end='')
        print(cte)
        plot(t,F_t,exponential(np.array(t), *cte))


def csv_reader(p):
    path =  p
    #Reading CSV file
    try:
        df= pd.read_csv(path)
        F_t= df['F(t)']
        F_t= [float(str(n).replace(',','.')) for n in F_t]
        t= df['t']
        t= [float(str(n).replace(',','.')) for n in t]
        return F_t, t

    #In case the file has no header
    except KeyError:
        df= pd.read_csv(path, header=None, names=['t','F(t)'])
        F_t= df['F(t)']
        F_t= [float(str(n).replace(',','.')) for n in F_t]
        t= df['t']
        t= [float(str(n).replace(',','.')) for n in t]
        return F_t, t


def plot(t,fx,fy):
    df = pd.DataFrame({'t': t, 'fx': fx, 'fy': fy})
    fig = px.scatter(df, x='t', y='fx', title='Dados Originais e Ajuste Linear')
    fig.add_trace(go.Scatter(x=t, y=fy, mode='lines', name='Ajuste linear'))
    fig.update_layout(xaxis_title='t', yaxis_title='f(t)')
    fig.show()


#Function to do linear fit
def fit_lin(t,f_t,n):
    x= np.array(t)
    f= np.array(f_t)

    cte = np.polyfit(x,f,int(n))
    f_fit = np.poly1d(cte)
    f_fit= f_fit(t)
    return f_fit,cte

#Generates an exponential function and uses curve_fit to find the parameters
def exponential(x,a,b,c):
    return a + b * np.exp(c * x)

def fit_exp(t,f):
    cte,cte_cov= curve_fit(exponential, t, f, p0=[0,1,1])
    return cte

if __name__ == "__main__":
    main()
