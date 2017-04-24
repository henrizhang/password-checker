def meetsThreshold(p):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "1234567890"
    return True in [x in lower for x in p] and True in [x in upper for x in p] and True in [x in digits for x in p]

def strength(p):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "1234567890"
    other = ".?!&#,;:-_*"
    stregnth=0
    hasLower=0
    hasUpper=0
    hasSpecial=0
    hasDigit=0
    if len([x in lower for x in p])>0:
        hasLower=1
    if len([x in upper for x in p])>0:
        hasUpper=1
    if len([x in other for x in p])>0:
        hasSpecial=1
    if len([x in digits for x in p])>0:
        hasDigit=1
    return (hasLower+hasUpper+hasSpecial+hasDigit)*len(p)

print meetsThreshold("skrrrt")
print meetsThreshold("skrtS1")
print strength("skrtS1")
print strength("skr!.?t1212312S1")