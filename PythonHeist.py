import os

clear = lambda: os.system('cls')


listOfTeamMembers = []

print("Plan Your Heist!")

while True:
    teamMemberDictionary = {}
    teamMemeberName = input("Please Enter a Name (Or leave blank to move on): ")
    teamMemberDictionary.append("Name", teamMemeberName)

    if teamMemeberName != "":
        teamMemberSkill = input("Please Enter their Skill level (1-20): ")
        teamMemberDictionary.append("Skill", teamMemberSkill)

        teamMemberCourage = input("Please Enter their Courage Factor (0.0 - 2.0): ")
        teamMemberDictionary.append("Courage", teamMemberCourage)

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

        for member in listOfTeamMembers:
            skillLevel = teamMemberDictionary.get("Skill")
            skillNumber = int(skillLevel)
            combinedSkill += skillNumber

        clear()

        for (i = 1; i <= trialRunsNumber; i += 1):
            