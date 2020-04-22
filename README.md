---
# logging
ingestion sampling to keep budget in rigour

## webapp
```bash
az webapp log config -n $NAME -g$GRP --level information --aplication-logging true
```
in app logging.AddAzureWebAppDiagnosticsi()
logger.LogInformation("foo")

## blob

```bash
az storage container policy create -c logs 
az storage container generate-sas
```

## Usage analytics
funnels  - user progression
impact - load times
retention - how many/ofter users returning/doing sth
user flow - navigation between pages

# autoscale
session state in Redis (classico)


# servicebus

```bash
az servicebus namespace create -n $NAME -g $GRP
az servicebus namespace authorization-rule key-list --namespace
az servicebus queue create --namespace
New-AzureRmServiceBusQueue
```

# eventgrid

```bash
az eventdrid event subscription create 
```
# api gw

openID - validate-jwt policy

* inbound - Auth, rate limiting, caching
* outbound - Filter, Transform, caching
* backend - Transform, slelect meth, retry

# search

```bash
az search service create -g $GRP --name $NAME --sku $PRICE_TIER
az search admin-key show --service-name $NAME -g $GRP --query "primaryKey"
az search admin-key list --service-name $NAME -g $GRP --query "[0].key"
```

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

```bash
az cosmosdb create --name $NAME -g $GRP --kind $KIND --location $LOCATION --default-consistency-level Strong --enable-multiple-write-location true --enable-automatic-failover
az cosmosdb database create -g $GRP --name $NAME --db-name $DB_NAME
az cosmosdb list-keys --name
az cosmosdb list-kets --name
az cosmosdb show --name $NAME -g $GRP --query $QUERY
```
# batch

```bash
az batch pool create
az batch job create
az batch task create
```

# aks

```bash
az aks create --node-count 3 --generate-ssh-keys -n $NAME -g $GRP
az aks create -g $GRP -n $CLUSTER_NAME --node-count=1 --generate-ssh-keys --enable-addons monitoring --node-vm-size Standard_A2_v2
az aks get-credentials  -g $REGION  -n $CLUSTER_NAME

```

# web app service

```bash
az appservice plan create -n $PLANNAME -g $GRP # --sku $MACHINE_TYPE --is-linux
az webapp create -n $APPNAME -g $GRP --plan $PLANNAME # --deployment-container-image-name busybox
az webapp deployment source config -n $APPNAME -g $GRP --repo-url $URL --branch $BRANCH
az webapp deployment source config -n $APPNAME -g $GRP --settings WEBSITES_PORT=80
```

# security
sp - service principal
msi - Managed service identity
sas - Shared access signature

```bash
az ad sp create-for-rbac --name $SPNAME $SP
```

## Roles
```bash
az role definition list --output json
az role assignment list --assigne $SP.appID
az role assignment create --role $ROLE --assignee $SP.appId --role "Website Contributor"
az role definition list --output json
```

## MSI
```bash
az webapp indentity assign -g $GRP 0n $WEBAPP_NAME

az sql server ad-admin create --resource-group $RES_GRP --server-name $SERVER_NAME --display-name $ADMIN_USER --object-id $FROM_PREV_STEP

```

## SAS

```bash
# Token
az storage blob generate-sas --start --expiry --permission --name foo.svg --container-name --account-name --account-key
# url
az storage blob url --account-name --account-key --name --container-name --sas $SAS -o tsv
```

## KeyVault

```bash
az keyvault create -n $NAME -g $GRP --sky $PRIcING_TIER
az keyvault secret set --name $NAME --vault-name $VAULT_NAME --value "my password mate"
az ad sp create-for-ebac --name $SP_NAME | jq
az keyvault set-policy --name $kvname --spn $SP_NAME --secret-permission get

```

## Storage accounts

```bash
az ad sp create-for-rbac -n $NAME
az role assignment delete --assignee $SP_APPID  --role Contributor 
```

## DDM (Dynamic Data Masking)
```bash
New-AzureRmSqlDatabaseDataMaskingRule -ServerNAme $SRV_NAME -DatabaseName $DB_NAME -ResourceGroupName $RES_GRP -schemaName dbo  -MaskingFunction Text -TableNAme "Foos"  --ColumnName "Bars" --suffixSize 3 --ReplaceString "xxxxxxxxxxxxxx"
```

```sql
use masking;
GO
```

