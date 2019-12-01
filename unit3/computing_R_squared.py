

"""See Ch. 15 Figure 15.5
"""

def rSquared(measured, predicted):
    """Assumes measured a one-dimensional array of measured values
               predicted a one-dimensional array of predicted values
        
    Returns:
        Coefficient of determination
    """
    estimationError = ((predicted - measured) ** 2).sum()
    meanOfMeasured = measured.sum()/float(len(measured))
    variability = ((measured - meanOfMeasured) ** 2).sum()
    return 1 - estimationError/variability
