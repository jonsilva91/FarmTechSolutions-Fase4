# 📊 Análise de Dados Agrícolas

## 🌾 Sobre o Projeto
Este projeto realiza a análise de dados de culturas agrícolas (soja e milho), processando informações de produtividade, insumos e condições climáticas utilizando **R e Python**. O código também se conecta a uma API meteorológica para obter previsões do tempo relevantes para a lavoura.

# Dados considerados para o desenvolvimento da aplicação em Python

Foi realizada uma extensa pesquisa sobre o cultivo de soja e milho, desde o manejo do solo até a manutenção da lavoura com aplicação de herbicidas, inseticidas e fungicidas, com suas respectivas frequências. Foram escolhidos milho e soja, pois são duas culturas que podem ser rotacionadas (no caso, utilizando milho safrinha, que é cultivado entre safras de soja).

Para o manejo do solo, há diferenças entre ambos os cultivos, principalmente devido à soja, pois esta é uma planta leguminosa e, portanto, realiza fixação biológica de nitrogênio. Assim, a planta se associa a bactérias que fixam o nitrogênio do ar, ofertando esse nutriente à planta.

Durante a pesquisa, foi constatada a necessidade de análise química do solo para adubação e, posteriormente, a consulta de uma tabela para a correta adubação do solo, que depende também da estimativa de produção, é necessário também uma análise física mas as intruções para isso podem ser incluídas em versões futuras.

### Exemplo de tabela no Python:

```python
def calcular_adubo_soja(produtividade, p_resina, k_trocavel):
    """Calcula a quantidade de adubo necessária com base na tabela de adubação."""
    # Tabela de recomendação de P2O5 (kg/ha) com base na produtividade esperada e P-resina (mg/dm³)
    tabela_p2o5 = {
        ("<2.0", (50, 40, 30, 20)),
        ("2.0-2.5", (60, 50, 40, 20)),
        ("2.5-3.0", (80, 60, 40, 20)),
        ("3.0-3.5", (90, 70, 50, 30)),
        (">3.5", (80, 50, 40, 0))
    }
    
    # Tabela de recomendação de K2O (kg/ha) com base no potássio trocável (mmolc/dm³)
    tabela_k2o = {
        ("<2.0", (60, 40, 20, 0)),
        ("2.0-2.5", (70, 50, 30, 20)),
        ("2.5-3.0", (70, 50, 50, 20)),
        ("3.0-3.5", (80, 60, 50, 30)),
        (">3.5", (80, 60, 60, 40))
    }
    
    # Encontrar valores correspondentes na tabela
    def encontrar_valor(tabela, produtividade):
        for chave, valores in tabela:
            if "-" in chave:
                lim_inf, lim_sup = map(float, chave.split("-"))
                if lim_inf <= produtividade <= lim_sup:
                    return valores
            elif "<" in chave and produtividade < float(chave[1:]):
                return valores
            elif ">" in chave and produtividade > float(chave[1:]):
                return valores
        return None
    
    valores_p2o5 = encontrar_valor(tabela_p2o5, produtividade)
    valores_k2o = encontrar_valor(tabela_k2o, produtividade)
    
    if not valores_p2o5 or not valores_k2o:
        print("Erro: Não foi possível encontrar os valores na tabela.")
        return
    
    # Selecionar a quantidade de P2O5 e K2O conforme os níveis de P-resina e K trocável
    p2o5_ha = valores_p2o5[0] if p_resina < 7 else valores_p2o5[1] if p_resina < 16 else valores_p2o5[2] if p_resina < 40 else valores_p2o5[3]
    k2o_ha = valores_k2o[0] if k_trocavel < 0.8 else valores_k2o[1] if k_trocavel < 1.5 else valores_k2o[2] if k_trocavel < 3.0 else valores_k2o[3]
    
    return p2o5_ha, k2o_ha
```

Para o milho, a função de adubação é obtida pela produtividade e a finalidade do cultivo, sendo grãos ou silagem.

### Exemplo de código Python:

```python
def calcular_adubo_milho(produtividade, tipo):
    """
    Calcula a quantidade de adubo necessária com base na produtividade esperada e no tipo de milho (grão ou silagem).
    """
    tabela_adubacao = {
        5:  {'grao': (120, 85, 31),  'silagem': (195, 105, 145)},
        10: {'grao': (240, 170, 61), 'silagem': (390, 210, 290)},
        15: {'grao': (360, 255, 92), 'silagem': (585, 315, 435)},
    }
    
    if produtividade not in tabela_adubacao:
        raise ValueError("Produtividade fora da faixa disponível (5-15 ton/ha).")
    if tipo not in ['grao', 'silagem']:
        raise ValueError("Tipo inválido. Use 'grao' ou 'silagem'.")
    
    return tabela_adubacao[produtividade][tipo]
```

Os dados foram considerados para o estado de **São Paulo**, pois outras tabelas deverão ser consultadas para diferentes regiões.

### Insumos e Defensivos
Foi previsto o uso de fungicida como insumo obrigatório, devido à riqueza de detalhes no manejo agrícola, levando em conta o tipo de semente transgênica, o espaçamento entre as plantas (esses dados foram inseridos de maneira fixa pois é uma recomendação da Embrapa para combate de ervas daninhas e consequente economia de herbicidas, sendo previsto a entrada de dados pelo usuário no futuro), tipos de pragas por insetos e tipos de pragas fúngicas, fase da planta V1-V7, se a aplicação é pós emergencial, etc. Foi optado o fungicida, pois são as doenças mais comuns enfrentadas nas lavouras, sendo ferrugem-asiática para soja e ferrugem do milho, geralmente de aplicação única segundo a bula.

Os dados de aplicação de fungicidas foram retirados de bulas comerciais listadas no Agrofit ([link](https://agrofit.agricultura.gov.br/agrofit_cons/principal_agrofit_cons)).

### Cálculos de Pulverização
Os cálculos de área são flexíveis e podem ser definidos pelo usuário a partir de figuras geométricas (retângulo, triângulo, trapézio ou círculo). Também há cálculos para pulverização, considerando dados de pulverizadores comerciais ([Stara](https://cdn.stara.com.br/institucional/uploads/products/prospecto/17-b_r__imperador_4000.pdf)).

### Exemplo:
\[
$\textbf{Largura da área tratada} = 40 \times 0.6 \text{ m} = 24 \text{ m}$
\]

\[
$\textbf{Área tratada} = \text{velocidade} \times \text{largura da área tratada}$
\]

\[
$200 \text{ m/min} \times 24 \text{ m} = 4800 \text{ m}^2/\text{min}$
\]

\[
$\text{Convertendo para hectares:} \quad \frac{4800}{10000} = 0.48 \text{ ha/min}$
\]


### Taxa de aplicação
A fórmula utilizada:

\[
$\text{Taxa de aplicação} = \frac{\text{Vazão total}}{\text{Área tratada}}$
\]


Exemplo:
\[
$\text{Taxa de aplicação} = \frac{32 \text{ L/min}}{0.48 \text{ ha/min}} = 67 \text{ L/ha}$
\]


### Quantidade de produto para o preparo da calda  

A quantidade de produto necessária é calculada pela fórmula:  

\[
$\text{Quantidade} = \frac{\text{Capacidade do tanque} \times \text{Dosagem do produto}}{\text{Taxa de aplicação}}$
\]

#### Exemplo  

Se o tanque tem **2000 litros** e a dosagem do produto é **0,2 L/ha**, o cálculo será:  

\[
$\text{Quantidade} = \frac{2000 \times 0.2}{67} = 5.97 \text{ L}$
\]

Ou seja, são necessários **5,97 litros de produto** para preparar a calda de um tanque cheio do pulverizador.  

O valor total de produto necessário pode ser obtido multiplicando esse resultado pela área total em hectares.  

### Cálculo de Semeadura  

Para o cálculo de semeadura é preciso saber o poder germinativo de cada semente, que varia com a variedade de planta:  

$$
nº \, de \, plantas/metro = \frac{\text{população de plantas/ha} \times \text{espaçamento} (m)}{10.000}
$$

Dessa forma, obtemos a taxa de semeadura e a quantidade de sementes por metro a ser utilizadas. O cálculo do número de plantas por metro linear a ser plantado na lavoura (***resultado do exemplo com 250000 plantas =*** 10 sementes/metro linear ):

$$
nº \, de \, plantas/metro = \frac{250000 \times 0.4}{10.000}
$$

E com o poder germinativo podemos ajustar esse valor:  

$$
nº \, de \, sementes/metro = \frac{nº \, de \, plantas/metro \times 100}{\% \, germinação}
$$

Em seguida, podemos calcular o número de sementes por hectare e o peso por hectare de sementes a ser utilizado na lavoura pelo estande desejado (foi utilizada uma previsão de 300.000 plantas/ha):  

$$
nº \, de \, sementes/hectare = \left( \frac{\text{estande desejado} \times 100}{\% \, germinação} \right) \times 1.1
$$

$$
nº \, de \, sementes/hectare = \left( \frac{300000 \times 100}{80} \right) \times 1.1
$$

O peso de 1000 grãos de soja é necessário para o cálculo da quantidade de quilos de sementes que iremos utilizar nas nossas lavouras. Existem variações nos pesos de 1000 grãos, de acordo com cada cultivar que pretendemos utilizar nas nossas áreas.  

Esses números, geralmente, ficam por volta de **140 g a 220 g** a cada 1000 grãos de soja e de **200 g a 500 g** de milho. Porém, como foi comentado, é vital saber exatamente o peso, de acordo com o híbrido, que iremos utilizar na nossa propriedade.  

#### Exemplo:

$$
Peso/ha = \frac{nº \, de \, sementes/hectare \times PMS}{1000}
$$

---

### Cálculo da Expectativa de Produtividade  

Foi utilizado dois métodos um para a Soja e o outro para o Milho. Referente à soja, o procedimento é o seguinte:  

1. Contar o número de vagens em 10 plantas consecutivas e dividir o resultado por 10  

   **Exemplo:** 10 plantas ao todo deram **200** vagens  
   - Média:  
   
   $\frac{200}{10} = 20 \text{ vagens/planta}$
   

2. Contar o número de grãos nas vagens e dividir pelo número de vagens  

   **Exemplo:** 60 vagens ao todo deram **150** grãos  
   - Média:  
   
   $\frac{150}{60} = 2.5 \text{ grãos/vagem}$
   

3. Olhar o peso de 1000 grãos para o híbrido utilizado  

   **Exemplo:** 200 g é o peso de 1000 grãos desse híbrido  

### Parâmetros do Cálculo:

- **Plantas por hectare:** 343.750 mil plantas  
- **Vagens por planta:** 20 vagens  
- **Grãos por vagem:** 2,5 grãos  
- **Peso de mil grãos:** 200 gramas  

A produtividade esperada pode ser calculada com a seguinte fórmula:  

$$
sc/ha = \frac{\text{plantas/ha} \times \text{vagens/planta} \times \text{grãos por vagem} \times \text{peso de mil grãos}}{60000}
$$

Aplicando os valores:  

$$
sc/ha = \frac{343750 \times 20 \times 2.5 \times 200}{60000}
$$

**Produtividade esperada: 57,29 sc/ha**  

#### Produtividade Milho


Para calcular a produtividade do milho, utilizamos a seguinte fórmula:  


$$
\text{produtividade} = \frac{\left( \frac{\mathrm{peso\_grãos}}{1000} \right) \times 60000}{1000}
$$


#### Exemplo:   

Suponha que o peso médio de 1000 grãos seja **185 g**. Aplicamos a fórmula:  


$\text{produtividade} = \frac{\left( \frac{185}{1000} \right) \times 60000}{1000}$



$\text{produtividade} = \frac{(0.185) \times 60000}{1000}$



$\text{produtividade} = \frac{11100}{1000} = 11.1 \, sc/ha$


Neste exemplo, a produtividade esperada do milho seria **11,1 sacas por hectare**.

---

## Cálculos a serem incluídos  

Podemos incluir além dos cálculos de outros tipos de pulverização como **inseticidas e herbicidas por fase da planta**, o cálculo de **ajuste de maquinário e tempo necessário de colheita**. Podemos utilizar **APIs** para obter dados reais de maquinário.  

Além disso, o cálculo de **lucratividade por tipo de lavoura** também poderá ser incluído no futuro.  


## Fontes Utilizadas  

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



## 📂 Estrutura do Repositório
```
.
├── R
│   ├── Analise_estatistica_previsao_metereologica.R
│   ├── Analise_estatistica_previsao_metereologica.html
│   ├── Analise_estatistica_previsao_metereologica.qmd
│   ├── Analise_estatistica_previsao_metereologica_files
│   │   ├── figure-html
│   │   │   ├── unnamed-chunk-16-1.png
│   │   │   ├── unnamed-chunk-17-1.png
│   │   │   └── unnamed-chunk-19-1.png
│   │   └── libs
│   ├── R.Rproj
├── README.md
├── __pycache__
│   ├── calculos.cpython-312.pyc
│   ├── dados.cpython-312.pyc
│   ├── interface.cpython-312.pyc
│   ├── validacao_dados.cpython-312.pyc
├── calculos.py
├── dados.py
├── data
│   └── dados.json
├── interface.py
├── main.py
└── validacao_dados.py
```

## 🔧 Instalação e Dependências
Para rodar o projeto, instale os pacotes necessários no **R**, em **python** foram usados apenas pacotes padrão:
```r
install.packages(c("jsonlite", "dplyr", "ggplot2", "openmeteo"))
library(jsonlite)
library(dplyr)
library(ggplot2)
library(openmeteo)
```
## 🌱 Como Funciona o Aplicativo em Python
O aplicativo permite gerenciar informações sobre culturas agrícolas, incluindo entrada, atualização e exclusão de dados, além de cálculos para adubação e aplicação de fungicidas. Ele funciona através de um menu interativo com as seguintes opções:

## 📌 Menu Principal

1. Entrada de dados
2. Saída de dados
3. Atualizar dados
4. Deletar dados
5. Sair

## 📊 Saída de Dados (Exemplo)

Ao escolher a **opção 2 - Saída de Dados**, o usuário visualiza detalhes das culturas cadastradas, incluindo área, espaçamento, densidade de sementes, taxa de semeadura e produtividade estimada. Além disso, são exibidos cálculos para **adubação** (quantidade de NPK por hectare e total para a lavoura) e para **aplicação de fungicidas.**

## ✅ Exemplo de saída:

[0] Cultura: Soja, Área: 100.00 hectares

   - Espaçamento: 40.0 cm entre plantas e linhas
   - Densidade: 12.00 sementes por metro linear
   - Produtividade: 68.75 sacas/hectare

   --- Insumos, Cálculos de Manejo ---
   Adubação:
      P2O5 total: 50.00 Kg/ha (5000.00 Kg no total)
      K2O total: 80.00 Kg/ha (8000.00 Kg no total)

   Fungicida: Aplicação de Morfolina
      Dosagem: 6.00 L por tanque
      Total a utilizar: 20.00 litros

## ✏️ Atualização de Dados

Na **opção 3 - Atualizar Dados**, o usuário pode modificar valores como **área da cultura, fertilidade do solo, estimativa de produção e dosagem de fungicidas.**
O programa solicita confirmação antes de recalcular valores críticos como **produtividade esperada.**

## ✅ Exemplo de atualização:

Digite o índice do dado a ser atualizado: 7

Atualizando dados para a cultura: soja
Novo P resina (mg/dm³) (Atual: 7.0): 
Novo K trocável (cmol/dm³) (Atual: 2.0): 
Nova estimativa de produção (t/ha) (Atual: 5.0): 


## 📊 Análises Realizadas em R
- **Cálculo de estatísticas básicas** (médias e desvios padrão de produtividade e insumos);
- **Visualização gráfica com `ggplot2`**;
- **Coleta de dados meteorológicos** via `openmeteo`;
- **Conversão de dados JSON** para análise.

## 🌦️ Dados Meteorológicos
Os dados climáticos são obtidos via API pública **Open-Meteo**. Para obter a previsão para os próximos 3 dias:
```r
previsao <- weather_forecast("São Paulo", 
                            daily = c("temperature_2m_max", "temperature_2m_min",
                                      "precipitation_sum", "wind_speed_10m_max",
                                      "sunshine_duration", "relative_humidity_2m_max"),
                            timezone = "America/Sao_Paulo")

cat("Previsão do tempo para os próximos 3 dias:\n")
previsao_3dias <- previsao[1:6, ]
for (i in 1:nrow(previsao_3dias)) {
  cat("\nData:", format(as.Date(previsao_3dias$date[i]), "%d/%m/%Y"), "\n")
  cat(" Temp. Máx:", previsao_3dias$daily_temperature_2m_max[i], "°C\n")
  cat(" Temp. Mín:", previsao_3dias$daily_temperature_2m_min[i], "°C\n")
  cat(" Precipitação:", previsao_3dias$daily_precipitation_sum[i], "mm\n")
  cat("Vento Máx:", previsao_3dias$daily_wind_speed_10m_max[i], "km/h\n")
  cat("Duração do Sol:", round((previsao_3dias$daily_sunshine_duration[i]/3600),2), "horas\n")
  cat("Umidade Máx:", previsao_3dias$daily_relative_humidity_2m_max[i], "%\n")
  cat("------------------------\n")
} 
```

## 📈 Exemplos de Visualização
### 🔹 **Boxplot de Produtividade**
```r
ggplot(dados, aes(x = cultura, y = produtividade, fill = cultura)) +
  geom_boxplot() +
  labs(title = "Distribuição da Produtividade por Cultura", 
       y = "Produtividade (ton/ha)", x = "Cultura") +
  theme_minimal()
```
![Boxplot de Produtividade](R/Analise_estatistica_previsao_metereologica_files/figure-html/unnamed-chunk-17-1.png)

## 🎥 Vídeo Demonstração

[![Assista ao vídeo](https://img.youtube.com/vi/SvARBqcmIGo/0.jpg)](https://youtu.be/SvARBqcmIGo)


## 🛠️ Futuras Melhorias
**python**
- [ ] Interface gráfica para facilitar a entrada e análise dos dados 📊
- [ ] Adição de mais insumos 🌾
- [ ] Exportação de relatórios em .csv ou .pdf 📄
- [ ] Integração com APIs meteorológicas para previsões do tempo  e tomada de decisão☁️🌡
- [ ] Cálculos e previsão de lucratividade 📈
- [ ] Suporte de outros insumos 🌾
- [ ] Cálculos para ajustes de maquinários 🚜

**R**
- [ ] Melhorar visualização dos dados com gráficos interativos 📊
- [ ] Adicionar mais variáveis meteorológicas 🌦️
- [ ] Implementar relatórios automáticos 📑

📌 **Autores:** Jonas Silva, João Severo e Renan Francisco.
