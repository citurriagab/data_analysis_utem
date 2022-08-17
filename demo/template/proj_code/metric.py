"""
    metric.py: Implementar las funciones de métrica y evaluación
"""
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score


def metrica_accuracy(y_verdad, y_preds):
    """Métrica de clasificación Accuracy"""
    return accuracy_score(y_verdad, y_preds)


def metrica_f1score(y_verdad, y_preds, avg='micro'):
    """Métrica de clasificación F1-score"""
    return f1_score(y_verdad, y_preds, average=avg)
