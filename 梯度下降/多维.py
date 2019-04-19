theta=[1,2]
a=len(theta)
data=[
    [1,1],
    [2,2],
    [3,3],

]
time=1500
alpha=0.001
m=len(data)

def fd(theta,data,time,alpha):

    for _ in range(time):
        temp_theta=theta
        temp_i = 0
        for s in data:


            for i in range(a-1):
                temp_i+=temp_theta[i]*s[i]


        for q in data:

            for i in range(a):
                if i==m-i:
                    temp_theta[i] =temp_theta[i]-((temp_i+temp_theta[a-1]-q[a-1])*alpha)/m
                else:
                    temp_theta[i]=temp_theta[i]-(q[i]*(temp_i+temp_theta[a-1]-q[a-1])*alpha)/m

        theta=temp_theta
        print(temp_theta)


if __name__=="__main__":
    fd(theta,data,time,alpha)