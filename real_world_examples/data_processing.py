# 数据处理调试示例
import pandas as pd

def process_data():
    data = pd.DataFrame({'values': [1,2,3,None,5]})
    return data.fillna(0)