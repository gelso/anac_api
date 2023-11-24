# StatoAvvisoType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_avviso** | **str** | identificativo univoco dell&#x27;Avviso generato da ANAC. | [optional] 
**id_appalto** | **str** | identificativo univoco dell&#x27;Appalto definito da ANAC. Valorizzato se l&#x27;avviso è relativo ad un Appalto. (A UUID specified by RFC4122) | [optional] 
**id_pianificazione** | **str** | identificativo univoco della Pianificazione definito da ANAC. Valorizzato se l&#x27;avviso è relativo ad un Piano. (A UUID specified by RFC4122) | [optional] 
**data_controllo** | **datetime** | data in cui è stato effettuato il controllo sullo stato dell&#x27;avviso (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
**stato** | [**StatoAvvisoEnum**](StatoAvvisoEnum.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

