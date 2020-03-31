import numpy as np
import requests

class LinearRegression:
    """Runs Linear regeression using gradient steep decent method
     and calculates the error using sum of sqr error"""

    def __init__(self, url):
        self.url = url

    def collect_datset(self):
        """ Collect dataset of CSGO
    The dataset contains ADR vs Rating of a player.
    :return : dataset obtained from the link, as matrix
    """
        response = requests.get(self.url)
        lines = response.text.splitlines()
        data = []
        for item in lines:
            item = item.split(",")
            data.append(item)
        data.pop(0) # to remove labels from list
        dataset = np.matrix(data)
        return dataset

    def run_steep_gradient_decent(self, data_x, data_y, len_data, alpha, theta):
        """
            Aplha : Learning rate
            Theta : Feature vector(weight's for our model)
            Theta = y - m * x
            Gradient Decent = Theta - (alpha/n)* d/dQ(Q0, Q1)
        """
        n = len_data
        prod = np.dot(theta, data_x.transpose())
        prod -= data_y.transpose()
        sum_grad = np.dot(prod, data_x)
        theta = theta - (alpha / n) * sum_grad
        return theta
    
    def sum_of_square_error(self, data_x, data_y, len_data, theta):
        ''' Error = sum of (Q.X - y)^2
            Error = Error / (2n) for standardization.     
        '''
        
        n =len_data
        prod = np.dot(theta, data_x.transpose())
        prod -= data_y.transpose()
        sum_elem = np.sum(np.square(prod))
        error = sum_elem / (2 * n)
        return error

    def run_linear_regression(self, data_x, data_y):
        '''Runs Linear regression model,
        calculates theta and error for 
        best fit line.'''
        
        # define number of iterations
        iterations = 100000
        # define learning rate
        alpha = 0.0001550

        no_features = data_x.shape[1]
        len_data = data_x.shape[0] - 1
        # initialize zeros matrix of size no of space features
        theta = np.zeros((1, no_features))

        for i in range(0, iterations):
            theta = self.run_steep_gradient_decent(data_x, data_y, len_data, alpha, theta)
            error = self.sum_of_square_error(data_x, data_y, len_data, theta)
            print("Interation no. %d - Error is %6.f" %(i + 1, error))
        
        return theta


if __name__ == "__main__":
    url = (
        "https://raw.githubusercontent.com/yashLadha/"
        + "The_Math_of_Intelligence/master/Week1/ADRvs"
        + "Rating.csv"
    )  # link to csgo player ratings
    
    lr = LinearRegression(url)
    data = lr.collect_datset()
    data_x =np.c_[np.ones(len(data)), data[:, :-1]].astype(float)

    # print(data_x)
    # print(len(data_x))


    data_y =  data[:, -1].astype(float)
    # print(data_y)
    # print(len(data_y))

    data_q= lr.run_linear_regression(data_x, data_y)
    len_q = data_q.shape[1]
    print("Resultant feature vector: ")
    for i in range(0, len_q):
        print(f"{data_q[0, i]}")

