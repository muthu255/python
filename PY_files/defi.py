import pandas as pd
import numpy as np

data=[[1,2,3,4],[1,2,5]]
src1=pd.DataFrame(data)


src2=pd.isnull(data)
print(src1)
print(src2)


