# Tennis-SF Scraper

This is a little python script to scrape and parse the courts listed on tennis-sf.com and structure them. The output will be a list of courts, like so:

```
[{
  'name': 'Buena Vista Park',
  'has_fee': False,
  'is_tennis_club': False,
  'courts': 2,
  'has_lights': False,
  'address': 'Haight St and Buena Vista Ave W, SF CA  94117',
  'is_restricted': False,
  'geo': {
      'lat': '37.7704789',
      'lng': '-122.4433505'
  },
  'has_wall': False
},
...the other courts...
]
```

It' currently hard-coded to work with the ["San Francisco-North"](https://www.tennissf.com/SF-Tennis-Courts?id=54) region on the Tennis-SF website.
