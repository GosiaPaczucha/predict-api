def rule_based_prediction(num1, num2):
    if num1 is None:
        num1 = 0
    if num2 is None:
        num2 = 0

    total = num1 + num2

    if total > 5.8:
        prediction = 1
    else:
        prediction = 0

    return {
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2,
            "total": total
        }
    }

