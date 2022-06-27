impor pandas as pd
import requests
from lxml import etree
import json
import openpyxl

url="https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4"

response = requests.get(url,headers=headers).text

print(response.text)
datas = json.loads(response)

html=etree.HTML(response.text)
result=html.xpath('//*[@id="captain-config"]/text()')
result=json.loads(result[0])
result_in=result["component"][0]["caseList"]
print(result_in)
wb=Workbook()
ws=wb.active
ws.title="疫情"
ws.append(['疫情地区','新增','现有','累计','治愈','死亡'])
for each in result_in:
    temp_list=[each['area'],each['add'],each['now'],each['sum'],each['heal'],each['dead'],]
    ws.append(temp_list)
wb.save("疫情.xlsx")
titanic=pd.DataFrame(pd.read_excel('疫情.xlsx'))
titanic.head()
titanic.to_csv('china_data.csv',encoding='utf-8')