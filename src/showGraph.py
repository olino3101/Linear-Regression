import matplotlib.pyplot as plt
from calculs import LinearModel

def ShowGraph(xPoints, yPoints, theta0, theta1, xArr): # x and y are the points
    # xLine = np.linspace(min(xPoints), max(xPoints), 100)
    yLine = LinearModel(theta0, theta1, xPoints)

    # plotting points as a scatter plot
    plt.scatter(xArr, yPoints, label= "stars", color= "green", 
            marker= "*", s=30)
    # plotting line function
    plt.plot(xArr, yLine, color='blue', label=f'y = {theta0:.2f} + {theta1:.2f}x')

    # naming the x axis
    plt.xlabel('Km')
    # naming the y axis
    plt.ylabel('Price')

    # giving a title to my graph
    plt.title('LINEAR REGRESSION')
    plt.show()