from cgi import test


t1_goalsfor = 99
t2_goalsfor = 94
t3_goalsfor = 76

t1_goalsagainst = 26
t2_goalsagainst = 26
t3_goalsagainst = 33

t1_gd = t1_goalsfor - t1_goalsagainst
t2_gd = t2_goalsfor - t2_goalsagainst
t3_gd = t3_goalsfor - t3_goalsagainst

average_gd = (t1_gd + t2_gd + t3_gd) / 3

print(average_gd)