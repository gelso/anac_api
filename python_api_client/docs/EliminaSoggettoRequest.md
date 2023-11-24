# EliminaSoggettoRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_fiscale** | **str** | codice fiscale del soggetto. Obbligatorio se idAppalto non è stato valorizzato | [optional] 
**id_appalto** | **str** | Identificativo univoco dell&#x27;Appalto definito da ANAC. Obbligatorio se codiceFiscale non è stato valorizzato | [optional] 
**cig** | **str** | Non gestito nella prima release - Identificativo univoco Gara-Lotto generato da ANAC. | [optional] 
**ruolo** | [**TipoRuoloEnum**](TipoRuoloEnum.md) |  | [optional] 
**servizio** | [**TipoServizioSoggettoEnum**](TipoServizioSoggettoEnum.md) |  | [optional] 
**operazione** | [**TipoOperazioneSoggettoEnum**](TipoOperazioneSoggettoEnum.md) |  | [optional] 
**data_inizio** | **datetime** | Data di inizio (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
**data_fine** | **datetime** | Data di fine (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

