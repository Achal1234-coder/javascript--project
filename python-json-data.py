import csv
from collections import defaultdict
import json

# make short_form dictionary as global it contain sort form of teams
short_form = {'Royal Challengers Bangalore': 'RCB',
              'Rising Pune Supergiant': 'RPS',
              'Rising Pune Supergiants': 'RPS', 'Deccan Chargers': 'DC',
              'Mumbai Indians': 'MI', 'Kochi Tuskers Kerala': 'KTK',
              'Delhi Daredevils': 'DD', 'Gujarat Lions': 'GL',
              'Sunrisers Hyderabad': 'SH',
              'Rajasthan Royals': 'RR', 'Pune Warriors': 'PW',
              'Kolkata Knight Riders': 'KKR',
              'Chennai Super Kings': 'CSK', 'Kings XI Punjab': 'k XI P',
              'Rising Pune Supergiantss': 'RPS'}


# question1:- Total runs scored by team
def question1():
    ''' Define a function question1 to solve the problem 1.'''

    with open('deliveries.csv', 'r') as csv_file_deliveries:

        # make a object csv_read_deliveries of csv.DictReader class
        csv_read_deliveries = csv.DictReader(csv_file_deliveries)

        teams_run = defaultdict(int)

        for row in csv_read_deliveries:

            short_team_name = short_form[row['batting_team']]
            teams_run[short_team_name] += int(row['total_runs'])

    question1_json_object = json.dumps(teams_run, indent=4)

    with open("json/question1.json", "w") as outfile:
        outfile.write(question1_json_object)


# question2:- Top batsman for Royal Challengers Bangalore
def question2():
    ''' Define a function question2 to solve the problem 2.'''

    with open('deliveries.csv', 'r') as csv_file_deliveries:

        csv_read_deliveries = csv.DictReader(csv_file_deliveries)
        batsman_of_RCB = defaultdict(int)

        for row in csv_read_deliveries:

            if row['batting_team'] == 'Royal Challengers Bangalore':
                batsman_of_RCB[row['batsman']] += int(row['batsman_runs'])

        values = [(value, key) for (key, value) in batsman_of_RCB.items()]
        sort_batsman = sorted(values)
        sort_batsman.reverse()
        sort_batsman = [(value, key) for key, value in sort_batsman]
        batsman_of_RCB = dict(sort_batsman[:20])
        print(batsman_of_RCB)

    question2_json_object = json.dumps(batsman_of_RCB, indent=4)

    with open("json/question2.json", "w") as outfile:
        outfile.write(question2_json_object)


# question3:-  Foreign umpire analysis
def question3():
    ''' Define a function question3 to solve the problem 3.'''

    with open('matches.csv', 'r') as csv_file_matches:

        csv_read_matches = csv.DictReader(csv_file_matches)

        with open('umpires.csv', 'r') as csv_file_umpires:

            csv_read_umpires = csv.DictReader(csv_file_umpires)

            country_umpire = {}
            no_of_umpire = defaultdict(int)

            for row in csv_read_umpires:

                country_umpire[row['umpire']] = row[' country']

            for row in csv_read_matches:

                country1 = country_umpire.get(row['umpire1'], 'India').strip()
                country2 = country_umpire.get(row['umpire2'], 'India').strip()

                if country1 != 'India':

                    no_of_umpire[country1] += 1

                if country2 != 'India':

                    no_of_umpire[country2] += 1

    question3_json_object = json.dumps(no_of_umpire, indent=4)

    with open("json/question3.json", "w") as outfile:
        outfile.write(question3_json_object)


# question4:- Stacked chart of matches played by team by season
def question4():
    ''' Define a function question4 to solve the problem 4.'''

    with open('matches.csv', 'r') as csv_file_matches:

        csv_read_matches = csv.DictReader(csv_file_matches)

        # calculation code start from this line

        match_byteam_byseas = {}

        for row in csv_read_matches:

            short_form_team1 = short_form[row['team1']]
            short_form_team2 = short_form[row['team2']]

            if row['season'] not in match_byteam_byseas:

                # We use 2D dictionary ex:-{2017: defaultdict({MI: 1, RCB: 1})}
                match_byteam_byseas[row['season']] = defaultdict(int)

                match_byteam_byseas[row['season']][short_form_team1] = 1
                match_byteam_byseas[row['season']][short_form_team2] = 1

            else:
                match_byteam_byseas[row['season']][short_form_team1] += 1
                match_byteam_byseas[row['season']][short_form_team2] += 1

    question4_json_object = json.dumps(match_byteam_byseas)

    with open("json/question4.json", "w") as outfile:
        outfile.write(question4_json_object)


if __name__ == "__main__":

    question1()
    question2()
    question3()
    question4()
    print("JSON files generated in json-files directory")
