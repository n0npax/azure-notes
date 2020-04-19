# logging
ingestion sampling to keep budget in rigour

## webapp
az webapp log config -n $NAME -g$GRP --level information --aplication-logging true
in app logging.AddAzureWebAppDiagnosticsi()
logger.LogInformation("foo")

## blob
az storage container policy create -c logs 
az storage container generate-sas

## Usage analytics
funnels  - user progression
impact - load times
retention - how many/ofter users returning/doing sth
user flow - navigation between pages

# autoscale
session state in Redis (classico)


# servicebus
az servicebus namespace create -n $NAME -g $GRP
az servicebus namespace authorization-rule key-list --namespace
az servicebus queue create --namespace
New-AzureRmServiceBusQueue

# eventgrid

az eventdrid event subscription create 

# api gw

openID - validate-jwt policy

* inbound - Auth, rate limiting, caching
* outbound - Filter, Transform, caching
* backend - Transform, slelect meth, retry

# search
az search service create -g $GRP --name $NAME --sku $PRICE_TIER
az search admin-key show --service-name $NAME -g $GRP --query "primaryKey"
az search admin-key list --service-name $NAME -g $GRP --query "[0].key"

## 
* searchServiceClient object - index mgmt (.indexex.Create)
* searchIndexClient - index search
* IndexBath.Upload
* Docsuments.Search<T>($QUERY, $PARAMS)
* searchable properties on item are required. Need to drop/rebuild if missing

# app logic
ways to build:
* visually with logic app desinger
* as a json (any ide)
* b2b integrations pack

## Error handling:
default: exp by 7.5sec min-5, max-45sec
expotential interval: random interval
fixed interval: guess what
none: Don't resend req

# cosmodb
az cosmosdb create --name $NAME -g $GRP --kind $KIND --location $LOCATION --default-consistency-level Strong --enable-multiple-write-location true --enable-automatic-failover
az cosmosdb database create -g $GRP --name $NAME --db-name $DB_NAME
az cosmosdb list-keys --name
az cosmosdb list-kets --name
az cosmosdb show --name $NAME -g $GRP --query $QUERY

# batch
az batch pool create
az batch job create
az batch task create
# aks
az aks create --node-count 3 --generate-ssh-keys -n $NAME -g $GRP
i
# web app service
az appservice plan create -n $PLANNAME -g $GRP # --sku $MACHINE_TYPE --is-linux
az webapp create -n $APPNAME -g $GRP --plan $PLANNAME # --deployment-container-image-name busybox
az webapp deployment source config -n $APPNAME -g $GRP --repo-url $URL --branch $BRANCH
az webapp deployment source config -n $APPNAME -g $GRP --settings WEBSITES_PORT=80

# security
sp - service principal

