import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    x=np.array(X)
    y1=np.array(y)
    a1=((x.T)@x)
    a2=((x.T)@y1)
    theta=((np.linalg.inv(a1))@a2)
    np.round(theta)
    return theta