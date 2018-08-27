"""
TARA WALTON
Write a program that lets the user enter the name of a team and then displays the number of times that team has won the World Series since 1903.
Format the ouput of your program as shown in the sample program runs. Design your program so that it contains at least one function other than the main function. 
No code should appear outside functions.

INPUT:	WorldSeriesWinners.txt

OUTPUT: display team name and count 
"""

def readfile(fname):
    '''Return a list of lines from the file (each line is a string)'''
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
     
    #print(lines)
    return lines


def build_team_dict(data):
    '''Return a dictionary in form of {team: count}'''
    
    team_d = {}       
    for team in data:  
        if team not in team_d:
            team_d[team] = 1
        else:
            team_d[team] += 1
            
    #print(team_d)
    return team_d


def query_team(team_d):
    '''Allow user enter a team name . Enter q to quit.'''
    
    print("What team would you like to search for? Enter 'q 'to quit.")
    query = input("Enter the team name.  ")
    #query = query.lower()
    keys = list(team_d.keys())
    keys = keys.sort
    while query != 'q':
        if query not in team_d:
            print("Sorry that team is not listed or there was an error. Please try again.")
            query = input("Enter the team name.  ")
        else:
            print(query, "have won ", team_d[query], "times.")
            query = input("Enter another name to search again. Enter 'q' to quit.  ")


def main():  #Don't change anything below here
    input_fname = 'WorldSeriesWinners.txt'
    data = readfile(input_fname)
    team_d = build_team_dict(data)
    query_team(team_d)
    

main()  
