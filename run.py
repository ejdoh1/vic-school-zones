import geopandas as gp

df = gp.read_file('Speed_Zones.shp').to_crs(epsg=4326)
df = df.loc[df['SIGN_SPEED'] == 40]
with open('Speed_Zones.json', 'w') as f:
    f.write(df.to_json())
