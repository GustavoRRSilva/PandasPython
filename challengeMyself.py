"""
---

## 🔹 Exercícios básicos (exploração inicial)

1. **Primeiras e últimas linhas**

   * Mostre as 5 primeiras linhas da coluna `bedrooms`.
   * Mostre as 8 últimas linhas.

2. **Valores únicos**

   * Liste todos os valores únicos de `bedrooms`.
   * Quantos valores diferentes existem (incluindo valores nulos)?

3. **Contagem de valores**

   * Descubra qual número de quartos aparece com mais frequência.
   * Mostre a contagem em ordem crescente.

---

## 🔹 Exercícios intermediários

4. **Maiores e menores valores**

   * Mostre os 10 maiores valores de `bedrooms`.
   * Mostre os 10 menores valores, mantendo duplicatas.

5. **Análise combinada (dataset houses)**

   * Encontre as 10 casas com mais quartos **e** mais banheiros.
   * O que você percebe nesses dados?

6. **Exploração de dados Netflix**

   * Mostre apenas as colunas `title` e `rating`.
   * Gere estatísticas descritivas para a coluna `rating`.

---

## 🔹 Exercícios de interpretação

7. **Padrões nos dados**

   * Qual é o número mais comum de quartos?
   * Existem valores estranhos (ex: casas com 0 quartos ou muitos quartos)?

8. **Distribuição**

   * A maioria das casas tem poucos ou muitos quartos?
   * Os dados parecem equilibrados ou concentrados?

9. **Netflix insights**

   * Qual o rating médio?
   * Existe muita variação nos ratings?

---

## 🔹 Desafio 🔥

10. Combine tudo:

* Pegue as 10 casas com mais quartos.
* Veja a frequência desses valores.
* Compare com os 10 menores valores.
* Escreva uma conclusão sobre a distribuição de `bedrooms`.

---

Se quiser, posso também:

* corrigir suas respostas
* ou transformar isso em um mini-projeto com dataset real 📊
"""

import pandas as pd 

houses = pd.read_csv("data/kc_house_data.csv")
bedrooms = houses["bedrooms"]

#1
#print(bedrooms.head(5))
#print(bedrooms.tail(8))

#2
#print(bedrooms.nunique())
#print(bedrooms.nunique(dropna=False))

#3
#print(bedrooms.value_counts(ascending=False))

#4
print(bedrooms.nlargest(10))
print(bedrooms.nsmallest(10,keep='all'))