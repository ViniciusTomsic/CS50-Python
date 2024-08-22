import project
import numpy as np

def test_fit_poly():
    t= [0,1,2,3]
    f_t= [0,1,2,3]
    n=1
    f_fit,cte= project.fit_lin(t,f_t,n)
    assert isinstance(f_fit, np.ndarray)
    assert isinstance(cte, np.ndarray)

def test_exponential():
    f_fit= project.exponential(np.array([0,1,2,3]),1,1,1)
    assert isinstance(f_fit, np.ndarray)

def test_fit_exp():
    t= np.array([0,1,2,3])
    f= np.array([1,3,9,23])
    cte= project.fit_exp(t,f)
    assert isinstance(cte, np.ndarray)
    
