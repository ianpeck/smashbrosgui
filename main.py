import sql as s
fighter1 = 'Bowser'
map = 'Corneria'

data_fighter_1 = s.select_view_row("SELECT * FROM CareerStatsByLocation WHERE Fighter_Name = '{}' AND Location_Name = '{}'".format(fighter1, map.replace("'","''")))
print(data_fighter_1[0])


listy = [1,2,3,4,5]

print(2 % 2)

