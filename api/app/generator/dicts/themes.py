# Specialized Domain Lexicons for Prolixo: Ecology, Law, Medicine, Mining, Politics, Technology

THEME_DICTS = {
    "pt": {
        "business": {
            "n_ms": [
                "planejamento estratégico", "plano de negócios", "fluxo de caixa", "retorno sobre o investimento",
                "posicionamento de mercado", "conselho de administração", "equilíbrio financeiro", "acordo comercial",
                "orçamento operacional", "valuation projetado", "capital de giro", "valor de mercado",
                "crescimento sustentável", "comitê executivo", "desempenho corporativo", "balanço patrimonial",
                "custo de aquisição", "lucro operacional", "passivo contingente", "patrimônio líquido",
                "fundo garantidor", "acordo de sócios", "ebitda ajustado", "plano de contingência",
                "capex operacional", "opex projetado", "modelo de negócios"
            ],
            "n_fs": [
                "estratégia corporativa", "gestão de riscos", "margem de lucro", "governança corporativa",
                "vantagem competitiva", "sinergia operacional", "análise de viabilidade", "reestruturação societária",
                "eficiência operacional", "fusão empresarial", "tomada de decisão", "visão estratégica",
                "rentabilidade financeira", "auditoria contábil", "due diligence", "alavancagem financeira",
                "avaliação patrimonial", "governança ESG", "liquidez corrente", "gestão de ativos",
                "precificação estratégica", "relação com investidores", "análise de sensibilidade"
            ],
            "n_mp": [
                "indicadores financeiros", "principais stakeholders", "ativos estratégicos", "resultados operacionais",
                "planos de contingência", "vetores de crescimento", "mercados emergentes", "fundos de investimento",
                "modelos de receita", "custos operacionais", "aportes de capital", "títulos de crédito",
                "relatórios de auditoria", "dividendos distribuídos", "investimentos estratégicos", "índices de liquidez"
            ],
            "n_fp": [
                "diretrizes estratégicas", "oportunidades de mercado", "metas corporativas", "projeções financeiras",
                "alianças comerciais", "estruturas de capital", "vantagens competitivas", "operações de crédito",
                "reservas de contingência", "obrigações tributárias", "demonstrações contábeis", "previsões orçamentárias",
                "sinergias corporativas", "linhas de financiamento"
            ],
            "adj_ms": [" estratégico", " corporativo", " financeiro", " rentável", " competitivo", " operacional", " escalável", " lucrativo", " comercial", " fiduciário", " consolidado", " superavitário", " auditável"],
            "adj_fs": [" estratégica", " corporativa", " financeira", " rentável", " competitiva", " operacional", " escalável", " lucrativa", " comercial", " fiduciária", " consolidada", " superavitária", " auditável"],
            "adj_mp": [" estratégicos", " corporativos", " financeiros", " rentáveis", " competitivos", " operacionais", " escaláveis", " lucrativos", " fiduciários", " consolidados", " superavitários"],
            "adj_fp": [" estratégicas", " corporativas", " financeiras", " rentáveis", " competitivas", " operacionais", " escaláveis", " lucrativas", " fiduciárias", " consolidadas", " superavitárias"],
            "v_trans_s": ["maximiza ", "alavanca ", "otimiza ", "consolida ", "potencializa ", "viabiliza ", "estrutura ", "impulsiona ", "mitiga ", "incorpora ", "implementa ", "aloca ", "equaliza ", "audita ", "capitaliza ", "diversifica "],
            "v_trans_p": ["maximizam ", "alavancam ", "otimizam ", "consolidam ", "potencializam ", "viabilizam ", "estruturam ", "impulsionam ", "mitigam ", "incorporam ", "implementam ", "alocam ", "equalizam ", "auditam ", "capitalizam ", "diversificam "],
            "v_intrans_s": ["maximiza o retorno sobre o investimento", "assegura a solidez financeira", "fortalece o posicionamento de mercado", "gera valor para os acionistas", "otimiza a rentabilidade operacional", "impulsiona a eficiência dos negócios", "maximiza a geração de caixa", "mitiga a exposição a riscos de mercado", "sustenta o crescimento de longo prazo"],
            "v_intrans_p": ["maximizam o retorno sobre o investimento", "asseguram a solidez financeira", "fortalecem o posicionamento de mercado", "geram valor para os acionistas", "otimizam a rentabilidade operacional", "impulsionam a eficiência dos negócios", "maximizam a geração de caixa", "mitigam a exposição a riscos de mercado", "sustentam o crescimento de longo prazo"],
            "circ": ["No atual cenário corporativo", "Diante das novas exigências do mercado", "Com o aumento da competitividade global", "Sob a perspectiva da governança corporativa", "Em virtude dos novos desafios mercadológicos", "Sem perder de vista o alinhamento de curto prazo", "Com foco na entrega de resultados", "Diante dos crescentes padrões de conformidade", "Com foco na excelência operacional", "Ao avaliar o ROI das iniciativas", "A partir da validação dos dados financeiros", "Sob o rigor da auditoria independente", "Diante da volatilidade dos mercados de capitais", "Com a consolidação do balanço corporativo"]
        },
        "ecology": {
            "n_ms": [
                "crédito de carbono", "bioma frágil", "ecossistema sustentável", "impacto ecológico",
                "manejo florestal", "reflorestamento consciente", "desenvolvimento sustentável", "inventário de emissões",
                "recurso hídrico", "balanço energético", "topo da cadeia trófica", "habitat natural",
                "atropelamento de fauna", "uso do solo", "mosaico de paisagens", "uso e cobertura da terra",
                "bem-estar animal", "corredor ecológico", "serviço ecossistêmico", "capital natural",
                "assoreamento de mananciais", "ciclo biogeoquímico", "manejo de bacias", "reflorestamento nativo",
                "plano de conservação", "estoque de biomassa", "patrimônio genético"
            ],
            "n_fs": [
                "transição energética", "pegada de carbono", "biodiversidade preservada", "conservação ambiental",
                "economia circular", "neutralidade climática", "gestão de resíduos", "sustentabilidade ecológica",
                "matriz renovável", "avaliação de impacto ambiental", "reserva extrativista", "conectividade ecológica",
                "fragmentação de habitats", "fragmentação florestal", "conectividade paisagística", "reserva legal",
                "área de preservação permanente", "ação antrópica", "avaliação de ciclo de vida",
                "recuperação de áreas degradadas", "biomassa residual", "resiliência climática",
                "gestão de recursos hídricos", "outorga de água", "compensação ambiental", "proteção da fauna"
            ],
            "n_mp": [
                "recursos naturais", "ecossistemas locais", "indicadores ambientais", "créditos de carbono",
                "padrões de sustentabilidade", "habitats protegidos", "resíduos sólidos", "serviços ecossistêmicos",
                "biomas ameaçados", "atropelamentos de fauna", "mosaicos de paisagens", "corredores ecológicos",
                "mananciais protegidos", "indicadores de sustentabilidade", "recursos hídricos", "estoques de carbono",
                "serviços ambientais", "processos ecológicos"
            ],
            "n_fp": [
                "energias renováveis", "metas de descarbonização", "políticas ambientais", "áreas de preservação",
                "práticas sustentáveis", "fontes de energia limpa", "emissões de gases de efeito estufa",
                "medidas mitigadoras", "ações de bem-estar animal", "unidades de conservação", "bacias hidrográficas",
                "compensações ambientais", "espécies nativas", "áreas de recarga hídrica", "florestas nativas"
            ],
            "adj_ms": [" sustentável", " ecológico", " de baixo carbono", " renovável", " de impacto neutro", " biodegradável", " ecossistêmico", " descarbonizado", " bioclimático", " restaurativo", " regenerativo", " hidrológico", " conservacionista"],
            "adj_fs": [" sustentável", " ecológica", " de baixo carbono", " renovável", " de impacto neutro", " biodegradável", " ecossistêmica", " descarbonizada", " bioclimática", " restaurativa", " regenerativa", " hidrológica", " conservacionista"],
            "adj_mp": [" sustentáveis", " ecológicos", " de baixo carbono", " renováveis", " de impacto neutro", " biodegradáveis", " ecossistêmicos", " bioclimáticos", " restaurativos", " regenerativos", " hidrológicos"],
            "adj_fp": [" sustentáveis", " ecológicas", " de baixo carbono", " renováveis", " de impacto neutro", " biodegradáveis", " ecossistêmicas", " bioclimáticas", " restaurativas", " regenerativas", " hidrológicas"],
            "v_trans_s": ["preserva ", "mitiga ", "regenera ", "descarboniza ", "conserva ", "restaura ", "reabilita ", "despolui ", "protege ", "incorpora ", "implementa ", "refloresta ", "revegeta ", "equilibra ", "neutraliza "],
            "v_trans_p": ["preservam ", "mitigam ", "regeneram ", "descarbonizam ", "conservam ", "restauram ", "reabilitam ", "despoluem ", "protegem ", "incorporam ", "implementam ", "reflorestam ", "revegetam ", "equilibram ", "neutralizam "],
            "v_intrans_s": ["promove a neutralidade climática", "reduz o impacto ambiental", "fortalece a biodiversidade", "assegura o equilíbrio ecológico", "regenera os ecossistemas nativos", "reduz o atropelamento de fauna", "promove o bem-estar animal", "assegura a conectividade ecológica", "mitiga a fragmentação de habitats", "promove o equilíbrio bioclimático", "restaura a integridade da paisagem", "assegura a preservação dos mananciais", "fortalece a resiliência ecológica"],
            "v_intrans_p": ["promovem a neutralidade climática", "reduzem o impacto ambiental", "fortalecem a biodiversidade", "asseguram o equilíbrio ecológico", "regeneram os ecossistemas nativos", "reduzem o atropelamento de fauna", "promovem o bem-estar animal", "asseguram a conectividade ecológica", "mitigam a fragmentação de habitats", "promovem o equilíbrio bioclimático", "restauram a integridade da paisagem", "asseguram a preservação dos mananciais", "fortalecem a resiliência ecológica"],
            "circ": ["Diante das mudanças climáticas globais", "No contexto da conservação ambiental", "Com o avanço da transição ecológica", "Sob a perspectiva da preservação dos biomas", "A partir da avaliação de impacto ambiental", "Com foco na regeneração dos ecossistemas", "Em virtude dos compromissos de sustentabilidade", "Diante da perda de biodiversidade", "Com o monitoramento constante dos habitats", "A partir de metas de descarbonização", "Em consonância com as metas climáticas", "No âmbito da restauração florestal", "Sob a perspectiva do capital natural"]
        },
        "law": {
            "n_ms": [
                "devido processo legal", "ordenamento jurídico", "litígio judicial", "amparo legal",
                "parecer jurídico", "vício formal", "recurso cabível", "acórdão proferido",
                "provimento jurisdicional", "agravo de instrumento", "juízo de admissibilidade", "trânsito em julgado",
                "agravo regimental", "embargos infringentes", "efeito suspensivo", "inadimplemento contratual",
                "dano moral", "nexo causal", "mandado de segurança", "recurso especial", "recurso extraordinário",
                "princípio da ampla defesa", "contencioso judicial", "despacho saneador", "negócio jurídico"
            ],
            "n_fs": [
                "jurisprudência consolidada", "segurança jurídica", "norma constitucional", "instrução processual",
                "súmula vinculante", "presunção de inocência", "cláusula pétrea", "tutela de urgência",
                "medida cautelar", "petição inicial", "coisa julgada", "tutela provisória",
                "prescrição intercorrente", "sucumbência recursal", "repercussão geral", "inconstitucionalidade material",
                "competência jurisdicional", "responsabilidade civil", "citação válida", "cláusula compromissória",
                "ação rescisória", "pretensão executória", "arguição de nulidade"
            ],
            "n_mp": [
                "direitos fundamentais", "prazos processuais", "precedentes judiciais", "autos do processo",
                "dispositivos legais", "recursos tempestivos", "honorários advocatícios", "atos ordinatórios",
                "embargos de declaração", "efeitos infringentes", "fundamentos jurídicos", "recursos adesivos",
                "honorários sucumbenciais", "meios de prova", "tribunais superiores"
            ],
            "n_fp": [
                "prerrogativas advocatícias", "garantias constitucionais", "normas jurídicas", "decisões interlocutórias",
                "medidas cautelares", "razões recursais", "petições intermediárias", "tutelas de urgência",
                "obrigações contratuais", "garantias processuais", "presunções legais", "ações declaratórias",
                "súmulas persuasivas"
            ],
            "adj_ms": [" jurídico", " constitucional", " processual", " vinculante", " tempestivo", " incontestável", " infraconstitucional", " jurisprudencial", " líqüido e certo", " vinculatório", " rescisório", " irrecorrível", " subsidiário", " cogente"],
            "adj_fs": [" jurídica", " constitucional", " processual", " vinculante", " tempestiva", " incontestável", " infraconstitucional", " jurisprudencial", " líqüida e certa", " vinculatória", " rescisória", " irrecorrível", " subsidiária", " cogente"],
            "adj_mp": [" jurídicos", " constitucionais", " processuais", " vinculantes", " tempestivos", " incontestáveis", " infraconstitucionais", " vinculatórios", " rescisórios", " irrecorríveis", " subsidiários", " cogentes"],
            "adj_fp": [" jurídicas", " constitucionais", " processuais", " vinculantes", " tempestivas", " incontestáveis", " infraconstitucionais", " vinculatórias", " rescisórias", " irrecorríveis", " subsidiárias", " cogentes"],
            "v_trans_s": ["fundamenta ", "ratifica ", "pacifica ", "prescreve ", "regulamenta ", "assenta ", "impulsiona ", "defere ", "incorpora ", "implementa ", "reforma ", "homologa ", "invalida ", "aprecia ", "julga ", "adjudica "],
            "v_trans_p": ["fundamentam ", "ratificam ", "pacificam ", "prescrevem ", "regulamentam ", "assentam ", "impulsionam ", "deferem ", "incorporam ", "implementam ", "reformam ", "homologam ", "invalidam ", "apreciam ", "julgam ", "adjudicam "],
            "v_intrans_s": ["garante a segurança jurídica", "resguarda o devido processo legal", "respeita o texto constitucional", "consolida o entendimento jurisprudencial", "viabiliza a ampla defesa", "assegura o contraditório e a ampla defesa", "consolida a segurança jurídica", "vincula os órgãos julgadores", "afasta a pretensão punitiva"],
            "v_intrans_p": ["garantem a segurança jurídica", "resguardam o devido processo legal", "respeitam o texto constitucional", "consolidam o entendimento jurisprudencial", "viabilizam a ampla defesa", "asseguram o contraditório e a ampla defesa", "consolidam a segurança jurídica", "vinculam os órgãos julgadores", "afastam a pretensão punitiva"],
            "circ": ["À luz do ordenamento jurídico vigente", "Sob a ótica constitucional", "Diante da jurisprudência consolidada", "Em observância ao devido processo legal", "No âmbito da instrução processual", "Com base nos preceitos fundamentais", "Diante das garantias constitucionais", "Em sede de juízo de admissibilidade", "Nos termos da legislação aplicável", "Consoante o entendimento dos tribunais", "Sob o crivo do contraditório", "Em sede de juízo de retratação", "Nos moldes do regimento interno"]
        },
        "medicine": {
            "n_ms": [
                "diagnóstico clínico", "protocolo terapêutico", "ensaio clínico", "marcador biológico",
                "quadro sintomático", "tratamento profilático", "exame laboratorial", "prognóstico médico",
                "agente patogênico", "transplante autólogo", "plano de cuidados", "estudo duplo-cego",
                "marcador sorológico", "fator de necrose tumoral", "quadro de sepse", "antibiograma bacteriano",
                "exame histopatológico", "perfil farmacocinético", "plano terapêutico", "choque séptico",
                "cateterismo cardíaco", "desfecho clínico"
            ],
            "n_fs": [
                "terapia profilática", "farmacovigilância", "conduta médica", "anamnese detalhada",
                "imunidade celular", "fisiopatologia", "resposta imune", "eficácia terapêutica",
                "propedêutica médica", "remissão completa", "dose terapêutica", "comorbidade associada",
                "terapia adjuvante", "farmacocinética clínica", "incidência epidemiológica", "resistência microbiana",
                "intervenção endovascular", "ventilação mecânica", "síndrome metabólica", "biópsia tecidual",
                "imunoterapia celular", "estratificação de risco"
            ],
            "n_mp": [
                "ensaios clínicos", "marcadores biológicos", "ensaios randomizados", "sintomas característicos",
                "agentes patogênicos", "parâmetros fisiológicos", "achados radiológicos", "tratamentos paliativos",
                "marcadores sorológicos", "estudos duplo-cegos", "ensaios clínicos multicêntricos", "fatores de risco",
                "parâmetros hemodinâmicos", "achados histológicos", "protocolos clínicos"
            ],
            "n_fp": [
                "respostas imunológicas", "terapias inovadoras", "intervenções cirúrgicas", "evidências científicas",
                "medidas profiláticas", "reações adversas", "diretrizes clínicas", "comorbidades clínicas",
                "terapias adjuvantes", "intervenções endovasculares", "amostras biológicas", "síndromes inflamatórias",
                "taxas de remissão"
            ],
            "adj_ms": [" terapêutico", " clínico", " profilático", " fisiológico", " patogênico", " multidisciplinar", " assintomático", " etiológico", " farmacológico", " epidemiológico", " imunológico", " adjuvante", " histopatológico", " patológico", " microbiano"],
            "adj_fs": [" terapêutica", " clínica", " profilática", " fisiológica", " patogênica", " multidisciplinar", " assintomática", " etiológica", " farmacológica", " epidemiológica", " imunológica", " adjuvante", " histopatológica", " patológica", " microbiana"],
            "adj_mp": [" terapêuticos", " clínicos", " profiláticos", " fisiológicos", " patogênicos", " multidisciplinares", " assintomáticos", " epidemiológicos", " imunológicos", " adjuvantes", " histopatológicos", " patológicos", " microbianos"],
            "adj_fp": [" terapêuticas", " clínicas", " profiláticas", " fisiológicas", " patogênicas", " multidisciplinares", " assintomáticas", " epidemiológicas", " imunológicas", " adjuvantes", " histopatológicas", " patológicas", " microbianas"],
            "v_trans_s": ["diagnostica ", "sintetiza ", "atenua ", "reabilita ", "prescreve ", "estabiliza ", "modula ", "inibe ", "combate ", "incorpora ", "implementa ", "induz ", "bloqueia ", "sedimenta ", "erradica "],
            "v_trans_p": ["diagnosticam ", "sintetizam ", "atenuam ", "rehabilitam ", "prescrevem ", "estabilizam ", "modulam ", "inibem ", "combatem ", "incorporam ", "implementam ", "induzem ", "bloqueiam ", "sedimentam ", "erradicam "],
            "v_intrans_s": ["potencializa a resposta imune", "garante a eficácia terapêutica", "combate a progressão da patologia", "assegura a recuperação clínica", "reduz a morbidade infantil", "reduz a morbidade clínica", "estabiliza os parâmetros vitais", "mitiga a resposta inflamatória", "restabelece a homeostase orgânica"],
            "v_intrans_p": ["potencializam a resposta imune", "garantem a eficácia terapêutica", "combatem a progressão da patologia", "asseguram a recuperação clínica", "reduzem a morbidade infantil", "reduzem a morbidade clínica", "estabilizam os parâmetros vitais", "mitigam a resposta inflamatória", "restabelecem a homeostase orgânica"],
            "circ": ["No contexto da prática clínica baseada em evidências", "Diante do quadro clínico apresentado", "Com base nos ensaios randomizados", "Sob a ótica da farmacovigilância", "A partir do diagnóstico precoce", "Com o avanço das terapias inovadoras", "Em observância aos protocolos terapêuticos", "Diante da resposta imune observada", "No acompanhamento do prognóstico do paciente", "Com foco na eficácia terapêutica", "Durante a monitorização hemodinâmica contínua", "Sob estrito controle farmacoterapêutico", "Após a estratificação de risco clínico"]
        },
        "mining": {
            "n_ms": [
                "beneficiamento de minério", "teor de jazida", "recuo geológico", "plano de lavra",
                "mapeamento geotécnico", "escoamento logístico", "processamento mineral", "depósito sedimentar",
                "teor de corte", "duto de rejeitos", "aluguel de equipamentos", "dique", "dique de contenção",
                "estudo de estabilidade da cava", "engenheiro de registro", "estudo de ruptura hipotética",
                "estudo de impacto ambiental", "descomissionamento de barragem", "talude de cava",
                "alteamento a montante", "alteamento a jusante", "maciço rochoso",
                "capeamento estéril", "empilhamento a seco", "piezômetro de corda vibrante", "radar interferométrico",
                "duto minerário", "ensaio triaxial", "aproveitamento mineral"
            ],
            "n_fs": [
                "lavra subterrânea", "barragem de rejeitos", "prospecção geológica", "lavra a céu aberto",
                "exploração mineral", "geotecnia operacional", "jazida lavrável", "recuperação de mina",
                "galeria de extração", "sondagem rotativa", "mineração responsável", "pilha de estéril",
                "cava", "zona de autossalvamento", "drenagem ácida de mina", "piezometria automatizada",
                "recuperação metalúrgica", "análise de estabilidade de taludes", "frente de lavra",
                "jazida aluvionar", "bacia de sedimentação", "bancada de lavra", "estabilidade geotécnica",
                "sondagem a percussão", "segurança de barragens", "rocha encaixante"
            ],
            "n_mp": [
                "rejeitos minerais", "teores de corte", "parâmetros geotécnicos", "corpos mineralizados",
                "recursos lavráveis", "métodos de extração", "concentrados minerais", "testes hidrogeológicos",
                "protocolos", "protocolos operacionais", "protocolos ambientais", "diques de segurança",
                "engenheiros de registro", "estudos de ruptura hipotética", "estudos de impacto ambiental",
                "taludes de cava", "maciços rochosos", "piezômetros de corda vibrante", "ensaios geomecânicos",
                "rejeitos filtrados"
            ],
            "n_fp": [
                "barragens de contenção", "jazidas minerais", "operações de lavra", "reservas provadas",
                "estruturas geotécnicas", "rochas hospedeiras", "escavações mecânicas", "pilhas de estéril",
                "cavas de lavra", "zonas de autossalvamento", "frentes de lavra", "bancadas de extração",
                "bacias de sedimentação", "pilhas de rejeito desaguado", "estruturas de empilhamento",
                "análises geomecânicas"
            ],
            "adj_ms": [" mineral", " geotécnico", " geológico", " extrativo", " de alta qualidade", " lavrável", " hidrogeológico", " sedimentar", " geomecânico", " aluvionar", " piezométrico", " desaguado", " metalúrgico", " estratificado"],
            "adj_fs": [" mineral", " geotécnica", " geológica", " extrativa", " de alta qualidade", " lavrável", " hidrogeológica", " sedimentar", " geomecânica", " aluvionar", " piezométrica", " desaguada", " metalúrgica", " estratificada"],
            "adj_mp": [" minerais", " geotécnicos", " geológicos", " extrativos", " lavráveis", " hidrogeológicos", " geomecânicos", " aluvionares", " piezométricos", " desaguados", " metalúrgicos", " estratificados"],
            "adj_fp": [" minerais", " geotécnicas", " geológicas", " extrativas", " lavráveis", " hidrogeológicas", " geomecânicas", " aluvionares", " piezométricas", " desaguadas", " metalúrgicas", " estratificadas"],
            "v_trans_s": ["extrai ", "beneficia ", "mapeia ", "processa ", "estabiliza ", "otimiza ", "perfura ", "escava ", "amostra ", "incorpora ", "implementa ", "alteia ", "desagua ", "consolida ", "amortece ", "recircula "],
            "v_trans_p": ["extraem ", "beneficiam ", "mapeiam ", "processam ", "estabilizam ", "otimizam ", "perfuram ", "escavam ", "amostram ", "incorporam ", "implementam ", "alteiam ", "desaguam ", "consolidam ", "amortecem ", "recirculam "],
            "v_intrans_s": ["aumenta a recuperação metalúrgica", "assegura a estabilidade geotécnica", "otimiza o ciclo de lavra", "maximiza o teor da reserva", "mitiga os riscos de ruptura", "promove a mineração responsável", "garante a integridade física do maciço", "otimiza a drenagem de águas pluviais", "reduz o índice de umidade dos rejeitos", "assegura o fator de segurança geotécnico"],
            "v_intrans_p": ["aumentam a recuperação metalúrgica", "asseguram a estabilidade geotécnica", "otimizam o ciclo de lavra", "maximizam o teor da reserva", "mitigam os riscos de ruptura", "promovem a mineração responsável", "garantem a integridade física do maciço", "otimizam a drenagem de águas pluviais", "reduzem o índice de umidade dos rejeitos", "asseguram o fator de segurança geotécnico"],
            "circ": ["Diante das condições do maciço rochoso", "Com o avanço da frente de lavra", "Sob a ótica da segurança de barragens", "No âmbito do plano de aproveitamento econômico", "A partir do monitoramento geotécnico contínuo", "Em conformidade com as normas regulamentadoras de mineração", "Diante dos estudos de estabilidade da cava", "Com o controle rigoroso da disposição de rejeitos", "No contexto da recuperação de áreas mineradas", "A partir da análise dos teores de corte", "Com o monitoramento piezométrico em tempo real", "Em consonância com as diretrizes da ANM", "Diante dos laudos de estabilidade de taludes"]
        },
        "politics": {
            "n_ms": [
                "pacto federativo", "processo legislativo", "orçamento participativo", "cenário eleitoral",
                "debate parlamentar", "pleito eleitoral", "acordo político", "projeto de lei",
                "sistema multipartidário", "quórum qualificado", "plenário da câmara", "quórum de votação",
                "obstrução legislativa", "veto presidencial", "acordo de lideranças", "voto de confiança",
                "relatório de comissão", "regimento interno da câmara", "plano plurianual", "recesso parlamentar"
            ],
            "n_fs": [
                "bancada parlamentar", "reforma institucional", "coalizão partidária", "articulação política",
                "soberania popular", "política pública", "diplomacia multilateral", "representatividade democrática",
                "emenda constitucional", "casa legislativa", "comissão parlamentar de inquérito", "emenda de relator",
                "medida provisória", "sanção governamental", "reforma tributária", "diplomacia bilateral",
                "participação social", "audiência pública", "sessão extraordinária", "governabilidade institucional"
            ],
            "n_mp": [
                "direitos civis", "acordos bilaterais", "projetos de lei", "debates públicos",
                "pactos institucionais", "mandatos representativos", "partidos políticos", "pleitos eleitorais",
                "vetos presidenciais", "acordos de bancada", "destaques regimentais", "debates plenários",
                "mandatos eletivos", "atos normativos"
            ],
            "n_fp": [
                "políticas públicas", "reformas estruturais", "coalizões partidárias", "instâncias de poder",
                "diretrizes governamentais", "emendas parlamentares", "comissões temáticas", "comissões parlamentares",
                "emendas constitucionais", "medidas provisórias", "audiências públicas", "votações nominais",
                "convenções partidárias"
            ],
            "adj_ms": [" parlamentar", " legislativo", " democrático", " institucional", " governamental", " multipartidário", " suprapartidário", " diplomático", " plurianual", " regimental", " republicano", " federativo", " bicameral"],
            "adj_fs": [" parlamentar", " legislativa", " democrática", " institucional", " governamental", " multipartidária", " suprapartidária", " diplomática", " plurianual", " regimental", " republicana", " federativa", " bicameral"],
            "adj_mp": [" parlamentares", " legislativos", " democráticos", " institucionais", " governamentais", " multipartidários", " plurianuais", " regimentais", " republicanos", " federativos", " bicamerais"],
            "adj_fp": [" parlamentares", " legislativas", " democráticas", " institucionais", " governamentais", " multipartidárias", " plurianuais", " regimentais", " republicanas", " federativas", " bicamerais"],
            "v_trans_s": ["articula ", "tramita ", "promulga ", "sanciona ", "debate ", "pactua ", "delibera ", "vota ", "negocia ", "incorpora ", "implementa ", "aprova ", "regulamenta ", "veta ", "emenda "],
            "v_trans_p": ["articulam ", "tramitam ", "promulgam ", "sancionam ", "debatem ", "pactuam ", "deliberam ", "votam ", "negociam ", "incorporam ", "implementam ", "aprovam ", "regulamentam ", "vetam ", "emendam "],
            "v_intrans_s": ["fortalece a representatividade democrática", "promove a estabilidade institucional", "assegura o exercício da cidadania", "consolida a participação popular", "viabiliza o consenso político", "fortalece a estabilidade democrática", "viabiliza o consenso partidário", "assegura a governabilidade institucional", "atende às diretrizes do plano plurianual"],
            "v_intrans_p": ["fortalecem a representatividade democrática", "promovem a estabilidade institucional", "asseguram o exercício da cidadania", "consolidam a participação popular", "viabilizam o consenso político", "fortalecem a estabilidade democrática", "viabilizam o consenso partidário", "asseguram a governabilidade institucional", "atendem às diretrizes do plano plurianual"],
            "circ": ["No atual cenário político e partidário", "Diante das deliberações do plenário", "Sob a perspectiva do pacto federativo", "Em virtude das negociações parlamentares", "No contexto da articulação da coalizão", "A partir do debate democrático", "Diante das demandas da sociedade civil", "Com o avanço das reformas institucionais", "No âmbito do processo legislativo", "Em observância à soberania popular", "Durante as sessões deliberativas do plenário", "Conforme os ritos do processo legislativo", "Em resposta às deliberações das comissões"]
        },
        "technology": {
            "n_ms": [
                "modelo estrutural", "planejamento estratégico", "sprint de inovação", "ecossistema de negócios",
                "pipeline de integração", "benchmark de mercado", "vetor de transformação", "dashboard de KPIs",
                "algoritmo preditivo", "servidor distribuído", "cluster de computação", "grafo de conhecimento",
                "modelo de linguagem", "banco de dados vetorial", "processamento assíncrono", "pipeline de telemetria",
                "balanceador de carga", "ambiente de microsserviços", "cluster de orquestração", "protocolo de comunicação"
            ],
            "n_fs": [
                "governança corporativa", "disrupção tecnológica", "metodologia ágil", "transformação digital",
                "arquitetura de microsserviços", "experiência do usuário", "inteligência preditiva", "matriz de priorização",
                "infraestrutura em nuvem", "linguagem de programação", "tolerância a falhas", "latência de rede",
                "autenticação multifator", "esteira de integração contínua", "arquitetura orientada a eventos",
                "computação quântica", "infraestrutura declarativa", "camada de abstração", "observabilidade operacional"
            ],
            "n_mp": [
                "fluxos de trabalho", "gargalos operacionais", "mecanismos de controle", "sistemas legados",
                "requisitos não-funcionais", "drivers de crescimento", "microsserviços escaláveis", "bancos de dados relacionais",
                "grafos de conhecimento", "modelos de linguagem", "bancos de dados vetoriais", "balanceadores de carga",
                "pipelines de dados", "ambientes conteinerizados", "repositórios de código"
            ],
            "n_fp": [
                "atividades operacionais", "metas estratégicas", "ferramentas tecnológicas", "competências essenciais",
                "soluções de ponta a ponta", "capacidades analíticas", "APIs RESTful", "filas de mensagens",
                "redes neurais convolucionais", "esteiras de CI/CD", "rotinas assíncronas", "políticas de segurança",
                "mensagerias distribuídas"
            ],
            "adj_ms": [" resiliente", " adaptativo", " sustentável", " disruptivo", " otimizado", " escalável", " inovador", " orientado a dados", " distribuído", " contenerizado", " assíncrono", " desacoplado", " autoescalável", " determinístico"],
            "adj_fs": [" resiliente", " adaptativa", " sustentável", " disruptiva", " otimizada", " escalável", " inovadora", " orientada a dados", " distribuída", " contenerizada", " assíncrona", " desacoplada", " autoescalável", " determinística"],
            "adj_mp": [" resilientes", " adaptativos", " sustentáveis", " disruptivos", " otimizados", " escaláveis", " inovadores", " orientados a dados", " distribuídos", " assíncronos", " conteinerizados", " desacoplados", " autoescaláveis"],
            "adj_fp": [" resilientes", " adaptativas", " sustentáveis", " disruptivas", " otimizadas", " escaláveis", " inovadoras", " orientadas a dados", " distribuídas", " assíncronas", " conteinerizadas", " desacopladas", " autoescaláveis"],
            "v_trans_s": ["exige ", "obriga ", "impulsiona ", "otimiza ", "viabiliza ", "sustenta ", "alavanca ", "desbloqueia ", "orquestra ", "compila ", "incorpora ", "implementa ", "conteineriza ", "desacopla ", "sincroniza ", "indexa "],
            "v_trans_p": ["exigem ", "obrigam ", "impulsionam ", "otimizam ", "viabilizam ", "sustentam ", "alavancam ", "desbloqueiam ", "orquestram ", "compilam ", "incorporam ", "implementam ", "conteinerizam ", "desacoplam ", "sincronizam ", "indexam "],
            "v_intrans_s": ["evolui de forma contínua", "progride a passos largos", "se consolida no mercado", "gera valor agregado de longo prazo", "reduz a latência operacional", "garante alta disponibilidade do cluster", "otimiza a taxa de transferência de dados", "reduz o consumo de recursos computacionais", "mantém a consistência eventual"],
            "v_intrans_p": ["evoluem de forma contínua", "progridem a passos largos", "se consolidam no mercado", "geram valor agregado de longo prazo", "reduzem a latência operacional", "garantam alta disponibilidade do cluster", "otimizam a taxa de transferência de dados", "reduzem o consumo de recursos computacionais", "mantêm a consistência eventual"],
            "circ": ["Com o advento das novas arquiteturas cloud", "A partir da adoção das metodologias ágeis", "Com a aceleração da automação e IA", "No contexto de sistemas distribuídos", "Diante da evolução da engenharia de software", "Com foco na escalabilidade e resiliência", "A partir da modernização de sistemas legados", "Com a integração contínua de pipelines", "Sob a perspectiva da segurança da informação", "Diante da constante disrupção digital", "Com a orquestração distribuída de microsserviços", "No contexto de computação de alto desempenho", "A partir da telemetria e observabilidade em tempo real"]
        }
    },
    "en": {
        "business": {
            "n_s": [
                "strategic planning", "business plan", "cash flow", "return on investment",
                "market positioning", "board of directors", "financial equilibrium", "commercial agreement",
                "operating budget", "projected valuation", "working capital", "corporate governance",
                "competitive advantage", "operational synergy", "feasibility analysis", "strategic decision",
                "balance sheet", "acquisition cost", "operating income", "contingent liability",
                "shareholder equity", "due diligence", "financial leverage", "EBITDA margin", "contingency plan"
            ],
            "n_p": [
                "key stakeholders", "financial metrics", "operating margins", "growth vectors",
                "revenue models", "emerging markets", "strategic partnerships", "capital allocations",
                "quarterly earnings", "operating expenses", "core competencies", "capital injections",
                "audit reports", "distributed dividends", "strategic investments", "liquidity ratios"
            ],
            "adj": ["strategic", "corporate", "financial", "profitable", "competitive", "operational", "scalable", "lucrative", "commercial", "enterprise-grade", "fiduciary", "consolidated", "auditable", "synergistic"],
            "v_trans_s": ["maximizes ", "leverages ", "optimizes ", "consolidates ", "enhances ", "enables ", "structures ", "drives ", "mitigates ", "scales ", "allocates ", "audits ", "capitalizes ", "diversifies "],
            "v_trans_p": ["maximize ", "leverage ", "optimize ", "consolidate ", "enhance ", "enable ", "structure ", "drive ", "mitigate ", "scale ", "allocate ", "audit ", "capitalize ", "diversify "],
            "v_intrans_s": ["maximizes return on investment", "delivers long-term shareholder value", "strengthens market position", "ensures financial resilience", "drives operational excellence", "accelerates business growth", "maximizes cash flow generation", "mitigates market risk exposure", "sustains long-term corporate growth"],
            "v_intrans_p": ["maximize return on investment", "deliver long-term shareholder value", "strengthen market position", "ensure financial resilience", "drive operational excellence", "accelerate business growth", "maximize cash flow generation", "mitigate market risk exposure", "sustain long-term corporate growth"],
            "circ": ["In today's corporate landscape", "Faced with evolving market dynamics", "Given the rise in global competition", "Under the lens of corporate governance", "Considering new strategic challenges", "Without losing sight of short-term milestones", "Focusing on sustainable value creation", "Amidst evolving compliance standards", "Prioritizing operational excellence", "When evaluating investment returns", "Under independent audit scrutiny", "Amid capital market volatility", "Following balance sheet consolidation"]
        },
        "ecology": {
            "n_s": [
                "carbon credit", "fragile biome", "sustainable ecosystem", "ecological impact",
                "forest management", "conscious reforestation", "sustainable development", "emissions inventory",
                "energy transition", "carbon footprint", "biodiversity conservation", "circular economy",
                "renewable grid", "climate resilience", "habitat protection", "waste recovery",
                "ecological corridor", "ecosystem service", "natural capital", "watershed management",
                "life cycle assessment", "degraded land reclamation", "biomass stock", "environmental offset"
            ],
            "n_p": [
                "natural resources", "local ecosystems", "environmental indicators", "carbon credits",
                "sustainability standards", "protected habitats", "renewable energies", "decarbonization goals",
                "ecological reserves", "green technologies", "conservation practices", "ecological corridors",
                "protected watersheds", "sustainability indicators", "water resources", "carbon sinks", "native species"
            ],
            "adj": ["sustainable", "ecological", "low-carbon", "renewable", "carbon-neutral", "biodegradable", "environmentally-sound", "climate-resilient", "bio-based", "regenerative", "restorative", "hydrological", "conservationist"],
            "v_trans_s": ["preserves ", "mitigates ", "regenerates ", "decarbonizes ", "conserves ", "restores ", "rehabilitates ", "protects ", "sequesters ", "reforests ", "revegetates ", "balances ", "neutralizes "],
            "v_trans_p": ["preserve ", "mitigate ", "regenerate ", "decarbonize ", "conserve ", "restore ", "rehabilitate ", "protect ", "sequester ", "reforest ", "revegetate ", "balance ", "neutralize "],
            "v_intrans_s": ["promotes climate neutrality", "reduces environmental impact", "strengthens biodiversity", "ensures ecological balance", "fosters environmental stewardship", "restores landscape integrity", "safeguards freshwater sources", "enhances ecological resilience"],
            "v_intrans_p": ["promote climate neutrality", "reduce environmental impact", "strengthen biodiversity", "ensure ecological balance", "foster environmental stewardship", "restore landscape integrity", "safeguard freshwater sources", "enhance ecological resilience"],
            "circ": ["In the face of global climate change", "Within the framework of environmental conservation", "With the acceleration of ecological transition", "From the perspective of biome preservation", "Based on environmental impact assessments", "Focusing on ecosystem regeneration", "In accordance with sustainability commitments", "Amid concerns over biodiversity loss", "Through continuous habitat monitoring", "Guided by net-zero decarbonization targets", "In alignment with climate goals", "Within the scope of forest restoration"]
        },
        "law": {
            "n_s": [
                "due process of law", "legal order", "judicial litigation", "legal protection",
                "legal opinion", "formal defect", "constitutional norm", "binding precedent",
                "established jurisprudence", "legal certainty", "statutory framework", "judicial decree",
                "interlocutory appeal", "burden of proof", "legal remedy", "injunctive relief",
                "contractual breach", "causal link", "statute of limitations", "judicial review",
                "civil liability", "adversarial proceeding", "substantive due process"
            ],
            "n_p": [
                "fundamental rights", "procedural deadlines", "judicial precedents", "court records",
                "statutory provisions", "constitutional guarantees", "legal prerogatives", "attorney fees",
                "binding rulings", "evidentiary standards", "superior courts", "procedural safeguards",
                "contractual obligations", "declaratory judgments"
            ],
            "adj": ["legal", "constitutional", "procedural", "binding", "statutory", "uncontestable", "judicial", "jurisprudence-based", "enforceable", "legitimate", "precedential", "substantive", "adversarial", "mandatory"],
            "v_trans_s": ["substantiates ", "ratifies ", "settles ", "prescribes ", "regulates ", "establishes ", "enforces ", "adjudicates ", "upholds ", "vacates ", "affirms ", "overrules ", "adjudges "],
            "v_trans_p": ["substantiate ", "ratify ", "settle ", "prescribe ", "regulate ", "establish ", "enforce ", "adjudicate ", "uphold ", "vacate ", "affirm ", "overrule ", "adjudge "],
            "v_intrans_s": ["guarantees legal certainty", "safeguards due process", "upholds constitutional norms", "consolidates judicial understanding", "protects fundamental rights", "ensures fair trial guarantees", "binds adjudicating authorities", "precludes punitive claims"],
            "v_intrans_p": ["guarantee legal certainty", "safeguard due process", "uphold constitutional norms", "consolidate judicial understanding", "protect fundamental rights", "ensure fair trial guarantees", "bind adjudicating authorities", "preclude punitive claims"],
            "circ": ["In light of the prevailing legal order", "Under constitutional scrutiny", "In view of established jurisprudence", "In compliance with due process of law", "Within the scope of procedural proceedings", "Grounding upon fundamental legal principles", "Pursuant to applicable statutory provisions", "In accordance with judicial precedents", "Under the jurisdiction of the court", "Upholding constitutional guarantees", "Subject to adversarial scrutiny", "Pursuant to the rules of procedure"]
        },
        "medicine": {
            "n_s": [
                "clinical diagnosis", "therapeutic protocol", "clinical trial", "biological marker",
                "symptomatic profile", "prophylactic treatment", "laboratory examination", "medical prognosis",
                "pharmacovigilance", "cellular immunity", "disease pathophysiology", "surgical intervention",
                "therapeutic efficacy", "autologous transplant", "double-blind study", "serological marker",
                "tumor necrosis factor", "septic condition", "histopathological analysis", "pharmacokinetic profile",
                "cardiac catheterization", "clinical outcome"
            ],
            "n_p": [
                "clinical trials", "biological markers", "randomized trials", "characteristic symptoms",
                "pathogenic agents", "physiological parameters", "immunological responses", "therapeutic regimens",
                "adverse reactions", "diagnostic guidelines", "serological markers", "double-blind studies",
                "multicenter clinical trials", "hemodynamic parameters", "histological findings"
            ],
            "adj": ["therapeutic", "clinical", "prophylactic", "physiological", "pathogenic", "multidisciplinary", "asymptomatic", "pharmacological", "etiological", "diagnostic", "epidemiological", "immunological", "histopathological", "adjuvant"],
            "v_trans_s": ["diagnoses ", "synthesizes ", "attenuates ", "rehabilitates ", "prescribes ", "stabilizes ", "modulates ", "inhibits ", "alleviates ", "induces ", "blocks ", "eradicates "],
            "v_trans_p": ["diagnose ", "synthesize ", "attenuate ", "rehabilitate ", "prescribe ", "stabilize ", "modulate ", "inhibit ", "alleviate ", "induce ", "block ", "eradicate "],
            "v_intrans_s": ["enhances immune response", "ensures therapeutic efficacy", "combats pathology progression", "secures clinical recovery", "optimizes patient outcome", "stabilizes vital parameters", "mitigates inflammatory response", "restores physiological homeostasis"],
            "v_intrans_p": ["enhance immune response", "ensure therapeutic efficacy", "combat pathology progression", "secure clinical recovery", "optimize patient outcome", "stabilize vital parameters", "mitigate inflammatory response", "restore physiological homeostasis"],
            "circ": ["In the context of evidence-based clinical practice", "Considering the patient's symptomatic profile", "Based on randomized controlled trials", "From the standpoint of pharmacovigilance", "Following early clinical diagnosis", "With the advent of novel therapeutic regimens", "In adherence to established medical protocols", "Given the observed immunological response", "Throughout long-term patient monitoring", "Focusing on treatment efficacy and safety", "During continuous hemodynamic monitoring", "Under strict pharmacotherapeutic control"]
        },
        "mining": {
            "n_s": [
                "ore processing", "deposit grade", "geological retreat", "mining plan",
                "geotechnical mapping", "mineral processing", "sedimentary deposit", "underground mining",
                "tailings dam", "mineral exploration", "cutoff grade", "opencast mine",
                "slurry pipeline", "rotary drilling", "dam decommissioning", "pit slope",
                "upstream raising", "downstream raising", "rock mass", "host rock",
                "waste rock dump", "dry stacking", "vibrating wire piezometer", "interferometric radar",
                "triaxial test", "mineral beneficiation"
            ],
            "n_p": [
                "mineral tailings", "cutoff grades", "geotechnical parameters", "mineralized bodies",
                "extractable reserves", "extraction methods", "ore concentrates", "hydrogeological surveys",
                "host rocks", "pit slopes", "rock masses", "vibrating wire piezometers", "geomechanical tests",
                "filtered tailings", "extraction benches"
            ],
            "adj": ["mineral", "geotechnical", "geological", "extractive", "high-grade", "sustainable", "hydrogeological", "sedimentary", "open-pit", "underground", "geomechanical", "piezometric", "dewatered", "metallurgical"],
            "v_trans_s": ["extracts ", "processes ", "maps ", "beneficiates ", "stabilizes ", "optimizes ", "drills ", "excavates ", "samples ", "heightens ", "dewaters ", "consolidates "],
            "v_trans_p": ["extract ", "process ", "map ", "beneficiate ", "stabilize ", "optimize ", "drill ", "excavate ", "sample ", "heighten ", "dewater ", "consolidate "],
            "v_intrans_s": ["increases metallurgical recovery", "ensures geotechnical stability", "optimizes the mining cycle", "maximizes deposit value", "mitigates slope failure risks", "safeguards rock mass integrity", "enhances pit water drainage", "achieves geotechnical safety factors"],
            "v_intrans_p": ["increase metallurgical recovery", "ensure geotechnical stability", "optimize the mining cycle", "maximize deposit value", "mitigate slope failure risks", "safeguard rock mass integrity", "enhance pit water drainage", "achieve geotechnical safety factors"],
            "circ": ["Given the conditions of the rock mass", "With the progression of the mining face", "From the perspective of tailings dam safety", "Within the framework of the mine development plan", "Through continuous geotechnical monitoring", "In compliance with mineral regulatory standards", "Based on pit slope stability assessments", "With rigorous tailings management protocols", "In the context of mine site reclamation", "Guided by cutoff grade optimization", "With real-time piezometric monitoring", "According to geotechnical stability reports"]
        },
        "politics": {
            "n_s": [
                "federal pact", "legislative process", "participatory budgeting", "electoral landscape",
                "parliamentary debate", "political agreement", "bill draft", "parliamentary caucus",
                "institutional reform", "party coalition", "constitutional amendment", "diplomatic protocol",
                "democratic representation", "voting quorum", "congressional committee of inquiry",
                "legislative filibuster", "presidential veto", "vote of confidence", "committee report",
                "multi-year budget plan", "extraordinary session"
            ],
            "n_p": [
                "civil rights", "bilateral agreements", "legislative bills", "public debates",
                "institutional pacts", "representative mandates", "political parties", "parliamentary committees",
                "diplomatic channels", "presidential vetoes", "caucus agreements", "plenary debates",
                "elective mandates", "statutory acts"
            ],
            "adj": ["parliamentary", "legislative", "democratic", "institutional", "governmental", "bipartisan", "diplomatic", "constitutional", "multilateral", "multi-year", "republican", "bicameral", "coalition-based"],
            "v_trans_s": ["articulates ", "promulgates ", "enacts ", "debates ", "sanctions ", "negotiates ", "deliberates ", "ratifies ", "sponsors ", "passes ", "amends ", "vetoes "],
            "v_trans_p": ["articulate ", "promulgate ", "enact ", "debate ", "sanction ", "negotiate ", "deliberate ", "ratify ", "sponsor ", "pass ", "amend ", "veto "],
            "v_intrans_s": ["strengthens democratic representation", "promotes institutional stability", "ensures civic participation", "consolidates popular sovereignty", "fosters political consensus", "fosters democratic governance", "secures partisan compromise", "fulfills multi-year strategic guidelines"],
            "v_intrans_p": ["strengthen democratic representation", "promote institutional stability", "ensure civic participation", "consolidate popular sovereignty", "foster political consensus", "foster democratic governance", "secure partisan compromise", "fulfill multi-year strategic guidelines"],
            "circ": ["In the current political landscape", "Amid parliamentary debates and deliberations", "Under the framework of the federal pact", "Given ongoing coalition negotiations", "Within the scope of the legislative process", "Through open democratic debate", "Responding to civic and public demands", "With the progress of institutional reforms", "Upholding democratic representation", "In accordance with constitutional mandates", "During plenary deliberative sessions", "Following committee recommendations"]
        },
        "technology": {
            "n_s": [
                "business model", "strategic planning", "digital transformation", "microservices architecture",
                "cloud computing", "machine learning", "artificial intelligence", "integration pipeline",
                "data engineering", "cybersecurity framework", "scalable infrastructure", "automated workflow",
                "API gateway", "knowledge graph", "large language model", "vector database",
                "asynchronous processing", "telemetry pipeline", "load balancer", "orchestration cluster",
                "fault tolerance", "event-driven architecture"
            ],
            "n_p": [
                "workflows", "operational bottlenecks", "control mechanisms", "legacy systems",
                "non-functional requirements", "growth drivers", "microservices", "relational databases",
                "cloud clusters", "containerized deployments", "knowledge graphs", "vector databases",
                "telemetry pipelines", "distributed queues", "data pipelines"
            ],
            "adj": ["resilient", "adaptive", "sustainable", "disruptive", "optimized", "scalable", "innovative", "data-driven", "distributed", "containerized", "cloud-native", "asynchronous", "decoupled", "auto-scaling", "deterministic"],
            "v_trans_s": ["demands ", "requires ", "drives ", "optimizes ", "enables ", "sustains ", "leverages ", "unlocks ", "orchestrates ", "deploys ", "containerizes ", "decouples ", "synchronizes ", "indexes "],
            "v_trans_p": ["demand ", "require ", "drive ", "optimize ", "enable ", "sustain ", "leverage ", "unlock ", "orchestrate ", "deploy ", "containerize ", "decouple ", "synchronize ", "index "],
            "v_intrans_s": ["evolves continuously", "progresses rapidly", "consolidates in the market", "delivers long-term value", "reduces operational latency", "ensures high cluster availability", "optimizes data throughput", "preserves eventual consistency"],
            "v_intrans_p": ["evolve continuously", "progress rapidly", "consolidate in the market", "deliver long-term value", "reduce operational latency", "ensure high cluster availability", "optimize data throughput", "preserve eventual consistency"],
            "circ": ["With the advent of cloud-native systems", "Through the adoption of agile frameworks", "With the acceleration of digital automation and AI", "In the context of distributed systems", "Given the rapid evolution of software engineering", "Focusing on system scalability and resilience", "Through the modernization of legacy stacks", "With continuous integration and deployment pipelines", "From the perspective of information security", "Amid ongoing technological disruption", "With distributed microservice orchestration", "In high-throughput computing environments"]
        }
    },
    "es": {
        "business": {
            "n_ms": [
                "planeamiento estratégico", "plan de negocios", "flujo de caja", "retorno de la inversión",
                "posicionamiento de mercado", "consejo de administración", "equilibrio financiero", "acuerdo comercial",
                "presupuesto operativo", "capital de trabajo", "crecimiento sostenible", "rendimiento corporativo",
                "balance general", "coste de adquisición", "beneficio operativo", "pasivo contingente",
                "patrimonio neto", "fondo de garantía", "acuerdo de accionistas", "ebitda ajustado", "plan de contingencia"
            ],
            "n_fs": [
                "estrategia corporativa", "gestión de riesgos", "margen de rentabilidad", "gobernanza corporativa",
                "ventaja competitiva", "sinergia operativa", "eficiencia financiera", "visión estratégica",
                "rentabilidad sostenida", "auditoría contable", "due diligence", "apalancamiento financiero",
                "valoración patrimonial", "gobernanza ESG", "liquidez corriente", "gestión de activos", "toma de decisiones"
            ],
            "n_mp": [
                "indicadores financieros", "principales accionistas", "activos estratégicos", "resultados operativos",
                "planes de contingencia", "mercados emergentes", "fondos de inversión", "costes operativos",
                "aportes de capital", "títulos de crédito", "informes de auditoría", "dividendos distribuidos",
                "vectores de crecimiento"
            ],
            "n_fp": [
                "directrices estratégicas", "oportunidades de mercado", "metas corporativas", "proyecciones financieras",
                "alianzas comerciales", "ventajas competitivas", "reservas de contingencia", "obligaciones tributarias",
                "cuentas anuales", "previsiones presupuestarias", "sinergias empresariales"
            ],
            "adj_ms": [" estratégico", " corporativo", " financiero", " rentable", " competitivo", " operativo", " escalable", " comercial", " fiduciario", " consolidado", " superavitario", " auditable"],
            "adj_fs": [" estratégica", " corporativa", " financiera", " rentable", " competitiva", " operativa", " escalable", " comercial", " fiduciaria", " consolidada", " superavitaria", " auditable"],
            "adj_mp": [" estratégicos", " corporativos", " financieros", " rentables", " competitivos", " operativos", " escalables", " fiduciarios", " consolidados", " superavitarios"],
            "adj_fp": [" estratégicas", " corporativas", " financieras", " rentables", " competitivas", " operativas", " escalables", " fiduciarias", " consolidadas", " superavitarias"],
            "v_trans_s": ["maximiza ", "apalanca ", "optimiza ", "consolida ", "potencia ", "viabiliza ", "impulsa ", "mitiga ", "asigna ", "audita ", "capitaliza ", "diversifica "],
            "v_trans_p": ["maximizan ", "apalancan ", "optimizan ", "consolidan ", "potencian ", "viabilizan ", "impulsan ", "mitigan ", "asignan ", "auditan ", "capitalizan ", "diversifican "],
            "v_intrans_s": ["maximiza el retorno de la inversión", "asegura la solidez financiera", "fortalece el posicionamiento en el mercado", "genera valor a largo plazo", "maximiza el flujo de caja", "mitiga la exposición a riesgos de mercado", "sostiene el crecimiento corporativo"],
            "v_intrans_p": ["maximizan el retorno de la inversión", "aseguran la solidez financiera", "fortalecen el posicionamiento en el mercado", "generan valor a largo plazo", "maximizan el flujo de caja", "mitigan la exposición a riesgos de mercado", "sostienen el crecimiento corporativo"],
            "circ": ["En el actual escenario corporativo", "Ante las nuevas exigencias del mercado", "Debido al aumento de la competitividad global", "Bajo la perspectiva de la gobernanza corporativa", "Dados los nuevos desafíos empresariales", "Sin perder de vista el alineamiento a corto plazo", "Con foco en la entrega de resultados", "Ante los crecientes estándares de cumplimiento", "Con enfoque en la excelencia operativa", "Al evaluar el retorno de la inversión", "Bajo el rigor de la auditoría independiente", "Ante la volatilidad de los mercados de capitales"]
        },
        "ecology": {
            "n_ms": [
                "crédito de carbono", "bioma frágil", "ecosistema sostenible", "impacto ecológico",
                "manejo forestal", "desarrollo sostenible", "inventario de emisiones", "recurso hídrico",
                "balance energético", "hábitat natural", "corredor ecológico", "servicio ecosistémico",
                "capital natural", "ciclo biogeoquímico", "manejo de cuencas", "plan de conservación",
                "stock de biomasa", "patrimonio genético"
            ],
            "n_fs": [
                "transición energética", "huella de carbono", "biodiversidad preservada", "conservación ambiental",
                "economía circular", "neutralidad climática", "gestión de residuos", "sostenibilidad ecológica",
                "matriz renovable", "evaluación de impacto ambiental", "reserva extractiva", "conectividad ecológica",
                "área de protección ambiental", "acción antrópica", "evaluación del ciclo de vida",
                "rehabilitación de áreas degradadas", "resiliencia climática", "gestión de recursos hídricos",
                "compensación ambiental"
            ],
            "n_mp": [
                "recursos naturales", "ecosistemas locales", "indicadores ambientales", "créditos de carbono",
                "hábitats protegidos", "residuos sólidos", "servicios ecosistémicos", "corredores ecológicos",
                "recursos hídricos", "sumideros de carbono", "procesos ecológicos"
            ],
            "n_fp": [
                "energías renovables", "metas de descarbonización", "políticas ambientales", "áreas de preservación",
                "prácticas sostenibles", "fuentes limpias", "emisiones de gases de efecto invernadero",
                "medidas mitigadoras", "especies nativas", "cuencas hidrográficas", "reservas naturales"
            ],
            "adj_ms": [" sostenible", " ecológico", " de bajo carbono", " renovable", " de impacto neutro", " biodegradable", " ecosistémico", " bioclimático", " restaurativo", " regenerativo", " hidrológico", " conservacionista"],
            "adj_fs": [" sostenible", " ecológica", " de bajo carbono", " renovable", " de impacto neutro", " biodegradable", " ecosistémica", " bioclimática", " restaurativa", " regenerativa", " hidrológica", " conservacionista"],
            "adj_mp": [" sostenibles", " ecológicos", " de bajo carbono", " renovables", " de impacto neutro", " biodegradables", " bioclimáticos", " restaurativos", " regenerativos"],
            "adj_fp": [" sostenibles", " ecológicas", " de bajo carbono", " renovables", " de impacto neutro", " biodegradables", " bioclimáticas", " restaurativas", " regenerativas"],
            "v_trans_s": ["preserva ", "mitiga ", "regenera ", "descarboniza ", "conserva ", "restaura ", "protege ", "rehabilita ", "reforesta ", "equilibra ", "neutraliza "],
            "v_trans_p": ["preservan ", "mitigan ", "regeneran ", "descarbonizan ", "conservan ", "restauran ", "protegen ", "rehabilitan ", "reforestan ", "equilibran ", "neutralizan "],
            "v_intrans_s": ["promueve la neutralidad climática", "reduce el impacto ambiental", "fortalece la biodiversidad", "asegura el equilibrio ecológico", "restaura la integridad del paisaje", "salvaguarda las fuentes hídricas", "fortalece la resiliencia ecológica"],
            "v_intrans_p": ["promueven la neutralidad climática", "reducen el impacto ambiental", "fortalecen la biodiversidad", "aseguran el equilibrio ecológico", "restauran la integridad del paisaje", "salvaguardan las fuentes hídricas", "fortalecen la resiliencia ecológica"],
            "circ": ["Frente al cambio climático global", "En el marco de la conservación ambiental", "Con el avance de la transición ecológica", "Bajo la perspectiva de la preservación de biomas", "A partir de la evaluación de impacto ambiental", "Con foco en la regeneración de ecosistemas", "En cumplimiento de los compromisos de sostenibilidad", "Ante la pérdida de biodiversidad", "Mediante el monitoreo constante de hábitats", "Con base en las metas de descarbonización", "En consonancia con los objetivos climáticos"]
        },
        "law": {
            "n_ms": [
                "debido proceso legal", "ordenamiento jurídico", "litigio judicial", "amparo legal",
                "dictamen jurídico", "vicio formal", "recurso procedente", "auto judicial",
                "proveído jurisdiccional", "pronunciamiento definitivo", "recurso de casación",
                "efecto suspensivo", "incumplimiento contractual", "daño moral", "nexo causal",
                "mandamiento judicial", "recurso extraordinario", "principio de contradicción"
            ],
            "n_fs": [
                "jurisprudencia consolidada", "seguridad jurídica", "norma constitucional", "instrucción procesal",
                "presunción de inocencia", "tutela de urgencia", "medida cautelar", "petición inicial",
                "cosa juzgada", "tutela provisional", "prescripción extintiva", "costas procesales",
                "relevancia constitucional", "inconstitucionalidad material", "competencia jurisdiccional",
                "responsabilidad civil", "acción rescisoria", "citación judicial"
            ],
            "n_mp": [
                "derechos fundamentales", "plazos procesales", "precedentes judiciales", "fundamentos legales",
                "recursos oportunos", "honorarios profesionales", "efectos estimatorios", "medios probatorios",
                "tribunales superiores", "autos judiciales"
            ],
            "n_fp": [
                "garantías constitucionales", "normas jurídicas", "decisiones interlocutorias", "medidas cautelares",
                "pretensiones jurídicas", "obligaciones contractuales", "garantías procesales", "presunciones legales",
                "acciones declarativas"
            ],
            "adj_ms": [" jurídico", " constitucional", " procesal", " vinculante", " ineludible", " tempestivo", " jurisprudencial", " firme y formal", " rescisorio", " subsidiario", " imperativo"],
            "adj_fs": [" jurídica", " constitucional", " procesal", " vinculante", " ineludible", " tempestiva", " jurisprudencial", " firme y formal", " rescisoria", " subsidiaria", " imperativa"],
            "adj_mp": [" jurídicos", " constitucionales", " procesales", " vinculantes", " ineludibles", " tempestivos", " rescisorios", " subsidiarios"],
            "adj_fp": [" jurídicas", " constitucionales", " procesales", " vinculantes", " ineludibles", " tempestivas", " rescisorias", " subsidiarias"],
            "v_trans_s": ["fundamenta ", "ratifica ", "pacifica ", "prescribe ", "reglamenta ", "asienta ", "defiende ", "avala ", "revoca ", "homologa ", "invalida ", "adjudica "],
            "v_trans_p": ["fundamentan ", "ratifican ", "pacifican ", "prescriben ", "reglamentan ", "asientan ", "defienden ", "avalan ", "revocan ", "homologan ", "invalidan ", "adjudican "],
            "v_intrans_s": ["garantiza la seguridad jurídica", "resguarda el debido proceso", "cumple la norma constitucional", "consolida la jurisprudencia", "asegura el derecho a la defensa", "vincula a los órganos judiciales", "desestima la pretensión punitiva"],
            "v_intrans_p": ["garantizan la seguridad jurídica", "resguardan el debido proceso", "cumplen la norma constitucional", "consolidan la jurisprudencia", "aseguran el derecho a la defensa", "vinculan a los órganos judiciales", "desestiman la pretensión punitiva"],
            "circ": ["A la luz del ordenamiento jurídico vigente", "Bajo la óptica constitucional", "Ante la jurisprudencia consolidada", "En observancia del debido proceso legal", "En el marco de la instrucción procesal", "Con base en los preceptos fundamentales", "Ante las garantías constitucionales", "En sede de admisibilidad judicial", "Según la legislación aplicable", "Conforme al criterio de los tribunales", "Bajo el principio de contradicción"]
        },
        "medicine": {
            "n_ms": [
                "diagnóstico clínico", "protocolo terapéutico", "ensayo clínico", "marcador biológico",
                "cuadro sintomático", "tratamiento profiláctico", "examen analítico", "pronóstico médico",
                "agente patógeno", "estudio doble ciego", "marcador serológico", "factor de necrosis tumoral",
                "cuadro de sepsis", "antibiograma bacteriano", "análisis histopatológico", "perfil farmacocinético",
                "cateterismo cardíaco", "resultado clínico"
            ],
            "n_fs": [
                "terapia profiláctica", "farmacovigilancia", "conducta médica", "anamnesis detallada",
                "inmunidad celular", "fisiopatología", "respuesta inmune", "eficacia terapéutica",
                "remisión completa", "comorbilidad asociada", "terapia adyuvante", "farmacocinética clínica",
                "incidencia epidemiológica", "resistencia microbiana", "intervención endovascular",
                "ventilación mecánica", "biopsia tisular", "inmunoterapia celular"
            ],
            "n_mp": [
                "ensayos clínicos", "marcadores biológicos", "síntomas característicos", "agentes patógenos",
                "parámetros fisiológicos", "estudios aleatorizados", "ensayos multicéntricos", "factores de riesgo",
                "parámetros hemodinámicos", "hallazgos histológicos"
            ],
            "n_fp": [
                "respuestas inmunológicas", "terapias innovadoras", "intervenciones quirúrgicas", "evidencias científicas",
                "reacciones adversas", "comorbilidades clínicas", "terapias adyuvantes", "muestras biológicas",
                "tasas de remisión"
            ],
            "adj_ms": [" terapéutico", " clínico", " profiláctico", " fisiológico", " patógeno", " multidisciplinar", " asintomático", " etiológico", " farmacológico", " epidemiológico", " inmunológico", " adyuvante", " histopatológico"],
            "adj_fs": [" terapéutica", " clínica", " profiláctica", " fisiológica", " patógena", " multidisciplinar", " asintomática", " etiológica", " farmacológica", " epidemiológica", " inmunológica", " adyuvante", " histopatológica"],
            "adj_mp": [" terapéuticos", " clínicos", " profilácticos", " fisiológicos", " patógenos", " multidisciplinares", " epidemiológicos", " inmunológicos", " adyuvantes"],
            "adj_fp": [" terapéuticas", " clínicas", " profilácticas", " fisiológicas", " patógenas", " multidisciplinares", " epidemiológicas", " inmunológicas", " adyuvantes"],
            "v_trans_s": ["diagnostica ", "sintetiza ", "atenúa ", "rehabilita ", "prescribe ", "estabiliza ", "modula ", "inhibe ", "combate ", "induce ", "bloquea ", "erradica "],
            "v_trans_p": ["diagnostican ", "sintetizan ", "atenúan ", "rehabilitan ", "prescriben ", "estabilizan ", "modulan ", "inhiben ", "combaten ", "inducen ", "bloquean ", "erradican "],
            "v_intrans_s": ["potencia la respuesta inmune", "garantiza la eficacia terapéutica", "combate la patología", "asegura la recuperación clínica", "estabiliza los parámetros vitales", "mitiga la respuesta inflamatoria", "restablece la homeostasis orgánica"],
            "v_intrans_p": ["potencian la respuesta inmune", "garantizan la eficacia terapéutica", "combaten la patología", "aseguran la recuperación clínica", "estabilizan los parámetros vitales", "mitigan la respuesta inflamatoria", "restablecen la homeostasis orgánica"],
            "circ": ["En el marco de la práctica clínica basada en evidencia", "Ante el cuadro clínico presentado", "Con base en ensayos aleatorizados", "Bajo la óptica de la farmacovigilancia", "A partir del diagnóstico temprano", "Con el avance de terapias innovadoras", "En observancia de los protocolos terapéuticos", "Dada la respuesta inmunológica observada", "En el seguimiento del pronóstico del paciente", "Con foco en la eficacia terapéutica", "Durante el monitoreo hemodinámico continuo"]
        },
        "mining": {
            "n_ms": [
                "procesamiento de mineral", "ley de yacimiento", "plan de minado", "mapeo geotécnico",
                "procesamiento mineral", "depósito sedimentario", "conducto de relaves", "estudio hidrogeológico",
                "cierre de faena", "talud de tajo", "recrecimiento aguas arriba", "recrecimiento aguas abajo",
                "macizo rocoso", "desmonte estéril", "depósito de relaves filtrados", "piezómetro de cuerda vibrante",
                "ensayo triaxial", "aprovechamiento minero"
            ],
            "n_fs": [
                "explotación subterránea", "presa de relaves", "prospección geológica", "explotación a cielo abierto",
                "geotecnia operativa", "recuperación de mina", "perforación rotativa", "drenaje ácido de mina",
                "piezometría automatizada", "recuperación metalúrgica", "estabilidad de taludes", "frente de arranque",
                "estabilidad geotécnica", "seguridad de presas"
            ],
            "n_mp": [
                "residuos mineros", "parámetros geotécnicos", "cuerpos mineralizados", "métodos de extracción",
                "concentrados minerales", "estudios geológicos", "taludes de tajo", "macizos rocosos",
                "piezómetros de cuerda vibrante", "ensayos geomecánicos", "relaves filtrados"
            ],
            "n_fp": [
                "presas de contención", "reservas probadas", "estructuras geotécnicas", "rocas encajantes",
                "escavaciones mecánicas", "frentes de explotación", "bancadas de extracción", "balsas de decantación",
                "estructuras de apilamiento"
            ],
            "adj_ms": [" mineral", " geotécnico", " geológico", " extractivo", " de alta ley", " hidrogeológico", " geomecánico", " aluvial", " piezométrico", " desaguado", " metalúrgico"],
            "adj_fs": [" mineral", " geotécnica", " geológica", " extractiva", " de alta ley", " hidrogeológica", " geomecánica", " aluvial", " piezométrica", " desaguada", " metalúrgica"],
            "adj_mp": [" minerales", " geotécnicos", " geológicos", " extractivos", " hidrogeológicos", " geomecánicos", " piezométricos", " metalúrgicos"],
            "adj_fp": [" minerales", " geotécnicas", " geológicas", " extractivas", " hidrogeológicas", " geomecánicas", " piezométricas", " metalúrgicas"],
            "v_trans_s": ["extrae ", "procesa ", "mapea ", "beneficia ", "estabiliza ", "optimiza ", "perfora ", "escava ", "recrece ", "desagua ", "consolida "],
            "v_trans_p": ["extraen ", "procesan ", "mapean ", "benefician ", "estabilizan ", "optimizan ", "perforan ", "escavan ", "recrecen ", "desaguan ", "consolidan "],
            "v_intrans_s": ["aumenta la recuperación metalúrgica", "asegura la estabilidad geotécnica", "optimiza el ciclo minero", "maximiza el valor del yacimiento", "garantiza la integridad física del macizo", "optimiza el drenaje pluvial del tajo", "asegura el factor de seguridad geotécnico"],
            "v_intrans_p": ["aumentan la recuperación metalúrgica", "aseguran la estabilidad geotécnica", "optimizan el ciclo minero", "maximizan el valor del yacimiento", "garantizan la integridad física del macizo", "optimizan el drenaje pluvial del tajo", "aseguran el factor de seguridad geotécnico"],
            "circ": ["Dadas las condiciones del macizo rocoso", "Con el avance del frente de explotación", "Bajo la óptica de la seguridad de presas de relaves", "En el marco del plan de aprovechamiento minero", "A partir del monitoreo geotécnico continuo", "En cumplimiento de las normas regulatorias mineras", "Ante los estudios de estabilidad del tajo", "Con el control riguroso del depósito de relaves", "En el contexto de la rehabilitación de faenas mineras", "A partir del análisis de las leyes de corte", "Con el monitoreo piezométrico en tiempo real"]
        },
        "politics": {
            "n_ms": [
                "pacto federal", "proceso legislativo", "presupuesto participativo", "escenario electoral",
                "debate parlamentario", "acuerdo político", "proyecto de ley", "quórum cualificado",
                "sistema multipartidista", "quórum de votación", "bloqueo legislativo", "veto presidencial",
                "voto de confianza", "dictamen de comisión", "plan plurianual", "receso parlamentario"
            ],
            "n_fs": [
                "bancada parlamentaria", "reforma institucional", "coalición partidaria", "articulación política",
                "soberania popular", "política pública", "diplomacia multilateral", "representación democrática",
                "enmienda constitucional", "comisión de investigación", "medida provisional", "sanción gubernamental",
                "reforma tributaria", "diplomacia bilateral", "participación ciudadana", "audiencia pública"
            ],
            "n_mp": [
                "derechos civiles", "acuerdos bilaterales", "proyectos de ley", "pactos institucionales",
                "mandatos representativos", "partidos políticos", "vetos presidenciales", "debates plenarios",
                "mandatos electivos"
            ],
            "n_fp": [
                "políticas públicas", "reformas estructurales", "coaliciones partidarias", "directrices gubernamentales",
                "comisiones parlamentarias", "enmiendas constitucionales", "medidas provisionales", "audiencias públicas"
            ],
            "adj_ms": [" parlamentario", " legislativo", " democrático", " institucional", " gubernamental", " multipartidista", " diplomático", " plurianual", " republicano", " bicameral"],
            "adj_fs": [" parlamentaria", " legislativa", " democrática", " institucional", " gubernamental", " multipartidista", " diplomática", " plurianual", " republicana", " bicameral"],
            "adj_mp": [" parlamentarios", " legislativos", " democráticos", " institucionales", " gubernamentales", " plurianuales", " republicanos", " bicamerales"],
            "adj_fp": [" parlamentarias", " legislativas", " democráticas", " institucionales", " gubernamentales", " plurianuales", " republicanas", " bicamerales"],
            "v_trans_s": ["articula ", "promulga ", "sanciona ", "debate ", "pacta ", "delibera ", "vota ", "negocia ", "aprueba ", "reglamenta ", "veta ", "enmienda "],
            "v_trans_p": ["articulan ", "promulgan ", "sancionan ", "debaten ", "pactan ", "deliberan ", "votan ", "negocian ", "aprueban ", "reglamentan ", "vetan ", "enmiendan "],
            "v_intrans_s": ["fortalece la representación democrática", "promueve la estabilidad institucional", "consolida la participación popular", "asegura el consenso político", "fortalece la gobernabilidad democrática", "viabiliza el consenso partidario"],
            "v_intrans_p": ["fortalecen la representación democrática", "promueven la estabilidad institucional", "consolidan la participación popular", "aseguran el consenso político", "fortalecen la gobernabilidad democrática", "viabilizan el consenso partidario"],
            "circ": ["En el actual escenario político", "Ante las deliberaciones del plenario", "Bajo la perspectiva del pacto federal", "En virtud de las negociaciones parlamentarias", "En el marco del proceso legislativo", "A partir del debate democrático", "Ante las demandas de la ciudadanía", "Con el avance de las reformas institucionales", "En observancia de la representación democrática", "Conforme a los principios de soberanía popular", "Durante las sesiones deliberativas del pleno"]
        },
        "technology": {
            "n_ms": [
                "modelo estructural", "desarrollo tecnológico", "plan estratégico", "diseño de negocio",
                "marco conceptual", "pipeline de integración", "dashboard analítico", "algoritmo predictivo",
                "servidor distribuido", "grafo de conocimiento", "modelo de lenguaje", "banco de datos vectorial",
                "procesamiento asíncrono", "pipeline de telemetría", "balanceador de carga", "cluster de orquestación",
                "protocolo de red"
            ],
            "n_fs": [
                "gobernanza corporativa", "disrupción tecnológica", "metodología ágil", "transformación digital",
                "sinergia organizacional", "arquitectura de microservicios", "inteligencia predictiva",
                "infraestructura en la nube", "tolerancia a fallos", "latencia de red", "autenticación multifactor",
                "arquitectura dirigida por eventos", "computación cuántica", "observabilidad de sistemas"
            ],
            "n_mp": [
                "flujos de trabajo", "cuellos de botella", "mecanismos de control", "sistemas heredados",
                "requisitos no funcionales", "motores de crecimiento", "microservicios escalables",
                "grafos de conocimiento", "bancos de datos vectoriales", "balanceadores de carga",
                "entornos de contenedores"
            ],
            "n_fp": [
                "actividades operativas", "metas estratégicas", "herramientas tecnológicas", "soluciones corporativas",
                "capacidades analíticas", "arquitecturas distribuidas", "redes neuronales convolucionales",
                "tuberías de CI/CD", "colas de mensajería"
            ],
            "adj_ms": [" resiliente", " adaptativo", " sostenible", " disruptivo", " optimizado", " escalable", " innovador", " orientado a datos", " asíncrono", " desacoplado", " autoescalable", " distribuido"],
            "adj_fs": [" resiliente", " adaptativa", " sostenible", " disruptiva", " optimizada", " escalable", " innovadora", " orientada a datos", " asíncrona", " desacoplada", " autoescalable", " distribuida"],
            "adj_mp": [" resilientes", " adaptativos", " sostenibles", " disruptivos", " optimizados", " escalables", " asíncronos", " desacoplados", " autoescalables", " distribuidos"],
            "adj_fp": [" resilientes", " adaptativas", " sostenibles", " disruptivas", " optimizadas", " escalables", " asíncronas", " desacopladas", " autoescalables", " distribuidas"],
            "v_trans_s": ["exige ", "obliga ", "impulsa ", "optimiza ", "viabiliza ", "sustenta ", "desbloquea ", "despliega ", "orquesta ", "contenedoriza ", "desacopla ", "sincroniza ", "indexa "],
            "v_trans_p": ["exigen ", "obligan ", "impulsan ", "optimizan ", "viabilizan ", "sustentan ", "desbloquean ", "despliegan ", "orquestan ", "contenedorizan ", "desacoplan ", "sincronizan ", "indexan "],
            "v_intrans_s": ["evoluciona continuamente", "progresa rápidamente", "se consolida en el mercado", "genera valor de largo plazo", "garantiza alta disponibilidad del clúster", "optimiza el rendimiento del sistema", "mantiene la consistencia eventual"],
            "v_intrans_p": ["evolucionan continuamente", "progresan rápidamente", "se consolidan en el mercado", "generan valor de largo plazo", "garantizan alta disponibilidad del clúster", "optimizan el rendimiento del sistema", "mantienen la consistencia eventual"],
            "circ": ["Con el surgimiento de las arquitecturas en la nube", "A través de la adopción de metodologías ágiles", "Con la aceleración de la automatización digital y la IA", "En el contexto de sistemas distribuidos", "Ante la rápida evolución de la ingeniería de software", "Con foco en la escalabilidad y resiliencia", "A partir de la modernización de sistemas heredados", "Con la integración continua de despliegues", "Bajo la perspectiva de la seguridad informática", "Frente a la constante disrupción tecnológica", "Con la orquestación distribuida de microservicios"]
        }
    },
    "fr": {
        "business": {
            "n_ms": [
                "plan stratégique", "plan d'affaires", "flux de trésorerie", "retour sur investissement",
                "positionnement sur le marché", "conseil d'administration", "équilibre financier", "accord commercial",
                "budget opérationnel", "capital d'exploitation", "développement pérenne", "rendement corporatif",
                "bilan comptable", "coût d'acquisition", "bénéfice d'exploitation", "passif éventuel",
                "fonds de garantie", "pacte d'actionnaires", "ebitda ajusté", "plan de continuité"
            ],
            "n_fs": [
                "stratégie d'entreprise", "gestion des risques", "marge bénéficiaire", "gouvernance d'entreprise",
                "valeur ajoutée", "synergie opérationnelle", "rentabilité financière", "prise de décision",
                "croissance durable", "audit comptable", "due diligence", "évaluation patrimoniale",
                "gouvernance ESG", "liquidité générale", "gestion d'actifs"
            ],
            "n_mp": [
                "indicateurs financiers", "principaux actionnaires", "actifs stratégiques", "résultats d'exploitation",
                "plans de continuité", "marchés émergents", "fonds d'investissement", "coûts de structure",
                "apports en capital", "rapports d'audit", "dividendes distribués", "investissements stratégiques"
            ],
            "n_fp": [
                "orientations stratégiques", "opportunités de marché", "projections financières", "alliances commerciales",
                "structures de capital", "décisions managériales", "provisions pour risques", "obligations fiscales",
                "prévisions budgétaires"
            ],
            "adj_ms": [" stratégique", " corporatif", " financier", " rentable", " compétitif", " opérationnel", " scalable", " commercial", " fiduciaire", " consolidé", " auditable"],
            "adj_fs": [" stratégique", " corporative", " financière", " rentable", " compétitive", " opérationnelle", " scalable", " commerciale", " fiduciaire", " consolidée", " auditable"],
            "adj_mp": [" stratégiques", " corporatifs", " financiers", " rentables", " compétitifs", " opérationnels", " scalables", " fiduciaires", " consolidés"],
            "adj_fp": [" stratégiques", " corporatives", " financières", " rentables", " compétitives", " opérationnelles", " scalables", " fiduciaires", " consolidées"],
            "v_trans_s": ["maximise ", "stimule ", "optimise ", "consolide ", "dynamise ", "viabilise ", "structure ", "mitige ", "alloue ", "audite ", "capitalise ", "diversifie "],
            "v_trans_p": ["maximisent ", "stimulent ", "optimisent ", "consolident ", "dynamisent ", "viabilisent ", "structurent ", "mitigent ", "allouent ", "auditent ", "capitalisent ", "diversifient "],
            "v_intrans_s": ["maximise le retour sur investissement", "assure la solidité financière", "renforce le positionnement sur le marché", "génère de la valeur à long terme", "maximise les flux de trésorerie", "pérennise la croissance de l'entreprise"],
            "v_intrans_p": ["maximisent le retour sur investissement", "assurent la solidité financière", "renforcent le positionnement sur le marché", "génèrent de la valeur à long terme", "maximisent les flux de trésorerie", "pérennisent la croissance de l'entreprise"],
            "circ": ["Dans le contexte économique contemporain", "Face aux nouvelles exigences du marché", "En raison de la compétitivité accrue", "Sous l'angle de la gouvernance d'entreprise", "Compte tenu des nouveaux défis stratégiques", "Sans perdre de vue les objectifs à court terme", "Dans une optique de création de valeur durable", "Face à l'évolution des normes de conformité", "Dans un souci d'excellence opérationnelle", "Lors de l'évaluation du retour sur investissement", "Sous le contrôle strict de l'audit indépendant"]
        },
        "ecology": {
            "n_ms": [
                "crédit carbone", "biome fragile", "écosystème durable", "impact écologique",
                "aménagement forestier", "développement durable", "bilan carbone", "cycle énergétique",
                "habitat naturel", "corridor écologique", "service écosystémique", "capital naturel",
                "cycle biogéochimique", "plan de conservation", "stock de biomasse"
            ],
            "n_fs": [
                "transition énergétique", "empreinte carbone", "biodiversité préservée", "conservation environnementale",
                "économie circulaire", "neutralité climatique", "gestion des déchets", "durabilité écologique",
                "évaluation d'impact environnemental", "connectivité écologique", "zone de protection environnementale",
                "action anthropique", "analyse du cycle de vie", "résilience climatique", "compensation écologique"
            ],
            "n_mp": [
                "ressources naturelles", "écosystèmes locaux", "indicateurs environnementaux", "crédits carbone",
                "habitats protégés", "déchets valorisés", "services écosystémiques", "corridors écologiques",
                "puits de carbone", "processus écologiques"
            ],
            "n_fp": [
                "énergies renouvelables", "cibles de décarbonation", "politiques environnementales", "zones protégées",
                "pratiques durables", "émissions de gaz à effet de serre", "mesures d'atténuation", "espèces indigènes",
                "réserves naturelles"
            ],
            "adj_ms": [" durable", " écologique", " bas carbone", " renouvelable", " écoresponsable", " biodégradable", " bioclimatique", " régénératif", " hydrologique", " conservationniste"],
            "adj_fs": [" durable", " écologique", " bas carbone", " renouvelable", " écoresponsable", " biodégradable", " bioclimatique", " régénérative", " hydrologique", " conservationniste"],
            "adj_mp": [" durables", " écologiques", " bas carbone", " renouvelables", " écoresponsables", " bioclimatiques", " régénératifs"],
            "adj_fp": [" durables", " écologiques", " bas carbone", " renouvelables", " écoresponsables", " bioclimatiques", " régénératives"],
            "v_trans_s": ["préserve ", "atténue ", "régénère ", "décarbonise ", "conserve ", "restaure ", "protège ", "reboise ", "équilibre ", "neutralise "],
            "v_trans_p": ["préservent ", "atténuent ", "régénèrent ", "décarbonisent ", "conservent ", "restaurent ", "protègent ", "reboisent ", "équilibrent ", "neutralisent "],
            "v_intrans_s": ["favorise la neutralité climatique", "réduit l'impact environnemental", "renforce la biodiversité", "garantit l'équilibre écologique", "restaure l'intégrité du paysage", "préserve les ressources hydriques", "renforce la résilience écologique"],
            "v_intrans_p": ["favorisent la neutralité climatique", "réduisent l'impact environnemental", "renforcent la biodiversité", "garantissent l'équilibre écologique", "restaurent l'intégrité du paysage", "préservent les ressources hydriques", "renforcent la résilience écologique"],
            "circ": ["Face aux défis du changement climatique", "Dans le cadre de la préservation environnementale", "Avec l'accélération de la transition écologique", "Sous l'angle de la protection des biomes", "À partir des évaluations d'impact environnemental", "En visant la régénération des écosystèmes", "Conformément aux engagements de durabilité", "Face au déclin de la biodiversité", "Grâce au suivi continu des habitats naturels", "Guidé par les objectifs de décarbonation", "En accord avec les cibles climatiques"]
        },
        "law": {
            "n_ms": [
                "respect du droit", "ordre juridique", "litige judiciaire", "cadre réglementaire",
                "avis juridique", "vice de forme", "recours contentieux", "jugement rendu",
                "dispositif légal", "pourvoi en cassation", "effet suspensif", "manquement contractuel",
                "préjudice moral", "lien de causalité", "principe du contradictoire", "contrôle juridictionnel"
            ],
            "n_fs": [
                "jurisprudence établie", "sécurité juridique", "norme constitutionnelle", "procédure judiciaire",
                "présomption d'innocence", "mesure conservatoire", "décision définitive", "autorité de la chose jugée",
                "inconstitutionnalité matérielle", "compétence juridictionnelle", "responsabilité civile",
                "action récursoire", "assignation en justice"
            ],
            "n_mp": [
                "droits fondamentaux", "délais de recours", "précédents judiciaires", "textes de loi",
                "honoraires d'avocat", "actes juridiques", "moyens de droit", "tribunaux de grande instance",
                "actes authentiques"
            ],
            "n_fp": [
                "garanties constitutionnelles", "règles de droit", "décisions interlocutoires", "mesures de sauvegarde",
                "prétentions juridiques", "obligations contractuelles", "garanties procédurales", "présomptions légales"
            ],
            "adj_ms": [" juridique", " constitutionnel", " procédural", " contraignant", " incontestable", " jurisprudentiel", " rescisoire", " exécutoire", " impératif"],
            "adj_fs": [" juridique", " constitutionnelle", " procédurale", " contraignante", " incontestable", " jurisprudentielle", " rescisoire", " exécutoire", " impérative"],
            "adj_mp": [" juridiques", " constitutionnels", " procéduraux", " contraignants", " incontestables", " exécutoires", " impératifs"],
            "adj_fp": [" juridiques", " constitutionnelles", " procédurales", " contraignantes", " incontestables", " exécutoires", " impératives"],
            "v_trans_s": ["fonde ", "confirme ", "clarifie ", "prescrit ", "réglemente ", "garantit ", "défend ", "annule ", "homologue ", "invalide ", "adjuge "],
            "v_trans_p": ["fondent ", "confirment ", "clarifient ", "prescrivent ", "réglementent ", "garantissent ", "défendent ", "annulent ", "homologuent ", "invalident ", "adjugent "],
            "v_intrans_s": ["garantit la sécurité juridique", "préserve le procès équitable", "respecte la constitution", "consolide la jurisprudence", "assure le respect des droits de la défense", "lie les instances judiciaires"],
            "v_intrans_p": ["garantissent la sécurité juridique", "préservent le procès équitable", "respectent la constitution", "consolident la jurisprudence", "assurent le respect des droits de la défense", "lient les instances judiciaires"],
            "circ": ["À la lumière de l'ordre juridique en vigueur", "Sous le contrôle de constitutionnalité", "Au vu de la jurisprudence constante", "Dans le respect du procès équitable", "Dans le cadre de l'instruction judiciaire", "Sur le fondement des principes généraux du droit", "En vertu des dispositions légales applicables", "Conformément aux décisions de justice", "Sous la juridiction compétente", "Garantissant les droits fondamentaux", "Au regard du principe du contradictoire"]
        },
        "medicine": {
            "n_ms": [
                "diagnostic clinique", "protocole thérapeutique", "essai clinique", "marqueur biologique",
                "tableau clinique", "traitement préventif", "bilan biologique", "pronostic médical",
                "agent pathogène", "essai en double aveugle", "marqueur sérologique", "facteur de nécrose tumorale",
                "choc septique", "antibiogramme bactérien", "examen histopathologique", "profil pharmacocinétique",
                "cathétérisme cardiaque", "résultat clinique"
            ],
            "n_fs": [
                "thérapie ciblée", "pharmacovigilance", "démarche médicale", "anamnèse complète",
                "immunité cellulaire", "physiopathologie", "réponse immunitaire", "efficacité thérapeutique",
                "comorbidité associée", "thérapie adjuvante", "pharmacocinétique clinique", "incidence épidémiologique",
                "résistance microbienne", "intervention endovasculaire", "ventilation mécanique", "biopsie tissulaire",
                "immunothérapie cellulaire"
            ],
            "n_mp": [
                "essais cliniques", "marqueurs biologiques", "symptômes cliniques", "agents pathogènes",
                "paramètres physiologiques", "traitements palliatifs", "essais multicentriques", "facteurs de risque",
                "paramètres hémodynamiques", "signes précurseurs"
            ],
            "n_fp": [
                "réponses immunitaires", "thérapies innovantes", "interventions chirurgicales", "preuves scientifiques",
                "réactions secondaires", "comorbidités cliniques", "thérapies adjuvantes", "échantillons biologiques"
            ],
            "adj_ms": [" thérapeutique", " clinique", " prophylactique", " physiologique", " pathogène", " pluridisciplinaire", " asymptomatique", " épidémiologique", " immunologique", " adjuvant", " histopathologique"],
            "adj_fs": [" thérapeutique", " clinique", " prophylactique", " physiologique", " pathogène", " pluridisciplinaire", " asymptomatique", " épidémiologique", " immunologique", " adjuvante", " histopathologique"],
            "adj_mp": [" thérapeutiques", " cliniques", " prophylactiques", " physiologiques", " pathogènes", " pluridisciplinaires", " épidémiologiques", " immunologiques", " adjuvants"],
            "adj_fp": [" thérapeutiques", " cliniques", " prophylactiques", " physiologiques", " pathogènes", " pluridisciplinaires", " épidémiologiques", " immunologiques", " adjuvantes"],
            "v_trans_s": ["diagnostique ", "synthétise ", "atténue ", "réadapte ", "prescrit ", "stabilise ", "module ", "inhibe ", "induit ", "bloque ", "éradique "],
            "v_trans_p": ["diagnostiquent ", "synthétisent ", "atténuent ", "réadaptent ", "prescrivent ", "stabilisent ", "modulent ", "inhibent ", "induisent ", "bloquent ", "éradiquent "],
            "v_intrans_s": ["stimule la réponse immunitaire", "assure l'efficacité thérapeutique", "enraye l'évolution de la maladie", "garantit le rétablissement clinique", "stabilise les paramètres vitaux", "atténue la réponse inflammatoire", "rétablit l'homéostasie physiologique"],
            "v_intrans_p": ["stimulent la réponse immunitaire", "assurent l'efficacité thérapeutique", "enrayent l'évolution de la maladie", "garantissent le rétablissement clinique", "stabilisent les paramètres vitaux", "atténuent la réponse inflammatoire", "rétablissent l'homéostasie physiologique"],
            "circ": ["Dans le cadre de la médecine fondée sur les preuves", "Au vu du tableau clinique du patient", "Sur la base des essais cliniques randomisés", "Sous l'angle de la pharmacovigilance", "Dès la pose du diagnostic précoce", "Avec l'essor des thérapies innovantes", "Dans le respect des protocoles thérapeutiques", "Compte tenu de la réponse immunitaire observée", "Lors du suivi pronostique du patient", "En visant l'efficacité thérapeutique et la sécurité", "Sous surveillance hémodynamique continue"]
        },
        "mining": {
            "n_ms": [
                "traitement du minerai", "gisement exploitable", "plan d'extraction", "relevé géotechnique",
                "processus minéralurgique", "dépôt sédimentaire", "forage d'exploration", "conduit de résidus",
                "talus de fosse", "remblai amont", "remblai aval", "massif rocheux", "stéril minier",
                "empilement à sec", "piézomètre à corde vibrante", "essai triaxial", "procédé métallurgique"
            ],
            "n_fs": [
                "exploitation souterraine", "digue de résidus", "prospection géologique", "mine à ciel ouvert",
                "stabilité géotechnique", "remise en état du site", "galerie d'extraction", "foration rotative",
                "stabilité des talus", "récupération métallurgique", "gestion des résidus", "sécurité des barrages"
            ],
            "n_mp": [
                "résidus miniers", "paramètres géotechniques", "corps minéralisés", "gisements découverts",
                "procédés d'extraction", "concentrés minéraux", "talus rocheux", "massifs rocheux",
                "piézomètres de contrôle", "essais géomécaniques", "résidus filtrés"
            ],
            "n_fp": [
                "digues de retenue", "réserves prouvées", "structures géologiques", "roches encaissantes",
                "excavations minières", "zones d'exploitation", "bacs de décantation", "galeries souterraines"
            ],
            "adj_ms": [" minier", " géotechnique", " géologique", " extractif", " métallifère", " sédimentaire", " géomécanique", " piézométrique", " métallurgique"],
            "adj_fs": [" minière", " géotechnique", " géologique", " extractive", " métallifère", " sédimentaire", " géomécanique", " piézométrique", " métallurgique"],
            "adj_mp": [" miniers", " géotechniques", " géologiques", " extractifs", " sédimentaires", " géomécaniques", " piézométriques", " métallurgiques"],
            "adj_fp": [" minières", " géotechniques", " géologiques", " extractives", " sédimentaires", " géomécaniques", " piézométriques", " métallurgiques"],
            "v_trans_s": ["extrait ", "traite ", "cartographie ", "stabilise ", "optimise ", "fore ", "échantillonne ", "rehausse ", "assèche ", "consolide "],
            "v_trans_p": ["extraient ", "traitent ", "cartographient ", "stabilisent ", "optimisent ", "forent ", "échantillonnent ", "rehaussent ", "assèchent ", "consolident "],
            "v_intrans_s": ["augmente la récupération métallurgique", "garantit la stabilité géotechnique", "optimise le cycle d'exploitation", "valorise le gisement", "préserve l'intégrité physique du massif", "optimise le drainage de la fosse"],
            "v_intrans_p": ["augmentent la récupération métallurgique", "garantissent la stabilité géotechnique", "optimisent le cycle d'exploitation", "valorisent le gisement", "préservent l'intégrité physique du massif", "optimisent le drainage de la fosse"],
            "circ": ["Compte tenu des caractéristiques du massif rocheux", "Avec la progression du front de taille", "Sous l'angle de la sécurité des digues de résidus", "Dans le cadre du plan d'exploitation minière", "Grâce à une surveillance géotechnique continue", "En conformité avec la réglementation minière", "Au vu des études de stabilité de la fosse", "Avec une gestion rigoureuse des résidus miniers", "Dans le contexte de la réhabilitation des sites miniers", "Selon l'optimisation des teneurs de coupure", "Grâce à la piézométrie en temps réel"]
        },
        "politics": {
            "n_ms": [
                "pacte républicain", "processus législatif", "débat parlementaire", "scrutin électoral",
                "accord politique", "projet de loi", "dialogue social", "compromis partisan",
                "quorum de vote", "blocage parlementaire", "veto présidentiel", "vote de confiance",
                "rapport de commission", "plan pluriannuel", "règlement intérieur"
            ],
            "n_fs": [
                "représentation démocratique", "réforme institutionnelle", "coalition majoritaire",
                "politique publique", "diplomatie multilatérale", "souveraineté populaire", "assemblée générale",
                "commission d'enquête parlementaire", "mesure d'urgence", "sanction gouvernementale",
                "réforme fiscale", "diplomatie bilatérale", "concertation citoyenne"
            ],
            "n_mp": [
                "droits civiques", "accords bilatéraux", "débats publics", "mandats électifs",
                "partis politiques", "enjeux électoraux", "vetos présidentiels", "débats en séance plénière"
            ],
            "n_fp": [
                "politiques publiques", "reformas structurelles", "coalitions politiques", "orientations gouvernementales",
                "commissions parlementaires", "réformes constitutionnelles", "mesures gouvernementales"
            ],
            "adj_ms": [" parlementaire", " législatif", " démocratique", " institutionnel", " gouvernemental", " multipartite", " diplomatique", " pluriannuel", " républicain", " bicaméral"],
            "adj_fs": [" parlementaire", " législative", " démocratique", " institutionnelle", " gouvernementale", " multipartite", " diplomatique", " pluriannuelle", " républicaine", " bicamérale"],
            "adj_mp": [" parlementaires", " législatifs", " démocratiques", " institutionnels", " gouvernementaux", " pluriannuels", " républicains", " bicaméraux"],
            "adj_fp": [" parlementaires", " législatives", " démocratiques", " institutionnelles", " gouvernementales", " pluriannuelles", " républicaines", " bicamérales"],
            "v_trans_s": ["articule ", "promulgue ", "promut ", "débat ", "sanctionne ", "négocie ", "délibère ", "adopte ", "approuve ", "réglemente ", "amende "],
            "v_trans_p": ["articulent ", "promulguent ", "promuvent ", "débattent ", "sanctionnent ", "négocient ", "délibèrent ", "adoptent ", "approuvent ", "réglementent ", "amendent "],
            "v_intrans_s": ["renforce la légitimité démocratique", "favorise la stabilité institutionnelle", "garantit la participation citoyenne", "facilite le consensus politique", "garantit la gouvernance républicaine", "pérennise le pacte social"],
            "v_intrans_p": ["renforcent la légitimité démocratique", "favorisent la stabilité institutionnelle", "garantissent la participation citoyenne", "facilitent le consensus politique", "garantissent la gouvernance républicaine", "pérennisent le pacte social"],
            "circ": ["Dans le paysage politique actuel", "Lors des débats et délibérations parlementaires", "Sous l'angle du pacte républicain", "Compte tenu des négociations au sein de la coalition", "Dans le cadre du processus législatif", "À l'issue du débat démocratique", "En réponse aux attentes citoyennes", "Avec la progression des réformes institutionnelles", "Dans le respect de la souveraineté populaire", "Conformément aux principes démocratiques", "Pendant les séances plénières délibératives"]
        },
        "technology": {
            "n_ms": [
                "modèle architectural", "développement logiciel", "système distribué", "pipeline de déploiement",
                "tableau de bord prédictif", "algorithme d'apprentissage", "serveur applicatif",
                "graphe de connaissances", "modèle de langage", "moteur d'inférence", "pipeline de télémétrie",
                "équilibreur de charge", "cluster d'orchestration", "protocole réseau"
            ],
            "n_fs": [
                "gouvernance des données", "disruption numérique", "méthode agile", "transformation digitale",
                "architecture de microservices", "intelligence artificielle", "infrastructure cloud",
                "tolérance aux pannes", "latence réseau", "authentification multifacteur", "architecture orientée événements",
                "observabilité des systèmes", "infrastructure déclarative"
            ],
            "n_mp": [
                "flux de données", "goulots d'étranglement", "systèmes patrimoniaux", "environnements conteneurisés",
                "microservices distribués", "clusters de calcul", "graphes de connaissances", "équilibreurs de charge",
                "pipelines de données"
            ],
            "n_fp": [
                "applications web", "solutions logicielles", "capacités analytiques", "infrastructures hybrides",
                "architectures événementielles", "chaînes d'intégration continue", "files d'attente distribuées"
            ],
            "adj_ms": [" résilient", " adaptatif", " cloud-native", " disruptif", " conteneurisé", " scalable", " innovant", " orienté données", " asynchrone", " découplé", " déterministe"],
            "adj_fs": [" résiliente", " adaptative", " cloud-native", " disruptive", " conteneurisée", " scalable", " innovante", " orientée données", " asynchrone", " découplée", " déterministe"],
            "adj_mp": [" résilients", " adaptatifs", " cloud-natives", " disruptifs", " conteneurisés", " scalables", " asynchrones", " découplés"],
            "adj_fp": [" résilientes", " adaptatives", " cloud-natives", " disruptives", " conteneurisées", " scalables", " asynchrones", " découplées"],
            "v_trans_s": ["exige ", "pilote ", "stimule ", "optimise ", "sécurise ", "déploie ", "orchestre ", "accélère ", "conteneurise ", "découple ", "synchronise ", "indexe "],
            "v_trans_p": ["exigent ", "pilotent ", "stimulent ", "optimisent ", "sécurisent ", "déploient ", "orchestrent ", "accélèrent ", "conteneurisent ", "découplent ", "synchronisent ", "indexent "],
            "v_intrans_s": ["évolue en continu", "progresse à grande échelle", "se standardise sur le marché", "réduit la latence opérationnelle", "garantit la haute disponibilité du cluster", "maintient la cohérence éventuelle"],
            "v_intrans_p": ["évoluent en continu", "progressent à grande échelle", "se standardisent sur le marché", "réduisent la latence opérationnelle", "garantissent la haute disponibilité du cluster", "maintiennent la cohérence éventuelle"],
            "circ": ["Avec l'émergence des technologies cloud", "Grâce à l'adoption des méthodes agiles", "Avec l'accélération de l'automatisation et de l'IA", "Dans le contexte des architectures distribuées", "Face à l'évolution du génie logiciel", "En privilégiant la résilience et la scalabilité", "À travers la modernisation des systèmes patrimoniaux", "Avec des pipelines d'intégration et de déploiement continus", "Sous l'angle de la cybersécurité", "Face aux disruptions technologiques continues", "Grâce à l'orchestration distribuée des microservices"]
        }
    },
    "la": {
        "business": [
            "Negotiatio honesta et prudentia commercialis divitias civitatum stabiliunt.",
            "Consilium directivum prudenter opes et rationes societatis dispensat.",
            "Fides mercatorum et claritas pactorum fundamentum totius commercii constituunt.",
            "Lucrum iustum et aequum ex solido labore et providentia nascitur.",
            "Societates mercatoriae per maria et terras utilitatem publicam propagant.",
            "Aerarium publicum et privatae rationes accurate computatae stabilitatem praestant.",
            "Pacta conventa sine dolo malo semper servari oportet inter negotiatores.",
            "Prudentia in sumptibus et diligentia in operibus prosperitatem diuturnam efficiunt."
        ],
        "ecology": [
            "Natura inest in mentibus nostris ad conservandum omne genus animantium et herbarum.",
            "Rerum naturae cognitio pacem animo adferat et terrarum orbis salutem conservat.",
            "Elementa mundi, ignis, aqua, aer et terra, perpetuo in se recurrunt et renovantur.",
            "Sol et ventus aeternas vires praebent quibus terrae pulchritudo sustinetur.",
            "Arbores silvarum et flumina pura vitam cunctis creaturis generosis largiuntur.",
            "Conservatio terrarum et marium officium hominis sapientis semper fuit.",
            "Ecosystema terrae in concordia et stabili temperantia naturae consistit.",
            "Vires naturae in exhausto fonte renovationis perpetuae redundantes rurgent."
        ],
        "law": [
            "Jurisprudentia est divinarum atque humanarum rerum notitia, iusti atque iniusti scientia.",
            "Iustitia est constans et perpetua voluntas ius suum cuique tribuendi.",
            "Juris praecepta sunt haec: honeste vivere, alterum non laedere, suum cuique tribuere.",
            "Salus populi suprema lex esto et in omnibus iudiciis aequitas servetur.",
            "Nullum crimen, nulla poena sine praevia lege scripta et stricta.",
            "Pacta sunt servanda et fides publica in contractibus semper custodiri debet.",
            "In dubio pro reo iudicandum est et praesumptio innocentiae custodiri oportet.",
            "Audiatur et altera pars antequam iudex sententiam finalem pronuntiet."
        ],
        "medicine": [
            "Sanitas est status secundum naturam et omnium corporis partium compositio harmonica.",
            "Primum non nocere et aegroto salutem semper consilio ac studio adferre.",
            "Medicina est ars curationis quae mentem et corpus pariter confortat et sanat.",
            "Cibus sit medicina tua et medicina sit cibus tuus in omni vita.",
            "Contagionum causa in parvis corpusculis latet quae aere et aqua pervagantur.",
            "Diagnosis praevia et cura sedula morbos gravissimos saepe avertunt.",
            "Anamnesis diligens et observatio signorum vitalium praesidium vitae praebent.",
            "Pharmacopolia et herbae medicinales aegrotantium dolores celeriter leniunt."
        ],
        "mining": [
            "Metalla ex intimis terrae visceribus arte et labore hominum eruuntur.",
            "Aurum, argentum et ferrum in venis montium abscondita ad usum civitatum extrahuntur.",
            "Geometria et mechanica in fodinis regendis et concavitatibus sustinendis necessariae sunt.",
            "Lapides pretiosi et mineralia varia varietates naturae mirabiles demonstrant.",
            "Montes excavantur ut materiae valentes ad aedificia et instrumenta fabricanda reperiantur.",
            "Terrae opes cum cautione et ratione effodiendae sunt ut futuram posteritatem adiuvent.",
            "Venae orichalci et aeris in cavis saxosis inventae divitias urbibus adferunt.",
            "Securitas fossorum in cuniculis subterraneis semper prima cura praefecti esto."
        ],
        "politics": [
            "Res publica est res populi, cum bene ac iuste geritur a magistratibus prudentibus.",
            "Concordia parvae res crescunt, discordia maximae dilabuntur in civitate.",
            "Leges breves esse oportet ut ab omnibus civibus facilius teneantur et observentur.",
            "Libertas est potestas faciendi id quod iure licet et nemini servire.",
            "Populi imperium et senatus auctoritas in republica moderata consentire debent.",
            "Publica utilitas privatis commodis semper anteponenda est in consiliis urbis.",
            "Civitas bene ordinata pacem et prosperitatem cunctis incolis pariter praestat.",
            "Oratoris facultas et consilium senatorium libertatem reipublicae defendunt."
        ],
        "technology": [
            "Ars et scientia in machinis construendis humanam potentiam ultra fines auferunt.",
            "Firmitas, utilitas et venustas in omnibus operibus architecturalibus servandae sunt.",
            "Automata et instrumenta mechanica labores graves hominum levant et accelerant.",
            "Ratio numerorum et figurae geometricae fundamentum totius artis ingeniariae constituunt.",
            "Inventionum novarum usus vias novas ad prosperitatem civitatum aperit.",
            "Scientia et usus in unum collati miracula opera in terris perficiunt.",
            "Aquaelia et structurae hydraulicis ratione exquisita urbium aquam dispensant.",
            "Machinationes novae et rotae versatiles celeritatem operum summopere augent."
        ]
    }
}
