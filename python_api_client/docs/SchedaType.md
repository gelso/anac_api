# SchedaType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_scheda** | **str** | Codice univoco della scheda. il campo viene determinato da anac e restituito nelle response. viene dunque ignorato il valore inserito nella post. | [optional] 
**codice** | [**CodiceSchedaEnum**](CodiceSchedaEnum.md) |  | 
**versione** | **str** | versione della scheda. necessaria al motore interno ANAC. | 
**stato** | [**StatoSchedaEnum**](StatoSchedaEnum.md) |  | [optional] 
**data_creazione** | **datetime** | data creazione della scheda (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

