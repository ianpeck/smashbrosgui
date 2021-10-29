import sql as s
fighter1 = 'Bowser'
map = 'Corneria'

data_fighter_1 = s.select_view_row("SELECT * FROM CareerStatsByLocation WHERE Fighter_Name = '{}' AND Location_Name = '{}'".format(fighter1, map.replace("'","''")))
print(data_fighter_1[0])


queries = "SELECT * FROM CareerStatsByLocation WHERE Fighter_Name = '{fighter1}' AND Location_Name = '{map}' UNION ALL SELECT * FROM CareerStatsByLocation WHERE Fighter_Name = '{fighter2}' AND Location_Name = '{map}' UNION ALL SELECT * FROM CareerStatsByFightType WHERE Fighter_Name = '{fighter1}' AND FightType = '{matchType}' UNION ALL SELECT * FROM CareerStatsByFightType WHERE Fighter_Name = '{fighter2}' AND FightType = '{matchType}' UNION ALL SELECT * FROM champfightstats WHERE Fighter_Name = '{fighter1}' UNION ALL SELECT * FROM champfightstats WHERE Fighter_Name = '{fighter2}' UNION ALL SELECT * FROM CareerStatsByPPV WHERE Fighter_Name = '{fighter1}' AND PPV = '{ppv}' UNION ALL SELECT * FROM CareerStatsByPPV WHERE Fighter_Name = '{fighter2}' AND PPV = '{ppv}' UNION ALL SELECT * FROM defendingtitle WHERE Fighter_Name = '{fighter1}' UNION ALL SELECT * FROM defendingtitle WHERE Fighter_Name = '{fighter2}' UNION ALL SELECT * FROM careerstats WHERE Fighter_Name = '{fighter1}' UNION ALL SELECT * FROM careerstats WHERE Fighter_Name = '{fighter2}' UNION ALL SELECT * FROM CareerStatsBySeason WHERE Fighter_Name = '{fighter1}' AND Season = '{season}' UNION ALL SELECT * FROM CareerStatsBySeason WHERE Fighter_Name = '{fighter2}' AND Season = '{season}' UNION ALL SELECT * FROM CareerStatsByBrand WHERE Fighter_Name = '{fighter1}' AND Brand = '{brand}' UNION ALL SELECT * FROM CareerStatsByBrand WHERE Fighter_Name = '{fighter2}' AND Brand = '{brand}'".format(fighter1=fighter1,fighter2=fighter2,ppv=ppv,matchType=matchType, map=map,season=season,brand=brand)


