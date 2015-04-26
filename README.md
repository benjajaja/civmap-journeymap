Civcraft map data
=================

This repo is where player contributions are saved.

### How to contribute imagery

You can add what you have mapped with journeymap. Go to your journeymap folder, usually  `.minecraft/journeyMap/data/mp/<civcraft>` where `<civcraft>` is a placeholder for whatever journeymap created, it seems that in latest versions it is whatever you named the server in the server list in-game. From there, enter `DIM0` and create an archive of `day`. An example of a full path would be `.minecraft/journeyMap/data/mp/civcraft_0/DIM0/day`. That folder *only* contains your tiles and not your waypoints or other irrelevant but potentially sensitive data.

You should then post an issue in this repo stating that you have imagery in the issue title, and a download link (google drive, dropbox, mediafire...) to the archive.

### How to contribute overlay data

#### Points (cities, towns, POI)

Also to be submitted as issues (one issue per entry) in this repo.  
For points, you must include:

* Type (city, town...)
* Name
* Coordinates in this format: `x,y` e.g. `-1000,3400`
* Flag image link, preferrably "imgur" about 200x100 pixels

Additionally you can optionally include the following info: 

* Subreddit
* Market link if any (only if your city has an actual market site that is used)
* Nether portal with specific coordinates, and optional description if coordinates are not sufficient
* Desired two-letter code
* If place is abandoned

#### Rails

Create an issue with an image with the rails drawn over the map. Rails MUST follow exact underground path. A rail addition may take longer if it is considered necessary to be verified in person (in game).

### How does all this work?

See https://github.com/gipsy-king/civmap-client
