import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 100
    n = len(x)
    learning_rate = 0.08

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        m_derivative = -(2/n) * sum(x * (y-y_predicted))
        b_derivative = -(2/n) * sum(y-y_predicted)

        m_curr = m_curr - learning_rate * m_derivative
        b_curr = b_curr - learning_rate * b_derivative
        print("m {} , b {} , cost {} ,iteration {}".format(m_curr,b_curr,cost,i))




gradient_descent(x,y)