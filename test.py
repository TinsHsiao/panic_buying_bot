import json

with open( "custermers.json" ) as f :
    p = json.load(f)
    print( p )
