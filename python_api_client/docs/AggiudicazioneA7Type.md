# AggiudicazioneA7Type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cig** | **str** | CIG affidamento incarico esterno di progettazione (in caso di progettista esterno) | 
**afferente_investimenti_pnrr** | **bool** | L’appalto o concessione è afferente gli investimenti pubblici finanziati, in tutto o in parte, con le risorse previste dal PNRR (Piano Nazionale di Ripresa e Resilienza) e/o dal PNC (Piano nazionale per gli investimenti complementari)? | 
**acquisizione_cup** | **bool** | Il contratto è finalizzato alla realizzazione di progetti d&#x27;investimento pubblico per i quali è prevista l&#x27;acquisizione del codice CUP ai sensi dell&#x27;art. 11 L. 3/2003 e ss.mm.? (E&#x27; necessario acquisire e comunicare il CUP per interventi finanziati, anche in parte, con risorse Comunitarie) (Si/No) | [optional] 
**cup_lotto** | **list[str]** | Cup associati al lotto | [optional] 
**oggetto_principale_contratto** | [**OggettoPrincipaleContrattoEnum**](OggettoPrincipaleContrattoEnum.md) |  | [optional] 
**parita_di_genere_generazionale** | [**ParitaDiGenereGenerazionaleType**](ParitaDiGenereGenerazionaleType.md) |  | [optional] 
**quadro_economico_standard** | [**QuadroEconomicoType**](QuadroEconomicoType.md) |  | [optional] 
**quadro_economico_concessioni** | [**QuadroEconomicoConcessioniType**](QuadroEconomicoConcessioniType.md) |  | [optional] 
**partecipanti** | [**list[PartecipanteADType]**](PartecipanteADType.md) |  | 
**finanziamenti** | [**list[FinanziamentoType]**](FinanziamentoType.md) | Dati relativi ai finanziamenti | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

