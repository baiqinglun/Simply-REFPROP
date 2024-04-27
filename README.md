基于ctREFPROP简单地调用REFPROP10

# 安装

```bash
pip install ctREFPROP
```

测试
```python
from REFPROP import Property,REFPROPManager,Substance

if __name__=='__main__':
    rEFPROPManager = REFPROPManager()
    rEFPROPManager.SetSubstance(Substance.HYDROGEN)
    D = rEFPROPManager.PTCalculateProperty(Property.D)
    H = rEFPROPManager.PTCalculateProperty(Property.H)
    S = rEFPROPManager.PTCalculateProperty(Property.S)
    print(f"密度={D}\n焓值={H}\n熵值={S}")
>> 
密度=0.08234824289694123
焓值=3931802.0434372686
熵值=53375.90259029434
```