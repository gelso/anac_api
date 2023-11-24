# SoggettoRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_fiscale** | **str** | codice fiscale del soggetto. | 
**id_appalto** | **str** | Identificativo univoco dell&#x27;Appalto definito da ANAC. | 
**cig** | **str** | Non gestito nella prima release - Identificativo univoco Gara-Lotto generato da ANAC. | [optional] 
**ruolo** | [**TipoRuoloEnum**](TipoRuoloEnum.md) |  | 
**servizio** | [**TipoServizioSoggettoEnum**](TipoServizioSoggettoEnum.md) |  | [optional] 
**operazione** | [**TipoOperazioneSoggettoEnum**](TipoOperazioneSoggettoEnum.md) |  | [optional] 
**data_inizio** | **datetime** | Data di inizio (A date-time specified by ISO 8601 as profiled by RFC 3339) | 
**data_fine** | **datetime** | Data di fine (A date-time specified by ISO 8601 as profiled by RFC 3339). Se il valore non è indicato la delega è a tempo indeterminato. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

