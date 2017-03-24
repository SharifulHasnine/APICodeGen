from django.shortcuts import render
from .models import *
import random
import csv
# Create your views here.

def insertRandomData():
	n = 500000
	
	while(n>0):
		n-=1
		randCode = int(random.random()*100000000)
		newRow = SampleCode(code=randCode)
		newRow.save()

	return

def createCode():
	randCode = int(random.random()*100000000)
	newRow = SampleCode(code=randCode)
	newRow.save()
	return
	
def generate_code(quantity,fileName,column_number):
	rows = SampleCode.objects.raw('SELECT * from Sample_code WHERE status=0 LIMIT %d'%(quantity))
	with open(fileName, 'w', newline='') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ')
		for row in rows:
			csvwriter.writerow(["Your","Code","is",str(row.code)])
			row.status=1
			row.save()
	return
