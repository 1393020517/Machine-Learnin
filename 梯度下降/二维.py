theta = [1,12] # [b,a] y=b+ax
data=[
    [1,1],
    [2,2],
    [3,3],
    [4,4],
]

m = len(data)
alpha = 0.001
iterm = 150000

def cost(theta,data):
    sum = 0
    for i in data:
        sum += (theta[0]+theta[1]*i[0]-i[1])*(theta[0]+theta[1]*i[0]-i[1])
    print(sum)

def gd(theta,data,alpha,iterm):
    for _ in range(iterm):
        cost(theta,data)
        temp_theta = theta
        for i in data:
            temp_theta[0] = theta[0]- ((theta[0]+theta[1]*i[0]-i[1])*alpha/m)
            temp_theta[1] = theta[1] - ((theta[0]+theta[1]*i[0]-i[1])*i[0]*alpha/m)
            theta = temp_theta
    print(theta)

if __name__ == "__main__":
    gd(theta,data,alpha,iterm)
