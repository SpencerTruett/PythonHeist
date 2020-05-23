import os
from random import seed
from random import randint
import random

clear = lambda: os.system('cls')


listOfTeamMembers = []

print("Plan Your Heist!")

while True:
    teamMemberDictionary = {'key' : 'value'}
    teamMemeberName = input("Please Enter a Name (Or leave blank to move on): ")
    teamMemberDictionary['Name'] = teamMemeberName

    if teamMemeberName != "":
        teamMemberSkill = int(input("Please Enter their Skill level (1-20): "))
        teamMemberDictionary['Skill'] = teamMemberSkill

        teamMemberCourage = float(input("Please Enter their Courage Factor (0.0 - 2.0): "))
        teamMemberDictionary['Courage'] = teamMemberCourage

        listOfTeamMembers.append(teamMemberDictionary)

        clear()

    else:
        bankDifficulty = input("Please Enter the Bank's Difficulty (1-100): ")
        bankDifficultyNumber = int(bankDifficulty)

        combinedSkill = 0

        trialRuns = input("How many times would you like to run the scenario? ")
        trialRunsNumber = int(trialRuns)
        successfulRun = 0
        unsuccessfulRun = 0

        for teamMemberDictionary in listOfTeamMembers:
            skillLevel = teamMemberDictionary["Skill"]
            skillNumber = skillLevel
            combinedSkillLevel = 0
            combinedSkillLevel += skillNumber

        clear()

        for _ in range(trialRunsNumber):
            random.seed()
            for _ in range(1):
                luckValue = randint(1, 3)
            totalBankDifficulty = bankDifficultyNumber + luckValue

            print("Team's Comined Skill: ", + combinedSkillLevel)
            print("Bank Difficulty: ", + totalBankDifficulty)
            print("Luck Value: ", + luckValue)

            if combinedSkillLevel >= totalBankDifficulty:
                print("You could pull off this heist!")
                print("--------------")
                successfulRun += 1
            else:
                print("Not a chance. Recruit some more and try again.")
                print("--------------")
                unsuccessfulRun += 1

        print("---------------------------")
        print("You succeeded ", + successfulRun, " times! And Failed ", + unsuccessfulRun, " times!")
        break