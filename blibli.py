from lxml import etree
import requests
import time
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '全站榜'
sheet.append(['排行', '标题', 'Up主', '播放量', '弹幕量'])
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3706.400 SLBrowser/10.0.3974.400',
}
url = 'https://www.bilibili.com/ranking/all/0/0/3'

res = requests.get(url,headers=headers)
html = etree.HTML(res.text)
datas = html.xpath('//div[@class="rank-body"]/div[3]/ul/li')
i = 1
for data in datas:
    # time.sleep(1)
    number = data.xpath('./div[1]/text()')[0]
    title = data.xpath('./div[2]/div[2]/a/text()')[0]
    up = data.xpath('./div[2]/div[2]/div/a/span/text()')[0]
    click_number = data.xpath('./div[2]/div[2]/div/span[1]/text()')[0]
    talk_number = data.xpath('./div[2]/div[2]/div/span[2]/text()')[0]
    sheet.append([number,title,up,click_number,talk_number])
    time.sleep(1)
    print('已完成第%d份'%i)
    i = i+1
wb.save('blibli.xlsx')