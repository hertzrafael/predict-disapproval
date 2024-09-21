from sklearn.linear_model import LinearRegression

class Model:

    def __init__(self):
        self.model = LinearRegression()
        self.__load__()

    def predict(self, mean):
        return self.model.predict([[mean]])[0][0]

    def __load__(self):
        pass