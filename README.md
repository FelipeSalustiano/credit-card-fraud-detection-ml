# Detecção de Fraude em Cartões de Crédito

Este projeto implementa um modelo de Machine Learning para detectar fraudes em transações de cartão de crédito, utilizando o dataset [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).

---

## Descrição

O objetivo é construir um modelo capaz de identificar transações fraudulentas em meio a um conjunto altamente desbalanceado, onde fraudes representam menos de 1% dos dados.

---

## Tecnologias Utilizadas

- Python 3
- Pandas
- NumPy 
- Scikit-learn
- XGBoost
- LightGBM
- CatBoost 
- Matplotlib 
- Seaborn


---

## Passos do Projeto

1. **Carregamento e análise exploratória dos dados**
2. **Divisão dos dados** 
3. **Validação cruzada** 
4. **Treinamento do modelo CatBoost** 
5. **Avaliação do modelo** usando métricas específicas para dados desbalanceados:
   - Recall
   - Matriz de Confusão


---

## Estrutura do Projeto


| Pasta / Arquivo        | Descrição |
|------------------------|-----------|
| `notebook/`            | Notebooks de análise e modelagem |
| └── `analise.ipynb`    | Notebook principal do projeto |
| `src/`                 | Scripts auxiliares |
| └── `utils.py`         | Funções usadas no projeto |
| `README.md`            | Documentação do projeto 