"""
    CS110 Lab
    Dictionary Lab

    Updated By: Roger Blake

    CSCI 110
    Date: 

    Working with Python dictionary (dict) data structure.
"""
import os

# create a mapping of state names to their codes using a dictionary
states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisianna': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massassuchetts': 'MA',
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
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'

 # FIXED – add codes for the rest of the states
}

# create a mapping of states to their capital state using a dictionary
capitalCity = {
    'AL': 'Montgomery',
    'AK': 'Juneau',
    'AZ': 'Phoenix',
    'AR': 'Little Rock',
    'CA': 'Sacramento',
    'CO': 'Denver',
    'CT': 'Hartford',
    'DE': 'Dover',
    'FL': 'Tallahassee',
    'GA': 'Atlanta',
    'HI': 'Honolulu',
    'ID': 'Boise',
    'IL': 'Springfield',
    'IN': 'Indianapolis',
    'IA': 'Des Moines',
    'KS': 'Topeka',
    'KY': 'Frankfort',
    'LA': 'Baton Rouge',
    'ME': 'Augusta',
    'MD': 'Annapolis',
    'MA': 'Boston',
    'MI': 'Lansing',
    'MN': 'Saint Paul',
    'MS': 'Jackson',
    'MO': 'Jefferson City',
    'MT': 'Helena',
    'NE': 'Lincoln',
    'NV': 'Carson City',
    'NH': 'Concord',
    'NJ': 'Trenton',
    'NM': 'Santa Fe',
    'NY': 'Albany',
    'NC': 'Raleigh',
    'ND': 'Bismarck',
    'OH': 'Columbus',
    'OK': 'Oklahoma City',
    'OR': 'Salem',
    'PA': 'Harrisburg',
    'RI': 'Providence',
    'SC': 'Columbia',
    'SD': 'Pierre',
    'TN': 'Nashville',
    'TX': 'Austin',
    'UT': 'Salt Lake City',
    'VT': 'Montpelier',
    'VA': 'Richmond',
    'WA': 'Olympia',
    'WV': 'Charleston',
    'WI': 'Madison',
    'WY': 'Cheyenne'
# FIXED – add capital cities for the rest of the states
    
}

# add some more entires to capitalCity dictionary
capitalCity['AL'] = 'Montgomery'
capitalCity['AK'] = 'Juneau'
capitalCity['AZ'] = 'Phoenix'
capitalCity['AR'] = 'Little Rock'
capitalCity['CA'] = 'Sacramento'
capitalCity['CO'] = 'Denver'
capitalCity['CT'] = 'Hartford'
capitalCity['DE'] = 'Dover'
capitalCity['FL'] = 'Tallahassee'
capitalCity['GA'] = 'Atlanta'
capitalCity['HI'] = 'Honolulu'
capitalCity['ID'] = 'Boise'
capitalCity['IL'] = 'Springfield'
capitalCity['IN'] = 'Indianapolis'
capitalCity['IA'] = 'Des Moines'
capitalCity['KS'] = 'Topeka'
capitalCity['KY'] = 'Frankfort'
capitalCity['LA'] = 'Baton Rouge'
capitalCity['ME'] = 'Augusta'
capitalCity['MD'] = 'Annapolis'
capitalCity['MA'] = 'Boston'
capitalCity['MI'] = 'Lansing'
capitalCity['MN'] = 'Saint Paul'
capitalCity['MS'] = 'Jackson'
capitalCity['MO'] = 'Jefferson City'
capitalCity['MT'] = 'Helena'
capitalCity['NE'] = 'Lincoln'
capitalCity['NV'] = 'Carson City'
capitalCity['NH'] = 'Concord'
capitalCity['NJ'] = 'Trenton'
capitalCity['NM'] = 'Santa Fe'
capitalCity['NY'] = 'Albany'
capitalCity['NC'] = 'Raleigh'
capitalCity['ND'] = 'Bismarck'
capitalCity['OH'] = 'Columbus'
capitalCity['OK'] = 'Oklahoma City'
capitalCity['OR'] = 'Salem'
capitalCity['PA'] = 'Harrisburg'
capitalCity['RI'] = 'Providence'
capitalCity['SC'] = 'Columbia'
capitalCity['SD'] = 'Pierre'
capitalCity['TN'] = 'Nashville'
capitalCity['TX'] = 'Austin'
capitalCity['UT'] = 'Salt Lake City'
capitalCity['VT'] = 'Montpelier'
capitalCity['VA'] = 'Richmond'
capitalCity['WA'] = 'Olympia'
capitalCity['WV'] = 'Charleston'
capitalCity['WI'] = 'Madison'
capitalCity['WY'] = 'Cheyenne'
# FIXED Add rest of the states’ capital cities to capitalCity dictionary


def menu():
    print("""
            Enter one of the menu options:
            [1] Find US state's code given its name
            [2] Find US state's capital given its code
            [3] Find US state's capital given its name
            [4] Exit the program
        """)


def main():
    while True:
        # clear screen
        os.system('clear')
        # print menu
        menu()
        # get menu option
        option = input()
        if option == '4':
            print('SEE YOU AGAIN... GOOD BYE!')
            break

        if option == '1':
            state = input('Enter a US state name: ')
            if state in states:  # check if state is in states dict
                print('Code for {} is {}.'.format(state, states[state]))
            else:
                print("Sorry! The US state name '{}' NOT found!".format(state))

        elif option == '2':
            capital = input('Enter US state code: ')
            if capital in capitalCity:
                print('Capital for {} is {}.'.format(capital, capitalCity[capital]))
            else: 
                print("Apologies, the US state code '{}' not found.".format(capital))
        
        elif option == '3':
            state_capital = input('Enter US State name: ')
            if state_capital in states:
                print('Capital for {} is {}.'.format(state_capital, capitalCity[states[state_capital]]))
            else:
                print("Apologies, the US state name '{}' not found.".format(state_capital))

        else:
            continue
        
        # FIXED - complete menu option 2
      

        # FIXED - complete menu option 3

        # FIXED - handle the case where user enters invalid menu option
        print('Enter to continue...')
        input()


if __name__ == "__main__":
    main()