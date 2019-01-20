# !/usr/bin/env Python
# -*- coding:utf-8 -*-
# Parser_Page.py
# 解析单页面的内容，提取想要的内容
# author: SugarChoc

import requests
import os
from bs4 import BeautifulSoup


class Parser_Page():
    # 解析页面
    def __init__(self, req):
        # 传入成功
        self.req = req
        self.goods_info_list = []

    def get_cell(self):
        # 得到货品单元div
        '''
        京东页面产品数量会随着下拉新增到一个页面60个，无下拉时只有30个
        '''
        soup = BeautifulSoup(self.req)
        goods_list = soup.find_all('div', class_="gl-i-wrap")  # 找到货品div
        for self.goods_cell in goods_list:  # 获得 单个 货品div
            self.get_info(self)

    def get_info(self):
        # 从货品单元获得信息:价格,图片,名称,链接
        info_dict = []  # 初始化
        info_dict['price'] = float(
            self.goods_cell.find('strong').find('i').text)  # 价格


# 调试主程序
if __name__ == "__main__":
    # 京东的蓝牙耳机
    url = "https://search.jd.com/Search?keyword=%E8%93%9D%E7%89%99%E8%80%B3%E6%9C%BA&enc=utf-8&suggest=2.def.0.V14&wq=lanya&pvid=c56fe9336e274887a05559d7b82cb21f"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    headers = {"user-agent": user_agent}
    try:
        req = requests.get(url=url, headers=headers)
        if req.status_code == 200:
            PP = Parser_Page(req)            
    except Exception as error:
        print(error)
    else:
        pass
    finally:
        pass

