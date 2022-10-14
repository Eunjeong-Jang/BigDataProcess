#!/usr/bin/python3

from openpyxl import load_workbook

wb = load_workbook(filename = 'student.xlsx')
ws = wb['Sheet1']

#total 계산
row_num = 1
total = []
for row in ws:
	if row_num != 1:
		sum = ws.cell(row = row_num, column = 3).value * 0.3
		sum += ws.cell(row = row_num, column = 4).value * 0.35
		sum += ws.cell(row = row_num, column = 5).value * 0.34
		sum += ws.cell(row = row_num, column = 6).value
		ws.cell(row = row_num, column = 7).value = sum
		
		total.append(sum)
	row_num += 1

#grade 계산
sorted_total = sorted(total, reverse=True) #점수 내림차순 정렬
max_grade = [] #몇 등까지 해당 학점(A+ ~ C+)을 받을 수 있는지
max_grade.append((int)(len(total) * 0.15))
max_grade.append((int)(len(total) * 0.3))
max_grade.append((int)(len(total) * 0.5))
max_grade.append((int)(len(total) * 0.7))
max_grade.append((int)(len(total) * 0.85))

index = 0
while index < 5:
	if max_grade[index] == 0:
		max_grade[index] = 1000
	else:
		if max_grade[index] < len(total):
			if sorted_total[max_grade[index] - 1] == sorted_total[max_grade[index]]:
				max_grade[index] = 1000 #받을 수 없는 학점에는 1000 입력
			else:
				max_grade[index] = sorted_total[max_grade[index] - 1]
		elif max_grade[index] == len(total):
			max_grade[index] = sorted_total[max_grade[index] - 1]
	index += 1

row_num2 = 1
for row in ws:
	if row_num2 != 1:
		if ws.cell(row = row_num2, column = 7).value >= max_grade[0]:
			ws.cell(row = row_num2, column = 8).value = 'A+'
		elif ws.cell(row = row_num2, column = 7).value >= max_grade[1]:
			ws.cell(row = row_num2, column = 8).value = 'A0'
		elif ws.cell(row = row_num2, column = 7).value >= max_grade[2]:
			ws.cell(row = row_num2, column = 8).value = 'B+'
		elif ws.cell(row = row_num2, column = 7).value >= max_grade[3]:
			ws.cell(row = row_num2, column = 8).value = 'B0'
		elif ws.cell(row = row_num2, column = 7).value >= max_grade[4]:
			ws.cell(row = row_num2, column = 8).value = 'C+'
		else:
			ws.cell(row = row_num2, column = 8).value = 'C0'
	row_num2 += 1

wb.save("student.xlsx")
