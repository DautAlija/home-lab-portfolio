from dotenv import load_dotenv 
import os
import requests 
from dataclasses import dataclass 


load_dotenv() 

API_TOKEN = os.environ.get("FOOTBALL_API_TOKEN")

r = requests.get('https://api.football-data.org/v4/teams/73', headers={'X-Auth-Token':API_TOKEN})

    #prints status code 200 means good, 403 meand connected but refusing access. 
    #or you can do r.status_code
#print(r) 

    #this returns all data in json format
# print(r.json()) 

    # shows attributes and methods that we can use  or use help(r) its way more detailed 
#print(dir(r))

    #returns headers 
#print(r.headers) 

r1 = requests.get('https://api.football-data.org/v4/persons/8133', headers={'X-Auth-Token':API_TOKEN})
#print(r1.json()) 


    #create player data variable that pullls from api request var r1.json() 
player_data = r1.json() 

    #decorator class created to pull information that i want 
@dataclass 
class PlayerItem: 
    name: str           #fields that i want (includes type )
    position: str
    nationality: str 
    shirtNumber: int    #change type str -> int. check using this request: print(type(player_data["shirtNumber"]))

    # creates player var to use later(such as print) cleans code and ease of use. 
    # nameofClass(ClassField=jsonRequestVariable["fieldNameInJson"])
player = PlayerItem(name=player_data["name"], position=player_data["position"], nationality=player_data["nationality"],shirtNumber=player_data["shirtNumber"])
#print(player)


#------------------------------------------------------------
    #create a new dataclass for player name and postion to store in a list. 

@dataclass
class SquadMember: 
    name : str 
    position : str 

team_data = r.json()  # request to to api to pull r var team info and store in variable team_data 

#print(team_data["squad"])   

    # create a function that creates a list(squadList) and loops through team_data storing name,position data. 
def build_squad(team_data): 
    squadList = []      # empty list 
    for player in team_data["squad"]:  # for variable(player) in team_data(pulled info) ... 
        squadList.append(SquadMember(name = player["name"],position = player["position"]))   #append keyword to add values to list, ... 
    print(squadList)        # use new data class (SquadMember(variable = loop var name["json name"]) for name and position) 
    return squadList        #print list and return list. 

    # ^^ the above works fine just prints really ugly, so loop below used to print name position cleanly. 

squad = build_squad(team_data) # create var(squad) to store function data and print it cleanly with f"..." string 
for member in squad: 
    print(f"Player:  {member.name}, \nPosition: {member.position}")