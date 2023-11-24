# AppaltoP4BaseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_appalto** | **str** | Codice univoco dell&#x27;appalto.il campo viene determinato da anac e restituito nelle response. viene dunque ignorato il valore inserito nelle put/post. | [optional] 
**codice_appalto** | **str** | Identificativo univoco dell&#x27;appalto definito dalla Stazione Appaltante | 
**prelazione_promotore** | **bool** | E&#x27; previsto il diritto di prelazione per il promotore? | 
**strumenti_svolgimento_procedure** | [**StrumentiSvolgimentoProcedureEnum**](StrumentiSvolgimentoProcedureEnum.md) |  | [optional] 
**id_pianificazione** | **str** | ID pianificazione | [optional] 
**termine_ridotto_avviso_preinformazione** | **bool** | E&#x27; stato utilizzato un termine ridotto con avviso di preinformazione? | [optional] 
**costituzione_societa_di_scopo** | **bool** | Indicare se è prevista la costituzione di una società di scopo | 
**dati_base** | [**DatiBaseAppaltoOptionalType**](DatiBaseAppaltoOptionalType.md) |  | [optional] 
**dati_base_procedura** | **AllOfAppaltoP4BaseTypeDatiBaseProcedura** |  | [optional] 
**dati_base_strumenti_procedura** | [**DatiBaseStrumentiProceduraAstaType**](DatiBaseStrumentiProceduraAstaType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

