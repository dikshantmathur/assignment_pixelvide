#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import math


num_teams = 32
country_list = {"england" : ["English", 4], "france" : ["French", 2],
                "spain" : ["Spanish", 5], "germany" : ["German", 4],
                "italy" : ["Italian", 2], "portugal" : ["Portuguese", 2],
                "russia" : ["Russian", 2], "kazakistan" : ["kaz", 1],
                "turkey" : ["Turkish", 1], "Israel" : ["Israeli", 1],
                "greece" : ["Greek", 1], "netherland" : ["ned", 1],
                "belgium" : ["Belgian", 1], "ukraine" : ["ukr", 2], "croatia" : ["cro", 1], "sweeden" : ["swe", 1], "Belarus" : ["blr", 1]}
group_and_teams = {"GroupA" : {}, "groupB" : {}, "groupC" : {}, "groupD" : {},
                   "groupE" : {}, "groupF" : {}, "groupG" : {}, "groupH" : {}}

print("\tUEFA Champions League Draw Simulator\n")
print("Enter teams to make your very own UEFA Champions League.")
input("Press the enter key to begin.")
x = 0
for country in country_list:
    x += country_list[country][1]
x = math.ceil(x / len(group_and_teams))

list_teams = {}
for country in country_list:
    for x in range(country_list[country][1]):
        list_teams[input("Please enter an {} team: ".format(country_list[country][0]))] = country

def find_open_slot(new_team):
    good = True
    group_chosen = False
    rand = random.sample(list(group_and_teams), 1)[0]
    while group_chosen == False:
        if len(group_and_teams[rand]) > 0:
            for listed_team in group_and_teams[rand]:
                if new_team == listed_team or list_teams[new_team][1] == group_and_teams[rand][listed_team]:
                    good = False
        else:
            group_chosen = True
            return rand

        if good == False:
            rand = random.sample(list(group_and_teams), 1)[0]
        else:
            group_chosen = True
            return rand

for team in list_teams:
    group = find_open_slot(team)
    teams = group_and_teams[group]
    teams[team] = list_teams[team]

print("\nAssembling groups...\n")
input("Groups complete. Press the enter key to view.")

for group in group_and_teams:
    for teams in group_and_teams[group]:
        print("{}: team: {}, Country: {}".format(group,teams, group_and_teams[group][teams]))

input("\n\nPress the enter key to exit.")


# In[ ]:




