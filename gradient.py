import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

def gradient_descent(x,y):

    # Setting initial values of m and b to 0

    m_curr = b_curr = 0

    # Setting the number of iterations

    iterations = 1000
    n = len(x)

    # Defining the learning rate

    learning_rate = 0.08

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr

        # Computing the cost, partial derivative of m and b from standard formulas
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        m_derivative = -(2/n) * sum(x * (y-y_predicted))
        b_derivative = -(2/n) * sum(y-y_predicted)

        # Update the values of m current and b current
        m_curr = m_curr - learning_rate * m_derivative
        b_curr = b_curr - learning_rate * b_derivative
        print("m {} , b {} , cost {} ,iteration {}".format(m_curr,b_curr,cost,i))




gradient_descent(x,y)