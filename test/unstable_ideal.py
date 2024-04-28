from REFPROP import Property,REFPROPManager,Substance
from REFPROP.gas import Gas
import math
from tool import logtime

@logtime
def calculate_unstable():
    rEFPROPManager = REFPROPManager()
    # 定义气瓶
    V0 = 0.025
    D = 0.002

    # 定义大气气体
    p_atm = 101325
    t_atm = t0 = 300
    gas_atm = Gas("H2",P=p_atm,T=t_atm)

    # 定义罐内初始条件
    p0 = 890000
    gas0 = Gas("H2",P=p0,T=t0)
    r= gas0.r
    rho0 = rEFPROPManager.PTCalculateProperty(Property.D,p=p0,t=t0)
    m0 = rho0 * V0

    dp = 1
    i = 0

    p3 = 2 * p_atm
    while p0 >= p_atm:
        if p3 >= p_atm:
            # 泄漏口压力
            p1 = pcr = pow(2/(r+1),r/(r-1)) * p0
            # 泄漏口温度
            t1 = t0 * (pow(math.e,(r-1)/r)*p1/p_atm)
            # 泄漏口速度
            v1 = c = pow(2*r/(r+1)*gas0.R*t0,0.5)
        else:
            p1 = p_atm
            t1 = t0 * (pow(math.e,(r-1)/r)*p1/p_atm)
            v1 = pow(2*r/(r-1)*gas0.R*t0*(1-pow(1-p_atm/p0,(r-1)/r)))

        if p1 <= p_atm:
            p3 = p_atm

        rho1 = rEFPROPManager.PTCalculateProperty(Property.D,p=p1,t=t1)
        m = math.pi * pow(D,2)*v1*rho1
        p0 = p0 - i * dp
        i = i + 1
        print(f"步数：{i}  质量为：{m}") if i%50 == 0 else ""

    gas1 = Gas("H2",P=p1,T=t1)
    gas1.print()