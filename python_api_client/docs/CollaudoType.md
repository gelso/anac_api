# CollaudoType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_collaudo** | **datetime** | Data del collaudo statico (ove ricorra) | [optional] 
**data_certificato** | **datetime** | Data del certificato di regolare esecuzione | [optional] 
**modo_collaudo** | [**ModoCollaudoEnum**](ModoCollaudoEnum.md) |  | [optional] 
**data_nomina** | **datetime** | Data nomina collaudatore/Commissione | [optional] 
**data_inizio** | **datetime** | Data inizio operazioni di collaudo | [optional] 
**data_redazione_certificato** | **datetime** | Data redazione certificato di collaudo/ verifica di conformità | [optional] 
**data_delibera_ammissibilita** | **datetime** | Data delibera di ammissibilità del collaudo (ove prevista) | [optional] 
**esito** | **str** | Esito del collaudo/ verifica di conformità | 
**quadro_economico_standard** | [**QuadroEconomicoType**](QuadroEconomicoType.md) |  | [optional] 
**quadro_economico_concessioni** | [**QuadroEconomicoConcessioniType**](QuadroEconomicoConcessioniType.md) |  | [optional] 
**numero_totale_riserve** | **float** | Numero totale riserve definite con accordo bonario | [optional] 
**oneri** | **float** | Oneri complessivi derivanti | [optional] 
**modalita_definizione** | [**list[DefinizioneType]**](DefinizioneType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

