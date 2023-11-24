# LottoP35Type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**afferente_investimenti_pnrr** | **bool** | L’appalto o concessione è afferente gli investimenti pubblici finanziati, in tutto o in parte, con le risorse previste dal PNRR (Piano Nazionale di Ripresa e Resilienza) e/o dal PNC (Piano nazionale per gli investimenti complementari)? | 
**categoria** | [**CategoriaEnum**](CategoriaEnum.md) |  | 
**servizio_pubblico_locale** | **bool** | Flag servizio pubblico locale | 
**ripetizioni_e_consegne_complementari** | **bool** | L’appalto prevede ripetizioni di servizi/forniture/lavori analoghi e consegne complementari? | 
**strumenti_elettronici_specifici** | **bool** | Uso e metodi e strumenti elettronici specifici, quali quelli di modellazione per l’edilizia e le infrastrutture, nelle fasi di progettazione, costruzione e gestione delle opere e relative verifiche | [optional] 
**condizioni_negoziata** | [**list[CondizioniNegoziataEnum]**](CondizioniNegoziataEnum.md) |  | [optional] 
**contratti_disposizioni_particolari** | [**ContrattiDisposizioniParticolariEnum**](ContrattiDisposizioniParticolariEnum.md) |  | 
**lavoro_o_acquisto_previsto_in_programmazione** | **bool** | Il lavoro o l’acquisto di bene o servizio è stato previsto all’interno della programmazione | 
**cui** | **str** | CUI programma triennale lavori pubblici o programma biennale forniture e servizi | [optional] 
**tipo_realizzazione** | [**TipoRealizzazioneContrattoEnum**](TipoRealizzazioneContrattoEnum.md) |  | [optional] 
**ipotesi_collegamento** | [**IpotesiCollegamentoType**](IpotesiCollegamentoType.md) |  | [optional] 
**opzioni_rinnovi** | **bool** | L’appalto prevede opzioni o rinnovi? | 
**quadro_economico_standard** | [**QuadroEconomicoType**](QuadroEconomicoType.md) |  | [optional] 
**dati_base** | **AllOfLottoP35TypeDatiBase** |  | [optional] 
**dati_base_cpv** | [**DatiBaseCPVType**](DatiBaseCPVType.md) |  | [optional] 
**dati_base_contratto** | [**DatiBaseContrattoType**](DatiBaseContrattoType.md) |  | [optional] 
**dati_base_aggiudicazione** | **AllOfLottoP35TypeDatiBaseAggiudicazione** |  | [optional] 
**dati_base_termini_invio** | [**DatiTerminiInvioType**](DatiTerminiInvioType.md) |  | [optional] 
**dati_base_accessibilita** | [**DatiBaseAccessibilitaType**](DatiBaseAccessibilitaType.md) |  | [optional] 
**dati_base_documenti** | [**DatiBaseDocumentiOptionalType**](DatiBaseDocumentiOptionalType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

