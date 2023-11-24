# AvvisoCommonType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_avviso** | **str** | identificativo univoco dell&#x27;Avviso generato da ANAC. | [optional] 
**data_creazione** | **datetime** | Data di crezione dell&#x27;Avviso  (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
**data_pubblicazione** | **datetime** | Data di pubblicazione dell&#x27;Avviso. (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
**data_controllo** | **datetime** | data in cui è stato effettuato il controllo dello stato avviso (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
**stato** | [**StatoAvvisoEnum**](StatoAvvisoEnum.md) |  | [optional] 
**azione** | [**TipoAzioneAvvisoEnum**](TipoAzioneAvvisoEnum.md) |  | [optional] 
**dati_pubblicazione_eu** | [**DatiPubblicazioneEUType**](DatiPubblicazioneEUType.md) |  | [optional] 
**dati_pubblicazione_it** | [**DatiPubblicazioneITType**](DatiPubblicazioneITType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

