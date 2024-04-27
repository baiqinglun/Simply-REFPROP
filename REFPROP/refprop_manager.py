import os, numpy as np
from ctREFPROP.ctREFPROP import REFPROPFunctionLibrary
from REFPROP.substance import Substance
from REFPROP.property import Property
from REFPROP.base_si import BASE_SI

class REFPROPManager(object):
    def __init__(self):
        # 初始化REFPROP
        os.environ['RPPREFIX'] = r'REFPROP'
        self.RP = REFPROPFunctionLibrary(os.environ['RPPREFIX'])
        self.RP.SETPATHdll(os.environ['RPPREFIX'])
        self.SetBaseSI(BASE_SI.MASS_SI)

        self.substance = str(Substance.HYDROGEN)

    # 设置基本单位制
    def SetBaseSI(self,base_type:BASE_SI):
        # 将单位设置为国际单位制
        self.BASE_SI = self.RP.GETENUMdll(0, str(base_type)).iEnum

    def SetSubstance(self,substance:Substance):
        self.substance = str(substance)
    
    # 调用REFPROPdll计算性质
    def PTCalculateProperty(self,calculate_type:Property,p=101325,t=298.15)->float:
        result = self.RP.REFPROPdll(self.substance, "PT",str(calculate_type),  self.BASE_SI, 0, 0, p, t, [1.0])
        if result.ierr == 0:
            return result.Output[0]
        else:
            print(f"错误: {result.herr}")

    def PSCalculateProperty(self,calculate_type:Property,p=101325,s=0)->float:
        result = self.RP.REFPROPdll(self.substance, "PS",str(calculate_type),  self.BASE_SI, 0, 0, p, s, [1.0])
        if result.ierr == 0:
            return result.Output[0]
        else:
            print(f"错误: {result.herr}")