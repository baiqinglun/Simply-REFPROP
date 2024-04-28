from REFPROP import Property,REFPROPManager,Substance
from REFPROP.gas import Gas
import math
from tool import logtime

@logtime
def calculate_unstable_actral():
    substance = Substance.HYDROGEN
    rEFPROPManager = REFPROPManager()
    rEFPROPManager.SetSubstance(substance)
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
    CV0 = rEFPROPManager.PTCalculateProperty(Property.CV,p=p0,t=t0)
    CP0 = rEFPROPManager.PTCalculateProperty(Property.CP,p=p0,t=t0)
    S0 = rEFPROPManager.PTCalculateProperty(Property.S,p=p0,t=t0)
    # 气体流速
    b = 0.007631
    v1 = pow(2*(r*gas0.R*gas0.R*t0)/(r-1)*(1-pow(p_atm/p0,(r-1)/r)))

    