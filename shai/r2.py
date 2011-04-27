
# Data block
## Raw data
#   Genres          # strings
K = 'ttttftfftfttffffftftftfffftttfffftfffftttfttfttfftffttfttttftftttttttfftfftftffttttfttfttttftttftftf'
L = 'ttttfftftfttffffttftftftfttftffffttftfftfftttttfffffttfttttttftttttttfftfftftffttttfttfttttftttftftt'
M = 'fftt--.--.ttf.ffttftftftftt.tfff.ttftf.t.ft--ttfffffttftttt-tftttttttfftfftftffttttfttftttt.ttt.tftt'
N = 'ttttftfftfftffftftftftftfttftftfftfffffttftftttfffffttfttttttftttttttfftfftftffttttfttfttttffttftftt'
P = 'ttttftfftfttffffttftftffftttfftfftfffffttfttfttfftffttfttttttftttttttfftfftftffttttfttfttttftttftftt'
R = 'ttttttfttfftffffftftftftftfttftfftfftftftftftttfttfftffttttttftttttttfftfftftfttttttttftttttftfftttt'

rlenG = range(len(K))
rnumG = range(len(Genres))
trueChars = 't.'
GenreNames = list("KLMNPR")
## Data "accessors":
def BoolArrayFromString(s):
  res = []
  for i in rlenG:
    if s[i] in trueChars: res.append(True)
    else: res.append(False)
  return res
# def BoolArrayByGenreName(): # dict [[Bool]]
#   return

Genres = map (BoolArrayFromString, [K, L, M, N, P, R])

# Logic Block
## Calculate
### For each genre
#### That's what data block is for
### For each pair of genres
def QuadrupleCoefficientsFromPairOfGenres(a, b):
  A = [(    a[i]) and (    b[i]) for i in rlenG]
  B = [(not a[i]) and (    b[i]) for i in rlenG]
  C = [(    a[i]) and (not b[i]) for i in rlenG]
  D = [(not a[i]) and (not b[i]) for i in rlenG]
  return tuple(map(sum, (A, B, C, D)))

def Correlation(a, b, SignificantDigits=6, ReturnCoefficients=False):
  (A, B, C, D) = QuadrupleCoefficientsFromPairOfGenres(a, b)
  AD = A*D
  BC = B*C
  if ReturnCoefficients: return A, B, C, D, round( float(AD-BC) / float(AD+BC), SignificantDigits)
  return round(float(AD-BC) / (AD+BC), SignificantDigits)
## Sort 
## Print
def tabulate(ReturnCoefficients=True):
  for i in rnumG:
    for j in rnumG[i+1:]:
      print GenreNames[j], GenreNames[i], Correlation(Genres[i], Genres[j], SignificantDigits=3), '\t' 
    
