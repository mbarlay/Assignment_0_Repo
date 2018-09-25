A = 1.2 #0.8m-high and 1.5m-wide window
h_1 = 10 #W/m2
h_2 = 40 #W/m2
k_a = 0.026 #W/mC
k_g = 0.78 #W/mC
L_g = 0.004 #m
L_a = 0.01 #m
T_i =20
T_o = -10

R_1 = 1/(h_1*A)
R_2 = 1/(h_2*A)
R_g_1 = L_g/(k_g*A)
R_g_2 = R_g_1
R_a = L_a/(k_a*A)
R_tot=R_1+R_2+R_g_1+R_g_2+R_a
Q = (T_i-T_o)/R_tot
T_1 = T_i-(Q*R_1)

print("The total resistance is "+str(R_tot))
print("The steady rate of heat transfer through the window is "+str(Q))
print("The temperature of the inner surface is "+str(T_1))

