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
	url = "http://redmine.uzabase.lan/redmine/issues.xml?limit=1" \
		+ "&project_id=%s" % 79 \
		+ "&key=%s" % apiKey() \
		+ "&created_on=%s" % "%3E%3C" \
		+ "%s" % start + "|%s" % end

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

