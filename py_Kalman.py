# not finished!!

import numpy as np
import matplotlib.pyplot as plt


'''
This implementation is partly based on "An Introduction to the Kalman Filter" by Greg Welch and Gary Bishop,
and on the python implementation by Andrew D. Straw (especially the plotting part).
We assume the process is governed by the linear difference equations:
x(k) = A*x(k-1) + B*u(k-1) + w(k)
z(k) = C*x(k) + D(k) + v(k) 
'''

# parameters
n_iter = 200   #number of iterations
dim_of_system = 1
A = np.zeros([dim_of_system,dim_of_system])
B = np.zeros([1,dim_of_system])
C = np.zeros([dim_of_system,1])
D = 0


# initiating parameters for this example
A = np.eye(dim_of_system)       #the state doesn't change from state to state
B=np.ones([1,dim_of_system])
u = 0                           #no control input. (hence B doesn't matter)
C = np.ones([dim_of_system,1])  #the measurement is of the state
D = 0

x = -0.37727 # truth value (typo in example at top of p. 13 calls this z)
z = np.random.normal(x,0.1,size=[n_iter,dim_of_system]) # observations (normal about x, sigma=0.1)
Q = (1e-5)*np.ones([dim_of_system]) # process variance
R = (0.1**2)*np.ones([dim_of_system]) # estimate of measurement variance, change to see effect

# allocating array spaces
x_hat = np.zeros([n_iter,dim_of_system])
x_hat_minus = np.zeros([n_iter,dim_of_system])
P = np.zeros([n_iter,dim_of_system])
P_minus = np.zeros([n_iter,dim_of_system])
K = np.zeros([n_iter,dim_of_system])

# intial guesses
x_hat[0] = 0.0
P[0] = 1.0

for k in range(1,n_iter):

    # time update
    x_hat_minus[k] = x_hat[k-1]
    P_minus[k] = P[k-1] + Q

    # measurement update
    K[k] = P_minus[k] * 1/(P_minus[k] + R)
    x_hat[k] = x_hat_minus[k] + K[k]*(z[k]-x_hat_minus[k])
    P[k] = ( np.ones([dim_of_system])  - K[k])*P_minus[k]

plt.figure()
plt.plot(z,'k+',label='noisy measurements')
plt.plot(x_hat,'b-',label='a posteri estimate')
plt.axhline(x,color='g',label='truth value')
plt.legend()
plt.title('Estimate vs. iteration step', fontweight='bold')
plt.xlabel('Iteration')
plt.ylabel('Voltage')

plt.figure()
valid_iter = range(1,n_iter) # Pminus not valid at step 0
plt.plot(valid_iter,P_minus[valid_iter],label='a priori error estimate')
plt.title('Estimated $\it{\mathbf{a \ priori}}$ error vs. iteration step', fontweight='bold')
plt.xlabel('Iteration')
plt.ylabel('$(Voltage)^2$')
plt.setp(plt.gca(),'ylim',[0,.01])
plt.show()
