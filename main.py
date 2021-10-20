import sql as s

data = s.query_sql("call SmashBros.headtohead('Mario');")

print(data)
