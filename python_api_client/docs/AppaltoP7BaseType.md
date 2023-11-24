# AppaltoP7BaseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_appalto** | **str** | Codice univoco dell&#x27;appalto.il campo viene determinato da anac e restituito nelle response. viene dunque ignorato il valore inserito nelle put/post. | [optional] 
**codice_appalto** | **str** | Identificativo univoco dell&#x27;appalto definito dalla Stazione Appaltante | 
**id_pianificazione** | **str** | ID pianificazione | [optional] 
**termine_ridotto_avviso_preinformazione** | **bool** | E&#x27; stato utilizzato un termine ridotto con avviso di preinformazione? | [optional] 
**categorie_merceologiche** | [**list[CategorieMerceologicheEnum]**](CategorieMerceologicheEnum.md) |  | 
**motivazione_cig** | [**MotivazioneCIGEnum**](MotivazioneCIGEnum.md) |  | 
**strumenti_svolgimento_procedure** | [**StrumentiSvolgimentoProcedureEnum**](StrumentiSvolgimentoProcedureEnum.md) |  | 
**motivo_urgenza** | [**MotivoUrgenzaEnum**](MotivoUrgenzaEnum.md) |  | [optional] 
**link_documenti** | **str** | Link ai documenti relativi all’affidamento diretto in somma urgenza e protezione civile (co 10, art 140 nuovo codice) | [optional] 
**dati_base** | **AllOfAppaltoP7BaseTypeDatiBase** |  | [optional] 
**dati_base_procedura** | **AllOfAppaltoP7BaseTypeDatiBaseProcedura** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

