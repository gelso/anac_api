# RitardoType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_termine** | **datetime** | Termine previsto per la consegna | 
**tipo_comunicazione** | [**TipologiaComunicazioneEnum**](TipologiaComunicazioneEnum.md) |  | 
**durata_sospensione** | **float** | Durata della sospensione in giorni (in caso di sospensione) | [optional] 
**motivo_sospensione** | **str** | Motivazione della sospensione/ritardo | [optional] 
**data_istanza_recesso** | **datetime** | Data di presentazione dell’istanza di recesso | 
**istanza_accolta** | **bool** | L&#x27;istanza di recesso è stata accolta? | 
**istanza_tardiva** | **bool** | Si è proceduto a consegna tardiva (in caso di ritardo) | 
**istanza_ripresa** | **bool** | Si è proceduto alla ripresa dei lavori (in caso di sospensione) | 
**istanza_riserva** | **bool** | L’appaltatore ha formulato riserve | 
**imp_spese** | **float** | Eventuale rimborso delle spese in € | 
**imp_oneri** | **float** | Eventuale compenso degli oneri derivanti dal ritardo in € | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

