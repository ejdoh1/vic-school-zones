import geopandas as gp

df = gp.read_file('Speed_Zones.shp')
df = df.loc[df["Variable_C"].str.contains("SCHOOL", na=False)]
df = df.to_crs(epsg=4326)
with open('Speed_Zones.json', 'w') as f:
    f.write(df.to_json())
