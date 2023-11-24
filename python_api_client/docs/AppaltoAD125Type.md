# AppaltoAD125Type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_appalto** | **str** | Codice univoco dell&#x27;appalto.il campo viene determinato da anac e restituito nelle response. viene dunque ignorato il valore inserito nelle put/post. | [optional] 
**codice_appalto** | **str** | Identificativo univoco dell&#x27;appalto definito dalla Stazione Appaltante | 
**motivo_urgenza** | [**MotivoUrgenzaEnum**](MotivoUrgenzaEnum.md) |  | 
**link_documenti** | **str** | Link ai documenti relativi all’affidamento diretto in somma urgenza e protezione civile (co 10, art 140 nuovo codice) | [optional] 
**relazione_unica_sulle_procedure** | **bool** | Il sottoscritto dichiara che questa SA ha redatto la Relazione Unica sulle Procedure | 
**opere_urbanizzazione_scomputo** | **bool** | Opere di urbanizzazione a scomputo | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

