from REFPROP import Property,REFPROPManager,Substance
from REFPROP.gas import Gas
import math
from tool import logtime

"""
文献名称：Release models for leaks from high-pressure hydrogen storage systems
"""

@logtime
def leakcalc():
    rEFPROPManager = REFPROPManager()
    rEFPROPManager.SetSubstance(Substance.HYDROGEN)

    # 计算罐内气体性质
    P0 = 42500000 # 管内初始压力
    T0 = 300 # 管内初始温度
    V0 = 0.0273 # 容器容积
    S0 = rEFPROPManager.PTCalculateProperty(Property.S,p=P0,t=T0)
    Rho0 = rEFPROPManager.PTCalculateProperty(Property.D,p=P0,t=T0)
    v0 = 1/Rho0
    r = 1.4
    R = 8.314
    M = 0.002
    Rg = R/M
    CONT = pow(v0,r)*P0 # 等熵流动定值
    m0 = Rho0 * V0

    # 计算出口处气体性质
    P2 = pow(2/(r+1),r/(r-1)) * P0 # 出口压力
    U2 = pow(2*r/(r+1)*Rg*T0,0.5) # 出口速度
    v2 = pow(CONT/P2,1/r) 
    Rho2 = 1/v2 # 出口密度
    
    # 质量流量
    A = 0.0000317
    qm = Rho2 * A * U2
    print(f"质量流量={qm}")

    # 迭代计算
    dt = 0.05

    m0 = m0 - qm * dt
    