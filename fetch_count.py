#-*- coding: utf-8 -*-

import sys
import urllib.request
import xml.etree.ElementTree as etree
import calendar
import datetime

import csv


work_path="work/"

def apiKey():
	f = open('.apikey')
	key = f.read()
	f.close()
	return key.strip()

def fetch(start, end):
	key = apiKey()
	url = "http://redmine.uzabase.lan/redmine/issues.xml?project_id=79&key=42244093aaf2bc2b638592cf75ff79a65b6b6ffa&created_on=%3E%3C" + start + "|" + end + "&limit=1"
	print(url)
	with urllib.request.urlopen(url) as res:
		html = res.read().decode("utf-8")
		f = open(fileName(start, end), 'w')
		f.write(html)
		f.close()

def fileName(start, end):
	return work_path + start + "to" + end

def output(start, end):
	tree = etree.parse(fileName(start, end))
	root = tree.getroot()
	count = root.attrib['total_count']
	print(start + " to " + end + " : " + count)

date=datetime.date(2016, 10, 31)
start_date=datetime.date(2013, 1, 1)

while start_date < date:
	date=date + datetime.timedelta(days=-1)
	end=str(date)
	date=date + datetime.timedelta(days=-6)
	start=str(date)
	fetch(start, end)
	output(start,end)

