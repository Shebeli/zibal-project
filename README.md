# Introduction

Hello and welcome

To setup project mongodb connection, refer to settings.py and update this parametrs as required:
- MONGO_USER
- MONGO_PASS
- MONGO_HOST 
- MONGO_NAME 

If you are running mongodb by its default setting and on local, (localhost:27017) just set MONGO_LOCAL to True and specify your database name on MONGO_NAME.

## New Transaction Collection

You can specify the number of max allowed documents on `transaction` collection by changing `MAX_TRANSACTION_COUNT` in the settings

This will save the new transaction document on `transaction_extra` collection whenever the count of transaction collection exceeds this constant.

## API Routes

- `/transaction` 
Based on query params given to this api, `mode`, `type` and optional `merchantId`, this API will give you the aggregated data as a response. for example:


`/transaction?type=count&mode=daily&merchantId=6110d2fa7462569413584c60`

- `/transaction_extra`
Same as `/transaction`, but will instead query the data from `transaction_extra` collection.

it takes the same query params as transaction route.

