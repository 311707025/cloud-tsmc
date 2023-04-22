import time,os
import datetime 
import pandas as pd
import numpy as np


class Search():

	def __init__(self, number):
		self.number = number


	def scrape(self):
		pass


class Company(Search):
	
	def company_data(self):
		df = pd.read_excel(r'/home/victor/cloud_tsmc/all_data.xlsx')

		num_list = df['文件編號']
		name_list = df['文件名稱']
		classifier_list = df['文件分類']
		source_list = df['發布來源']
		ddate_list = df['發布日期']
		update_list = df['上次更新時間']

		result_list = []

		for i in range(len(df)):
			result_list.append(dict(num=num_list[i], name=name_list[i], classifier=classifier_list[i], source=source_list[i], ddate=ddate_list[i], update=update_list[i]))
			
		return result_list