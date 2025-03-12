from futu import *
import pandas as pd

pd.set_option('display.max_rows', None)  # Show all rows

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_plate_list(Market.HK, Plate.CONCEPT)
# ret, data = quote_ctx.get_plate_list(Market.HK, Plate.INDUSTRY)
if ret == RET_OK:
    print(data)
    print(data['plate_name'][0])    # 取第一条的板块名称
    print(data['plate_name'].values.tolist())   # 转为 list
else:
    print('error:', data)
quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽

# Export to Excel
# data.to_excel('output1.xlsx', index=False)  # Set index=False to avoid writing row indices