Shown below are the plots for our step response test. A setpoint of 6900 degrees was used to test the step response. 
The green plot shows the excessive oscillation test (Kp = 10), the orange plot shows the best performance achieved (Kp = 0.1), and the blue plot shows the underdamped/slow performance test (Kp = 0.023). The orange plot closely matches the setpoint set for this test (6900), making it near perfect. 

![lab03](https://github.com/dijonm53/Lab3/assets/79309467/38d56efc-dc13-4612-b272-9c85645ca6fb)

Our closed-loop controller takes in a Kp (gain) value and updates the motor position every 10 ms until the motor reaches the position associated with the setpoint. The controller asks the user for a gain every time a test is run and completed.  
