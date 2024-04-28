from REFPROP import Property,REFPROPManager,Substance
from REFPROP.gas import Gas
import math
from tool import logtime

@logtime
def calculate_unstable1():
    rEFPROPManager = REFPROPManager()
    rEFPROPManager.SetSubstance(substance=Substance.HYDROGEN)

    # 初始化参数
    P = 101325
    T = 300
    H1 = 0.5 # 高度

    # 初始化泄漏量
    Cd = 1
    A = math.pi/4.0 * pow(0.01,2)
    M = 2
    r = 1.4
    R = 8.314
    P1 = 4000000
    T1 = 300
    Q1 = Cd * A * P1 * pow(M*r*pow(2/(r+1),(r+1)/(r-1))/R/T1,0.5)
    H1 =rEFPROPManager.PTCalculateProperty(Property.H,p=P1,t=T1)
    D1 =rEFPROPManager.PTCalculateProperty(Property.D,p=P1,t=T1)
    S1 =rEFPROPManager.PTCalculateProperty(Property.S,p=P1,t=T1)
    # 初始化vcr
    vcr = pow(2/(r+1),r/(r-1))

    print(H1)
    # print(D1)
    # print(S1)
    ua = 1300
    do = True
    Qnew = 1
    dvcr = 0.00001
    i = 0
    Q0 = 0.003889 # kg/s
    while do or (Qnew - Q1)/Qnew <= 0.001:
        do = False
        u2 = 0
        while abs(u2-ua) >= 0.1:
            P2 = vcr * P1
            H2 = rEFPROPManager.PSCalculateProperty(Property.H,p=P2,s=S1)
            u2 = pow(2*(H1-H2),0.5)
            vcr = vcr - dvcr
            i = i + 1
            print(f"压力为{P2}，速度为{u2}") if i%50 == 0 else ""
            pass
        rho2 = rEFPROPManager.PSCalculateProperty(Property.D,p=P2,s=S1)
        u0 = Q0 / (A*rho2)
        print(f"速度为{u0}")
        # Cv = Q0 / (rho2 * (P2-P0))
        pass
    pass