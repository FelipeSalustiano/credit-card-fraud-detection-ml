# Detecção de Fraude em Cartões de Crédito

Este projeto implementa um modelo de Machine Learning para detectar fraudes em transações de cartão de crédito, utilizando o dataset [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).

---

## Descrição

O objetivo é construir um classificador capaz de identificar transações fraudulentas em meio a um conjunto altamente desbalanceado, onde fraudes representam menos de 1% dos dados.

---

## Tecnologias Utilizadas

- Python 3
- Pandas, NumPy (manipulação de dados)
- Scikit-learn (modelagem e avaliação)
- Imbalanced-learn (SMOTE para balanceamento)
- Matplotlib (visualização)

---

## Passos do Projeto

1. **Carregamento e análise exploratória dos dados**
2. **Pré-processamento**: normalização dos dados e balanceamento com SMOTE
3. **Divisão dos dados** em treino e teste, mantendo proporção das classes
4. **Treinamento do modelo Random Forest** com dados balanceados
5. **Avaliação do modelo** usando métricas específicas para dados desbalanceados:
   - AUC-ROC
   - Recall
   - F1-score
6. **Análise da importância das features** (opcional)
7. **Salvamento do modelo treinado** para uso futuro
