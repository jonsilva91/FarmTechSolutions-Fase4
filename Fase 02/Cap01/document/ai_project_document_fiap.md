
<img src="../assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=30% height=30%>

# AI Project Document - Módulo 1 - FIAP



## FarmTech Solutions


#### Nomes dos integrantes do grupo

- Jonas Silva  
- João Severo  
- Renan Francisco

## Sumário

[1. Introdução](#c1)

[2. Visão Geral do Projeto](#c2)

[3. Desenvolvimento do Projeto](#c3)

[4. Resultados e Avaliações](#c4)

[5. Conclusões e Trabalhos Futuros](#c5)

[6. Referências](#c6)

[Anexos](#c7)

<br>

# <a name="c1"></a>1. Introdução

## 1.1. Escopo do Projeto

### 1.1.1. Contexto da Inteligência Artificial

A agricultura digital tem se beneficiado amplamente da Inteligência Artificial e tecnologias associadas para aumentar a produtividade e reduzir desperdícios. Nesse contexto, a FarmTech Solutions propõe uma aplicação orientada a dados para o agronegócio, com foco em sensoriamento de campo e tomada de decisão baseada em dados históricos e preditivos.

### 1.1.2. Descrição da Solução Desenvolvida

A solução consiste em um sistema de banco de dados relacional que coleta, armazena e processa informações de sensores instalados em plantações de diferentes culturas. O sistema permite o monitoramento contínuo do solo (umidade, pH, nutrientes), vinculando os dados a ações como aplicações de água e fertilizantes. Dessa forma, é possível ajustar a quantidade de recursos aplicados conforme a necessidade real da lavoura, promovendo economia e sustentabilidade.

# <a name="c2"></a>2. Visão Geral do Projeto

## 2.1. Objetivos do Projeto

Desenvolver um Modelo Entidade-Relacionamento (MER) e seu correspondente Diagrama Entidade-Relacionamento (DER) que sirvam de base para um sistema inteligente de coleta, análise e gestão de dados agrícolas, otimizando o uso de recursos e permitindo decisões mais assertivas na lavoura.

Além disso, foi desenvolvida uma aplicação em Python que simula a entrada e a manipulação dos dados relacionados à produção agrícola, incluindo funcionalidades para:

- Inserção, atualização e exclusão de dados das culturas;

- Cálculos agronômicos automatizados como adubação, densidade de plantio e aplicação de fungicidas;

- Leitura de dados estruturados via JSON;

- Interface de linha de comando com menu interativo para o produtor;

- Preparação da base de dados para futuras análises automatizadas.


## 2.2. Público-Alvo

Produtores rurais, cooperativas agrícolas, empresas de agritechs e consultores agronômicos que necessitam de automação e inteligência no campo.

## 2.3. Metodologia

A metodologia adotada neste projeto seguiu uma abordagem iterativa e orientada a dados, com as seguintes etapas:

- Análise do problema apresentado: Compreensão do contexto agrícola envolvendo sensores e tomada de decisão baseada em dados;

- Levantamento de requisitos e definição das regras de negócio: Identificação das entidades, relacionamentos, atributos e fluxos que representam a realidade da FarmTech Solutions;

- Modelagem conceitual (MER): Criação de um modelo entidade-relacionamento com base nas regras de negócio;

- Implementação visual do modelo relacional (DER): Modelagem no SQL Developer Data Modeler com definições de chaves primárias, estrangeiras e cardinalidades;

- Desenvolvimento de uma aplicação funcional em Python: Simulação prática do sistema com funcionalidades para inserção, atualização e visualização de dados agrícolas, incluindo cálculos automatizados de insumos;

- Estruturação do projeto no GitHub seguindo os padrões da FIAP: Organização em pastas específicas para código, documentos, imagens e configuração, garantindo rastreabilidade e clareza no desenvolvimento.

# <a name="c3"></a>3. Desenvolvimento do Projeto

## 3.1. Tecnologias Utilizadas

- SQL Developer Data Modeler – modelagem visual do DER

- Python + JSON – simulação de dados e estruturação de leitura para análise

- R + RStudio – visualização estatística dos dados simulados

- LaTeX + VSCode – documentação do MER e regras de negócio

- GitHub – versionamento e organização do projeto

## 3.2. Modelagem e Algoritmos

Não há modelo de IA implementado, mas o banco está preparado para uso futuro com modelos de regressão, análise temporal e predição.

## 3.3. Treinamento e Teste

Não se aplica neste módulo, pois o foco foi modelagem de dados. A futura aplicação de IA poderá ser feita com base nos dados históricos armazenados no banco.

# <a name="c4"></a>4. Resultados e Avaliações

## 4.1. Análise dos Resultados

O modelo desenvolvido cobre todas as necessidades funcionais levantadas:

- Representa com clareza os relacionamentos entre cultura, sensores e aplicações, com base nas regras de negócio levantadas;
- Permite integração entre dados de sensores automatizados e operadores humanos responsáveis por áreas de plantio;
- Está normalizado e preparado para escalabilidade, possibilitando a expansão futura para novas culturas, sensores e tratamentos;
- **Os testes realizados com a aplicação em Python demonstraram a viabilidade do sistema, permitindo ao usuário cadastrar culturas, estimar insumos agrícolas como fertilizantes e fungicidas, calcular produtividade e realizar atualizações e exclusões conforme necessário;**
- **Complementarmente, as análises estatísticas desenvolvidas em R possibilitaram visualizar a distribuição da produtividade por cultura, bem como calcular médias e desvios padrão de insumos utilizados por hectare, utilizando gráficos gerados com o pacote `ggplot2` e dados meteorológicos da API `openmeteo`;**
- Com esses resultados, foi possível validar que o modelo não apenas atende aos requisitos estruturais do banco de dados, como também serve de base sólida para sistemas reais de apoio à decisão na agricultura de precisão.

## 4.2. Feedback dos Usuários

Como o projeto ainda é conceitual, não houve testes com usuários finais, mas o modelo foi validado por membros da equipe com base em literatura técnica e recomendações da Embrapa.

# <a name="c5"></a>5. Conclusões e Trabalhos Futuros

O projeto atendeu aos objetivos propostos e criou uma base sólida para expansão futura. Trabalhos futuros incluem:

- Aplicação desenvolvida em Python e R  sobre os dados coletados

- Interface de entrada de dados web ou mobile

- Integração com APIs meteorológicas e de maquinário agrícola

- Modelagem conceitual e lógica do banco de dados

- Implementação de banco de dados

- Implementação de modelos de IA baseado nos dados coletados

- Dashboards com visualização dos indicadores em tempo real

# <a name="c6"></a>6. Referências


- **Embrapa – Tecnologias de Produção de Soja**  
  [Acesse aqui](https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/975595/1/SP16online.pdf)  

- **Embrapa – Manejo do Milho**  
  [Acesse aqui](https://www.embrapa.br/en/agencia-de-informacao-tecnologica/cultivos/milho/producao/manejo-do-solo-e-adubacao/adubacao-e-fertilidade-do-solo/exigencias-nutricionais-da-planta)  

- **Produção Agrícola**  
  [Como estimar a produtividade antes da colheita](https://blog.sensix.ag/como-estimar-a-produtividade-antes-da-colheita/#:~:text=Para%20estimar%20a%20produtividade%20por,%2C%2060.000%20gramas%20por%20saca).  

- **Produtividade do Milho**  
  [Acesse aqui](https://blog.aegro.com.br/producao-de-milho-por-hectare/)  

- **Fabricante Pulverizador STARA**  
  [Imperador 3000 e 4000](https://www.stara.com.br/produtos-servicos/maquinas-agricolas/pulverizadores-maquinas-agricolas/imperador-3000-e-4000#comparador)  

- **STARA 3000 – Dados Técnicos**  
  [Acesse aqui](https://cdn.stara.com.br/institucional/uploads/products/prospecto/17-b_r__imperador_4000.pdf)  

- **Agrofit**  
  [Acesse aqui](https://agrofit.agricultura.gov.br/agrofit_cons/principal_agrofit_cons)  

- **Embrapa – Espaçamento de Plantação**  
  [Acesse aqui](https://www.embrapa.br/en/agencia-de-informacao-tecnologica/cultivos/milho/producao/plantio/espacamento-e-densidade#:~:text=Dados%20de%20pesquisa%20mostram%20vantagens,densidades%20de%20plantio%20mais%20elevadas.)  

# <a name="c7"></a>Anexos

### 📘 MER (Modelo Entidade-Relacionamento)

- [📄 MER_farmtech.pdf](document/MER_farmtech.pdf)
- ![Diagrama MER](assets/MER.png)

### 📑 Regras de Negócio

- [📄 Regras_de_Negocio.pdf](document/Regras_de_Negocio.pdf)

### 🗂️ DER (Diagrama Entidade-Relacionamento)

- ![Diagrama DER](assets/diagrama_DER.png)
