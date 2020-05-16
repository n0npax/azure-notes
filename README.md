# Azure notes
Some commands, copied docs(from [microsoft](https://docs.microsoft.com)) and memos about azure

# Databricks
same as apache spark

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
az storage container policy create -c logs --name foo --start --expiry --permission lwrd --account-name --account-key
```

1. Positive -> `ETAG` property
2. Negative -> Lease


## Usage analytics

### funnels  - user progression, track progression
If your application involves multiple stages, you need to know if most customers are progressing through the entire process, or if they are ending the process at some point. The progression through a series of steps in a web application is known as a funnel. You can use Azure Application Insights Funnels to gain insights into your users, and monitor step-by-step conversion rates.

### impact - load times, how load time impact progression
Impact analyzes how load times and other properties influence conversion rates for various parts of your app. To put it more precisely, it discovers how any dimension of a page view, custom event, or request affects the usage of a different page view or custom event.

One way to think of Impact is as the ultimate tool for settling arguments with someone on your team about how slowness in some aspect of your site is affecting whether users stick around. While users may tolerate a certain amount of slowness, Impact gives you insight into how best to balance optimization and performance to maximize user conversion.

### retention - how many/ofter users returning/doing sth
The retention feature in Azure Application Insights helps you analyze how many users return to your app, and how often they perform particular tasks or achieve goals. For example, if you run a game site, you could compare the numbers of users who return to the site after losing a game with the number who return after winning. This knowledge can help you improve both your user experience and your business strategy.

### user flow - navigation between pages and features, people doing repetitive actions
The User Flows tool visualizes how users navigate between the pages and features of your site. It's great for answering questions like:

* How do users navigate away from a page on your site?
* What do users click on a page on your site?
* Where are the places that users churn most from your site?
* Are there places where users repeat the same action over and over?
* The User Flows tool starts from an initial page view, custom event, or exception that you specify. Given this initial event, User 

Flows shows the events that happened before and afterwards during user sessions. Lines of varying thickness show how many times each path was followed by users. Special Session Started nodes show where the subsequent nodes began a session. Session Ended nodes show how many users sent no page views or custom events after the preceding node, highlighting where users probably left your site.

### Users, sessions, and events analysis in Application Insights
Find out when people use your web app, what pages they're most interested in, where your users are located, and what browsers and operating systems they use. Analyze business and usage telemetry by using Azure Application Insights.

### cohort
A cohort is a set of users, sessions, events, or operations that have something in common. In Azure Application Insights, cohorts are defined by an analytics query. In cases where you have to analyze a specific set of users or events repeatedly, cohorts can give you more flexibility to express exactly the set you’re interested in.

# autoscale
session state in Redis (classico)


# servicebus

```bash
az servicebus namespace create -n $NAME -g $GRP
az servicebus namespace authorization-rule key-list --namespace
az servicebus queue create --namespace
```

new queue
```bash
New-AzureRmServiceBusQueue
```

# eventgrid

```bash
az eventdrid event subscription create 
```

subscription filters
* Event
* Subject Begins with
* Subject Ends With
* Advanced filters (operator key, Value)



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
* **searchServiceClient** object - index mgmt (.indexex.Create)
* **searchIndexClient** - index search
* **IndexBath** Upload
* **Indexes** Create
* **Docsuments.Search<T>($QUERY, $PARAMS)**
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
az cosmosdb show --name $NAME -g $GRP --query $QUERY
```

# sql
json and sql queries -> SQL type

## Consistency Levels
* Strong
* Bounded-staleness
* Session
* consistent prefix
* Eventual

## TDE
TDE encrypts the entire database using an AES encryption algorithm which doesn’t require application developers to make any changes to existing applications. TDE performs real-time I/O encryption and decryption of the data and log files. Once the database is loaded into memory, the data is accessible to administrators (DBAs) of SQL Server (sysadmin, db_owner), and Azure SQL Database (cloud) administrators and can be used by all roles and applications that have access to the database. If a database contains sensitive data in specific columns that needs to be protected from administrator roles and remain encrypted in memory, using Always Encrypted should be evaluated in addition to TDE.

## Always encrypted
Always Encrypted is a feature designed to protect sensitive data, stored in Azure SQL Database or SQL Server databases from access by database administrators (e.g. the members of the SQL Server sysadmin or db_owner roles), administrators of machines hosting SQL Server instances,), and Azure SQL Database (cloud) administrators. Data stored in the database is protected even if the entire machine is compromised, for example by malware. Always Encrypted leverages client-side encryption: a database driver inside an application transparently encrypts data, before sending the data to the database. Similarly, the driver decrypts encrypted data retrieved in query results.

With Always Encrypted, cryptographic operations on the client-side use keys that are never revealed to the Database Engine (SQL Database or SQL Server). There are two types of keys in Always Encrypted:

Column encryption keys are used to encrypt data in the database. These keys are stored in the database in the encrypted form (never in plaintext).
Column master keys are used to encrypt column encryption keys. These keys are stored in an external key store, such as Windows Certificate Store, Azure Key Vault or hardware security modules.  For keys stored in Azure Key Vault, only the client application has access to the keys, but not the database, unlike TDE.

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

az aks enable-addons # i.e monitor
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

## SQL

```bash
az sql db list
az sql db show-connection-string --client sqlcmd --name Logistics
```


# Sampling

## Adaptive sampling
Adaptative sampling automatically adjusts the volume of telemetry sent from the SDK in your ASP.NET/ASP.NET Core app, and from Azure Functions. This is the default sampling when you use the ASP.NET or ASP.NET Core SDK. Adaptive sampling is currently only available for ASP.NET server-side telemetry, and for Azure Functions.

# Fixed rate
Fixed-rate sampling reduces the volume of telemetry sent from both your ASP.NET or ASP.NET Core or Java server and from your users' browsers. You set the rate. The client and server will synchronize their sampling so that, in Search, you can navigate between related page views and requests.

# Ingestion sampling
Ingestion sampling happens at the Application Insights service endpoint. It discards some of the telemetry that arrives from your app, at a sampling rate that you set. It doesn't reduce telemetry traffic sent from your app, but helps you keep within your monthly quota. The main advantage of ingestion sampling is that you can set the sampling rate without redeploying your app. Ingestion sampling works uniformly for all servers and clients, but it does not apply when any other types of sampling are in operation.

