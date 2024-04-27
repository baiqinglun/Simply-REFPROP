from REFPROP import Property,REFPROPManager,Substance
from REFPROP.gas import Gas

def calculate_unstable():
    # 定义基本物性
    substance:Substance = Substance.HYDROGEN
    p0:float = 101254
    t0:float = 298
    h2_0 = Gas("H2",P=p0,T=t0)
    c = h2_0.sound_velocity
    dp = 1
    i = 0
    v1 = 0
    
    rEFPROPManager = REFPROPManager()
    rEFPROPManager.SetSubstance(Substance.HYDROGEN)
    D0 = rEFPROPManager.PTCalculateProperty(Property.D)
    H0 = rEFPROPManager.PTCalculateProperty(Property.H)
    S0 = rEFPROPManager.PTCalculateProperty(Property.S)
    h2_0.SetDensity(D0)
    h2_0.SetEnthalpy(H0)
    h2_0.SetEntropy(S0)

    while v1<=c:
        p = p0 - i * dp
        T1 = rEFPROPManager.PSCalculateProperty(Property.T,p=p,s=S0)
        H1 = rEFPROPManager.PSCalculateProperty(Property.H,p=p,s=S0)
        D = rEFPROPManager.PSCalculateProperty(Property.D,p=p,s=S0)
        v1 = pow(2*(H0-H1),0.5)
        i = i + 1
    
    h2_1 = Gas("H2",p,T1)
    h2_1.SetDensity(D)
    h2_1.SetEntropy(S0)
    h2_1.SetEnthalpy(H1)
    h2_1.print()
