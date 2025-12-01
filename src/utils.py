def train_predict_evaluate(x, y, model, train_step=True):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn import model_selection
    from sklearn import metrics

    x_train, x_test, y_train, y_test = model_selection.train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    if train_step:
        model.fit(x_train, y_train)

    pred = model.predict(x_test)

    reports = metrics.classification_report(y_test, pred)
    cm = metrics.confusion_matrix(y_test, pred)

    print("Reports:\n", reports)
    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Matriz de Confusão")
    plt.xlabel("Previsão")
    plt.ylabel("Valor Real")
    plt.show()

    return model
