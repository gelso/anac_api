# AppaltoBaseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_appalto** | **str** | identificativo univoco dell&#x27;Appalto definito da ANAC. Restituito dall&#x27;operazione di creazione Appalto. (A UUID specified by RFC4122) | [optional] 
**codice_appalto** | **str** | identificativo univoco dell&#x27;Appalto definito dal SA. | [optional] 
**oggetto** | **str** | descrizione dell&#x27;appalto | [optional] 
**data_creazione** | **datetime** | data creazione dell&#x27;appalto (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
**stato** | [**StatoAppaltoEnum**](StatoAppaltoEnum.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

