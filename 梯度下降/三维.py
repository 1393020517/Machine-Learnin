theta=[5,4,6]#(a,b,c)z=ax+by+c
data=[
    [0,0,1],
    [1,1,3],
    [1,2,4],
    [2,3,6],
]
time=15000000
alpha=0.001
m=len(data)
def fd(theta,data,time,alpha):
    for _ in range(time):
        for i in data:
            temp_theta=theta
            temp_theta[0]=theta[0]-((i[0]*(temp_theta[0]*i[0]+temp_theta[1]*i[1]+temp_theta[2]-i[2]))*alpha/m)#对a偏导
            temp_theta[1] = theta[1] - ((i[1] * (temp_theta[0] * i[0] + temp_theta[1] * i[1] + temp_theta[2] - i[2])) *alpha/ m)  # 对b偏导
            temp_theta[2] = theta[2] - ((temp_theta[0] * i[0] + temp_theta[1] * i[1] + temp_theta[2] - i[2]) *alpha/ m)  # 对c偏导
            theta=temp_theta
            print(theta)
if __name__=="__main__":
    fd(theta,data,time,alpha)