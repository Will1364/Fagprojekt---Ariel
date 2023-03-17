@author: Christina Vejby Larsen
# DeltaBIC funktion
# Input: chi^2-fordelingen for henholdsvis den fittede model og for 
# en flad linje og n (antallet af datapunkter).
# Output: DeltaBIC (hvor godt dataen passser modellen ift. en flad linje)
def BIC(chi_anden_m,chi_anden_f,n)
    k = 20
    BIC_m = chi_anden_m + k*ln(n)
    BIC_f = chi_anden_f + k*ln(n)
    DeltaBIC = chi_anden_m - chi_anden_f
    return DeltaBIC

