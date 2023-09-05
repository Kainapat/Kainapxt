# Define the teams and their members
TeamA = ['Somchai', 'Somkiet', 'Daycha', 'Yodchai', 'Petch', 'Sopa']
TeamB = ['Nares', 'Sopa', 'Nipa', 'Daycha', 'Pimon', 'Petch']
TeamC = ['Choojai', 'Sopa', 'Somkiet', 'Nares', 'Nipa', 'Daycha', 'Tawan']
TeamD = ['Sopa', 'Tawan', 'Pimon', 'Yodchai', 'Petch', 'Somjai']

# Define the rewards based on team membership
Reward = [0, 5000, 7500, 10000, 15000]

# Create a dictionary to store rewards for each team member
rewards = {}

# Calculate rewards based on the number of teams each member is in
for member in set(TeamA + TeamB + TeamC + TeamD):
    num_teams = sum([member in team for team in [TeamA, TeamB, TeamC, TeamD]])
    rewards[member] = Reward[num_teams]

# Display the rewards in a table format
print("REWARDS FOR SALE TEAM")
print("----------------------")
print("Name           Reward")
print("----------------------")

total_reward = 0
for member, reward in rewards.items():
    print(f"{member:15s} {reward:7,}")
    total_reward += reward

print("----------------------")
print(f"Total          {total_reward:7,}")
print("----------------------")