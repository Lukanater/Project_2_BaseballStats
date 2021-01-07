"""
Unit 2: Project: Baseball Stats:
////////
There are a use of dictionaries, because of a list of keys and values.
There is also a KWARGS; this is because there may be a group of arguments being made withen a function, or functions.

"""
import constants
import copy


copy.deepcopy()
deepcopy()
print("test import")
constants.basketball_st()
teams = input(teams)
teams = copy.deepcopy(TEAMS)
players = copy.deepcopy(PLAYERS)

def basketball_st():

    #teamstats = teams.stat
    #When someone chooses either a quit(player quits), and the Display team stats, he/she is then prompt to choose a team afterwards.
    startApp = input("Hear are your options! Pick one!")
    end_game = input(quit)
    end_game = input("Quit")
    displayStats = input(displayStats)
    displaySatts = input("Display team stats")
    
    try:
        startApp = input()
    
    while True:
         if startApp == True:
            print(displayStats)
            print(end_game)
            if displayStats:
                print("Choose reguistar a team.")
                print("Choose a team based on options below:{}".format(teams))
            elif:
                print("Are you ready to choose your team yet?")
                
                continue
                
            else:
                print(end_game)
                end_game = input(quit)
    print("Welcome to Generic BasketBall Game!!!")
    print(" /n Reguistar you team!!!!!")
    for team in teams:
    """ Think of getting KWARGS and reference use of dictionaries."""
        if team == "Panthers":
            """ PLAYERS are selected: Karl Saygan, Matt Gill, Sammy Adams, Chloe Alaska, Bill Bon, Jie Kavalier"""
            #Will lead to referencing keys and values;dictionaries#also references indexes of each players attributes, []
            
        if team == "Bandits":
            """ PLAYERS are selected: Les Clay, Phillip Helm, Sal Dali, Suzane Greenberg, Jill Tanner, Alnold Willis"""
            #Will lead to referencing keys and values;dictionaries

print basketball_st()        
#def        

#__Name__
"""TEAMS = [
    'Panthers',
    'Bandits',
    'Warriors',
]

PLAYERS = [{
        'name': 'Karl Saygan',
        'guardians': 'Heather Bledsoe',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Matt Gill',
        'guardians': 'Charles Gill and Sylvia Gill',
        'experience': 'NO',
        'height': '40 inches'
    },
    {   'name': 'Sammy Adams',
        'guardians': 'Jeff Adams and Gary Adams',
        'experience': 'NO',
        'height': '45 inches'
    },
    {
        'name': 'Chloe Alaska',
        'guardians': 'David Alaska and Jamie Alaska',
        'experience': 'NO',
        'height': '47 inches'
    },
    {
        'name': 'Bill Bon',
        'guardians': 'Sara Bon and Jenny Bon',
        'experience': 'YES',
        'height': '43 inches'
    },
    {
        'name': 'Joe Kavalier',
        'guardians': 'Sam Kavalier and Elaine Kavalier',
        'experience': 'NO',
        'height': '39 inches'
    },
    {
        'name': 'Phillip Helm',
        'guardians': 'Thomas Helm and Eva Jones',
        'experience': 'YES',
        'height': '44 inches'
    },
    {
        'name': 'Les Clay',
        'guardians': 'Wynonna Brown',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Sal Dali',
        'guardians': 'Gala Dali',
        'experience': 'NO',
        'height': '41 inches'
    },
    {
        'name': 'Suzane Greenberg',
        'guardians': 'Henrietta Dumas',
        'experience': 'YES',
        'height': '44 inches'
    },
    {
        'name': 'Jill Tanner',
        'guardians': 'Mark Tanner',
        'experience': 'YES',
        'height': '36 inches'
    },
    {
        'name': 'Arnold Willis',
        'guardians': 'Claire Willis',
        'experience': 'NO',
        'height': '43 inches'
    },
    {
        'name': 'Herschel Krustofski',
        'guardians': 'Hyman Krustofski and Rachel Krustofski',
        'experience': 'YES',
        'height': '45 inches'
    },
    {
        'name': 'Eva Gordon',
        'guardians': 'Wendy Martin and Mike Gordon',
        'experience': 'NO',
        'height': '45 inches'
    },
    {
        'name': 'Ben Finkelstein',
        'guardians': 'Aaron Lanning and Jill Finkelstein',
        'experience': 'NO',
        'height': '44 inches'
    },
    {
        'name': 'Joe Smith',
        'guardians': 'Jim Smith and Jan Smith',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Diego Soto',
        'guardians': 'Robin Soto and Sarika Soto',
        'experience': 'YES',
        'height': '41 inches'
    },
    {
        'name': 'Kimmy Stein',
        'guardians': 'Bill Stein and Hillary Stein',
        'experience': 'NO',
        'height': '41 inches'
    }
]
"""
