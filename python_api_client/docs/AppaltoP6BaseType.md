# AppaltoP6BaseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_appalto** | **str** | Codice univoco dell&#x27;appalto. il campo viene determinato da anac e restituito nelle response. viene dunque ignorato il valore inserito nelle put/post. | [optional] 
**codice_appalto** | **str** | Identificativo univoco dell&#x27;appalto definito dalla Stazione Appaltante | 
**cig_accordo_quadro** | **str** | CIG relativo all’accordo quadro/convenzione cui si aderisce | 
**strumenti_svolgimento_procedure** | [**StrumentiSvolgimentoProcedureEnum**](StrumentiSvolgimentoProcedureEnum.md) |  | [optional] 
**id_pianificazione** | **str** | ID pianificazione | [optional] 
**termine_ridotto_avviso_preinformazione** | **bool** | E&#x27; stato utilizzato un termine ridotto con avviso di preinformazione? | [optional] 
**dati_base_procedura** | [**DatiBaseProceduraCompletoType**](DatiBaseProceduraCompletoType.md) |  | [optional] 
**dati_base_strumenti_procedura** | **AllOfAppaltoP6BaseTypeDatiBaseStrumentiProcedura** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

