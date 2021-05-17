import datetime

deadline = input("Enter goal-deadline: ").split("-")

deadline_goal = deadline[0]
input_deadline_date = deadline[1]


deadline_date = datetime.datetime.strptime(input_deadline_date, "%d.%m.%y")
print(deadline_goal.capitalize() + " by",deadline_date)
current_date = datetime.datetime.today()
print("Today is:",current_date)

difference = deadline_date - current_date
print("Days left:",difference.days)
hours = difference.seconds//3600
minutes = (difference.seconds%3600)//60
seconds = (difference.seconds%3600)%60

# print(difference.seconds)
print("Time left: {} hours {} minutes {} seconds".format(hours,minutes,seconds))
# print("Time left: {}".format(round(difference.seconds/3600,2)))

print("Total left: {}".format(difference))