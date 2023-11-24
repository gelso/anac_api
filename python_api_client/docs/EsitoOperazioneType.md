# EsitoOperazioneType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_appalto** | **str** | identificativo univoco dell&#x27;Appalto definito da ANAC. Restituito dall&#x27;operazione di creazione Appalto. (A UUID specified by RFC4122) | [optional] 
**id_pianificazione** | **str** | identificativo univoco della Pianificazione definito da ANAC. Restituito dall&#x27;operazione di creazione Piano. (A UUID specified by RFC4122) | [optional] 
**id_scheda** | **object** | Identificativo univoco della Scheda definito da ANAC. (A UUID specified by RFC4122) | [optional] 
**id_nuova_scheda** | **object** | Identificativo univoco della nuova Scheda definito da ANAC a seguito delle operazioni di modifica-avviso e rettifica-avviso. (A UUID specified by RFC4122) | [optional] 
**id_avviso** | **str** | identificativo univoco dell&#x27;Avviso generato da ANAC, qualora il tipo di scheda lo consente, durante l&#x27;invocazione delle operazioni dispositive conferma-piano, conferma-appalto, conferma-scheda. | [optional] 
**id_nuovo_avviso** | **str** | identificativo univoco del nuovo Avviso generato da ANAC a seguito delle operazioni di modifica-avviso e rettifica-avviso. | [optional] 
**id_contratto** | **str** | identificativo univoco del Contratto generato da ANAC, qualora il tipo di scheda lo consente, durante l&#x27;invocazione dell&#x27; operazione dispositiva conferma-scheda. | [optional] 
**esito** | [**EsitoEnum**](EsitoEnum.md) |  | [optional] 
**tipo_operazione** | [**TipoOperazioneEnum**](TipoOperazioneEnum.md) |  | [optional] 
**dettaglio** | [**DettaglioEsitoOperazioneEnum**](DettaglioEsitoOperazioneEnum.md) |  | [optional] 
**data_controllo** | **datetime** | data in cui è stato effettuato il controllo dell&#x27;esito dell&#x27;operazione (A date-time specified by ISO 8601 as profiled by RFC 3339) | [optional] 
**errori** | [**list[ErroriEnum]**](ErroriEnum.md) | elenco degli errori | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

