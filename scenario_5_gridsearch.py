from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

def tune_model(X_train, y_train):
    model = RandomForestClassifier(random_state=42)
    params = {
        "max_depth": [3, 5, 7],
        "n_estimators": [50, 100]
    }
    grid = GridSearchCV(model, params, cv=5, scoring="accuracy")
    grid.fit(X_train, y_train)
    return grid.best_params_, grid.best_score_
