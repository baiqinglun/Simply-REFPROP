R = 8.314
import json

class Gas:
    def __init__(self,name="Gas",P=10100,T=298):
        with open("REFPROP/gas.json", 'r') as file:
            data = json.load(file)
            self.name = data[name]["name"]
            self.M = data[name]["M"]
            self.r = data[name]["r"]
            self.critical_T = data[name]["critical_T"]
            self.critical_P = data[name]["critical_P"]
            self.specific_heat_capacity = data[name]["specific_heat_capacity"]
            self.R = R / self.M # J/(kg K)
            self.CalSoundVelocity()
        self.P = P
        self.T = T
        self.S = 0
        self.H = 0
        self.rho = 0
        self.Cp = 0
        self.Cv = 0

    def print(self):
        self.CalSoundVelocity()
        print("=================================================")
        print("气体",self.name,"的属性如下：")
        print("分子量",self.M*1000)
        print("绝热指数",self.r)
        print("温度",self.T)
        print("压力",self.P)
        print("密度",self.rho)
        print("焓值",self.H)
        print("熵值",self.S)
        print("定压比热容",self.Cp)
        print("定容比热容",self.Cv)
        print("临界温度",self.critical_T)
        print("临界压力",self.critical_P)
        print("比热",self.specific_heat_capacity)
        print("个别气体常数",self.R)
        print("声速",self.sound_velocity)
        print("=================================================")

    def SetDensity(self,rho):
        self.rho = rho
    def SetEnthalpy(self,H):
        self.H = H
    def SetEntropy(self,S):
        self.S = S
    def CalSoundVelocity(self):
        self.sound_velocity = pow(self.r * self.R * 298,0.5)