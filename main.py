import csv
import os
from datetime import datetime

us_states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
    }
    

def reader(path = "D:\\GT Data Science and Analytics\\Home_work\\03-Python\\ExtraContent\\Instructions\\PyBoss", file = "employee_data.csv"):

	employee_data = os.path.join(path, file)
	id_lst = []
	full_name_lst = []
	dob_lst = []
	ssn_lst = []
	state_lst = []
	try:
		with open(employee_data, newline = '') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter = ',')
			header = next(csv_reader)
			for line in csv_reader:
				id_lst.append(int(line[0]))
				full_name_lst.append(str(line[1]).split(' '))
				dob_lst.append(datetime.strptime(line[2] , '%Y-%m-%d'))
				ssn_lst.append(str(line[3]).split('-'))
				state_lst.append(str(line[4]))
				
	except FileNotFoundError:
		csv_reader = None

	return id_lst, full_name_lst, dob_lst, ssn_lst, state_lst


def writer(_id, _name, _surname, _dob, _ssn, _state):
	
	with open('results.csv', 'w') as new_csv_file:
		field_names = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
		csv_writer = csv.DictWriter(new_csv_file, fieldnames = field_names, delimiter = ',')
		csv_writer.writeheader()
		for i in range(len(_id)):
			csv_writer.writerow({'Emp ID': _id[i], 'First Name': _name[i], 'Last Name': _surname[i], 'DOB': _dob[i], 'SSN': _ssn[i], 'State': _state[i]})



def converter(full_names, dobs, ssns, states):
	name, surname, new_dobs, ssn_5, states_2 = [], [], [], [], []
	for i in range(len(full_names)):
		#This will add names and surnames to corresponding lists without altering the order.
		name.append(full_names[i][0])
		surname.append(full_names[i][1])

		#This code will convert the datetime format date to a string of a required format of "day/month/year"
		new_dobs.append(dobs[i].strftime('%m/%d/%Y'))

		#This will add the ssn numbers starting from the 6th number. 
		ssn_5.append(ssns[i][2])

		#This code will get the corresponding 2 letter state code for a full state name from the us_states dictinoary and return "Not found" if state is missing in dictionary or not written correctly.
		states_2.append(us_states.get(states[i], 'Not found')) 


	return name, surname, new_dobs, ssn_5, states_2


def logic():

	ident, fname, dob, ssn, state = reader() 
	name, surname, new_dob, new_ssn, state_abrv  = converter(fname, dob, ssn, state)
	writer(ident, name, surname, new_dob, new_ssn, state_abrv)

    
logic()