# LottoP23Type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lot_identifier** | **str** | Id univoco del lotto generato dalla stazione appaltante - corrisponde al campo bt-137 - Purpose Lot Identifier del TED | 
**cod_istat** | [**CodIstatEnum**](CodIstatEnum.md) |  | 
**lavoro_o_acquisto_previsto_in_programmazione** | **bool** | Il lavoro o l’acquisto di bene o servizio è stato previsto all’interno della programmazione | [optional] 
**cui** | **str** | CUI programma triennale lavori pubblici o programma biennale forniture e servizi | [optional] 
**afferente_investimenti_pnrr** | **bool** | L’appalto o concessione è afferente gli investimenti pubblici finanziati, in tutto o in parte, con le risorse previste dal PNRR (Piano Nazionale di Ripresa e Resilienza) e/o dal PNC (Piano nazionale per gli investimenti complementari)? | 
**acquisizione_cup** | **bool** | Il contratto è finalizzato alla realizzazione di progetti d&#x27;investimento pubblico per i quali è prevista l&#x27;acquisizione del codice CUP ai sensi dell&#x27;art. 11 L. 3/2003 e ss.mm.? (E&#x27; necessario acquisire e comunicare il CUP per interventi finanziati, anche in parte, con risorse Comunitarie) (Si/No) | 
**cup_lotto** | **list[str]** | Cup associati al lotto | [optional] 
**motivo_esclusione_ordinario_speciale** | [**MotivoEsclusioneOrdinarioSpecialeEnum**](MotivoEsclusioneOrdinarioSpecialeEnum.md) |  | [optional] 
**finanziamenti** | [**list[FinanziamentoType]**](FinanziamentoType.md) | Dati relativi ai finanziamenti | [optional] 
**quadro_economico_concorsi_progettazione** | [**QuadroEconomicoConcorsiProgettazioneType**](QuadroEconomicoConcorsiProgettazioneType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

