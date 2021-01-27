# TERRA-REF Breeder's API (BRAPI)

Implementation of the BRAPI standard for TERRA-REF instance of the BETYdb database (terraref.org/bety).

## Mappings from BETY to BRAPI models

| BRAPI      | BETY        | Notes |
|------------|-------------|-------|
| /calls     | generated   |       |
| /events    | managements |       |
| /locations | sitegroups  | lat/lon computed from sites part of sitegroup |
| /seasons   | experiments | season = month of start_date, year of start_date |
| /germplasm  | cultivars.  |       | 
| /observations | traits | |

# Currently implemented endpoints & parameters

See [Swagger documentation](http://terraref.org/brapi/v1/ui) for more details

```
  /calls	
  	dataType
  	paging
  /commoncropnames
  	paging				
  /events
   date
   eventDbId
   eventDescription
   eventParameters
   eventType
   observationUnitDbIds
   studyDbId
  /locations
  	locationType - Unavailable
  	paging
  /locations/{locationDbId}
  /trials
  	commonCropName	
  	programDbId		
  	locationDbId - Not supported
  	active - Unavailable
  	sorting	- Not supported
  	paging
  /programs
  	commonCropName
  	programName	
  	abbreviation
  	paging		
  /seasons
  	seasonDbId	
  	season	
  	year	
  	paging	
  /studies
  	commonCropName - Not supported
  	studyTypeDbId - Unavailable
  	programDbId	- Not supported
  	locationDbId
  	seasonDbId
  	trialDbId - Not supported
  	studyDBId
  	active - Unavailable
  	sorting
  	paging
  /studies/{studyDbId}			
  /studies/{studyDbId}/germplasm
  	paging				
  /studies/{studyDbId}/layouts
  	paging				
  /observationunits
  	germplasmDbId		
  	observationVariableDbId	
  	studyDbId	
  	locationDbId	
  	trialDbId - Not supported
  	programDbId - Not supported
  	seasonDbId
  	observationLevel - Unavailable
  	observationTimeStampRangeStart
  	observationTimeStampRangeEnd
  	paging
  /germplasm
  	germplasmPUI			
  	germplasmDbId			
  	germplasmName		
  	commonCropName		
  	paging
```

## How to set up a development environment.

We assume you have the following installed:
- [Docker](https://www.docker.com/products/docker-desktop) (to run BETYdb)
- [Postman](https://www.postman.com/) (to test out APIs)
- [PyCharm](https://www.jetbrains.com/pycharm/) (for development)

### Run a development instance of BETYdb

The following commands can be used to initialize the database to be used with BRAPI development. This will fetch public data from TERRA-REF database (id=6). To get the latest data you can call the sync command. 

```bash
docker-compose up -d postgres
docker-compose run --rm bety initialize
docker-compose run --rm bety sync
```

_Note:_ If you get an error about port 5432 already in use, you likely need to stop another instance of postgres (locally or as docker).

### Set up PyCharm 

Now that you have BETYdb running on port 5432, you will be able to begin developing the server. These instructions assume that you are using PyCharm and have a project open to your brapi directory.

* Go to run --> edit configurations
* Set the "name" field to "server"
* Set the 'script path' to `<localpath>/brapi/server.py`
* In the top right of PyCharm, select the server configuration and click the green triangle to run the server
* In Postman test that the API exists by navigating to http://localhost:5000/brapi/v1/calls  

### How to evaluate changes in an endpoint

* modify the file named `api/<endpoint>.py`
* click the 'reload' button in PyCharm to restart the server
* reload the endpoint in Postman and determine if requested changes are present.
 
### How to add an endpoint

You will need add a new file under the `api` folder called with the name of the endpoint, for example the /locations endpoint will be defined in a file called api/locations.py. In that file you will need a `search` function to handle the call to the GET endpoint. If the function is not implemented the url will return the actual name of the file and the function name.

## Showing data in BETY database

You can use the following command to start a docker container that is connected to the database
allowing you to browse the database.

```
docker-compose up -d bety
```

To enable the guest user you can run the following sql query when
connected to the database:

```
INSERT INTO users (login, name, email, crypted_password, salt, city, state_prov, postal_code, country, area, access_level, page_access_level, created_at, updated_at, apikey, remember_token, remember_token_expires_at)
 VALUES ('guestuser', 'guestuser', 'betydb@example.com', '994363a949b6486fc7ea54bf40335127f5413318', 'bety', 'Urbana', 'IL', '61801', 'USA', '', 4, 4, NOW(), NOW(), NULL, NULL, NULL);
```

## Testing your additions

Before you commit your new endpoints or any new code, please make sure that you check it with
BRAVA. You can do this by running the brava container 

```sh 
docker-compose up -d brava
```

At this point you can connect to http://localhost:8080/ to see the Brava UI.

Next switch to 'Test your own' and change the URL. To launch the BrAPI:

```sh
docker-compose up -d brapi
```

If you run the brapi server as a docker container in docker-compose you can use `http://brapi:5000/brapi/v1` as the URL. If you run
the server on your machine you can either use `http://host.docker.internal:5000/brapi/v1` or
you can use `http://<ipaddress>:5000/brapi/v1`.


## Configuring and Augmenting the TERRA REF database

### Contributed Data

This repository provides the canonical reference for data that is
outside of the scope of databases used in the TERRA REF program. Such
data can be found in the `/contrib/` folder. 

Genomics data in `contrib/genomics` is in a set of CSVs that were
previously only available in the [experimental design section of the TERRA REF documentation](https://docs.terraref.org/scientific-objectives-and-experimental-design/experimental-design). These files provide metadata that describe the germplasm used in the sorghum trials, and were originally prepared by Noah Fahlgren.

The data in these files could be inserted into the BETYdb attributes table.

The data in `contrib/ontologies/variables_annotations.csv` contain sorghum phenotypes, descriptions, ontologyReference from the Plant Trait Ontology, and the persistent URL, which were annotated by [Laurel Cooper](https://agsci.oregonstate.edu/users/laurel-cooper). 

The file `contrib/ontologies/ontology_reference.json` contains metadata for the Plant Trait Ontology.

### Setup Locations

For the locations endpoint to work correctly we grouped multiple sites together in a sitegroup. The commands in `contrib/locations_setup.sql` were used to associate sites with the sitegroups. (This has been done and is now part of the TERRA-REF dump).
