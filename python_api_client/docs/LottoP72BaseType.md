# LottoP72BaseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lot_identifier** | **str** | Id univoco del lotto generato dalla stazione appaltante | 
**categorie_merceologiche** | [**list[CategorieMerceologicheEnum]**](CategorieMerceologicheEnum.md) |  | 
**sa_non_soggetta_obblighi24_dicembre2015** | **bool** | Che questa stazione appaltante non è soggetta agli obblighi del DPCM 24 dicembre 2015 e ss.mm.ii. | 
**iniziative_non_soddisfacenti** | **bool** | Che nessuna delle iniziative disponibili presso i soggetti aggregatori di riferimento ha caratteristiche in grado di soddisfare i fabbisogni di questa stazione appaltante | 
**strumenti_elettronici_specifici** | **bool** | Uso e metodi e strumenti elettronici specifici, quali quelli di modellazione per l’edilizia e le infrastrutture, nelle fasi di progettazione, costruzione e gestione delle opere e relative verifiche | [optional] 
**motivo_esclusione_ordinario_speciale** | [**MotivoEsclusioneOrdinarioSpecialeEnum**](MotivoEsclusioneOrdinarioSpecialeEnum.md) |  | [optional] 
**motivo_esclusione_concessione** | [**MotivoEsclusioneConcessioneEnum**](MotivoEsclusioneConcessioneEnum.md) |  | [optional] 
**condizioni_negoziata** | [**list[CondizioniNegoziataEnum]**](CondizioniNegoziataEnum.md) |  | 
**contratti_disposizioni_particolari** | [**ContrattiDisposizioniParticolariEnum**](ContrattiDisposizioniParticolariEnum.md) |  | [optional] 
**cod_istat** | [**CodIstatEnum**](CodIstatEnum.md) |  | 
**servizio_pubblico_locale** | **bool** | Flag servizio pubblico locale | 
**lavoro_o_acquisto_previsto_in_programmazione** | **bool** | Il lavoro o l’acquisto di bene o servizio è stato previsto all’interno della programmazione | 
**cui** | **str** | CUI programma triennale lavori pubblici o programma biennale forniture e servizi | [optional] 
**ripetizioni_e_consegne_complementari** | **bool** | L’appalto prevede ripetizioni di servizi/forniture/lavori analoghi e consegne complementari? | 
**ipotesi_collegamento** | [**IpotesiCollegamentoType**](IpotesiCollegamentoType.md) |  | 
**opzioni_rinnovi** | **bool** | L’appalto prevede opzioni/rinnovi? | 
**afferente_investimenti_pnrr** | **bool** | L’appalto o concessione è afferente gli investimenti pubblici finanziati, in tutto o in parte, con le risorse previste dal PNRR (Piano Nazionale di Ripresa e Resilienza) e/o dal PNC (Piano nazionale per gli investimenti complementari)? | 
**acquisizione_cup** | **bool** | Il contratto è finalizzato alla realizzazione di progetti d&#x27;investimento pubblico per i quali è prevista l&#x27;acquisizione del codice CUP ai sensi dell&#x27;art. 11 L. 3/2003 e ss.mm.? (E&#x27; necessario acquisire e comunicare il CUP per interventi finanziati, anche in parte, con risorse Comunitarie) (Si/No) | [optional] 
**cup_lotto** | **list[str]** | Cup associati al lotto | [optional] 
**parita_di_genere_generazionale** | [**ParitaDiGenereGenerazionaleType**](ParitaDiGenereGenerazionaleType.md) |  | [optional] 
**ccnl** | **str** | indicare il codice CNEL o non applicabile | 
**modalita_acquisizione** | [**ModalitaAcquisizioneEnum**](ModalitaAcquisizioneEnum.md) |  | [optional] 
**tipologia_lavoro** | [**list[TipologiaLavoroEnum]**](TipologiaLavoroEnum.md) |  | [optional] 
**categoria** | [**CategoriaEnum**](CategoriaEnum.md) |  | 
**prestazioni_comprese** | [**PrestazioniEnum**](PrestazioniEnum.md) |  | 
**finanziamenti** | [**list[FinanziamentoType]**](FinanziamentoType.md) | Dati relativi ai finanziamenti | 
**tipo_realizzazione** | [**TipoRealizzazioneContrattoEnum**](TipoRealizzazioneContrattoEnum.md) |  | 
**dati_base** | **AllOfLottoP72BaseTypeDatiBase** |  | [optional] 
**dati_base_cpv** | **AllOfLottoP72BaseTypeDatiBaseCpv** |  | [optional] 
**dati_base_contratto** | **AllOfLottoP72BaseTypeDatiBaseContratto** |  | [optional] 
**dati_base_aggiudicazione** | **AllOfLottoP72BaseTypeDatiBaseAggiudicazione** |  | [optional] 
**dati_base_aggiuntivi** | [**DatiBaseAggiuntiviType**](DatiBaseAggiuntiviType.md) |  | [optional] 
**dati_base_accessibilita** | [**DatiBaseAccessibilitaType**](DatiBaseAccessibilitaType.md) |  | [optional] 
**dati_base_comunicazione** | [**DatiBaseComunicazioneType**](DatiBaseComunicazioneType.md) |  | [optional] 
**dati_base_documenti** | [**DatiBaseDocumentiType**](DatiBaseDocumentiType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

