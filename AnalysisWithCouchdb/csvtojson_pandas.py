import pandas as pd
df = pd.read_csv(r'/Users/amanpreetsingh/Conestoga/Sem_1/NoSQL_Database/Week10_Couchdb/LocationVsPopularAgeVsFeature.csv')
df.to_json(r'/Users/amanpreetsingh/Conestoga/Sem_1/NoSQL_Database/Week10_Couchdb/LocationVsPopularAgeVsFeature.json',orient='records')
