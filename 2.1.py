import pandas as pd 
heights = [188, 172, 187, 161, 183, 172, 185, 163, 173, 183, 174, 174, 175,
178, 183, 195, 178, 173, 174, 183, 174, 181, 162, 180, 170, 175, 182, 180, 183,
178, 182, 188, 175, 179, 184, 193, 182, 183, 175, 185, 182, 183, 156, 185, 199]
weights = [86, 71, 89, 64, 83, 71, 86, 68, 73, 84, 73, 72, 75, 78, 85, 93, 78,
70, 74, 80, 83, 82, 68, 80, 73, 78, 82, 81, 83, 79, 82, 86, 76, 77, 80, 103,
82, 83, 77, 89, 80, 85, 82, 85, 110]
ages = [58, 61, 54, 54, 58, 57, 63, 54, 37, 51, 34, 26, 50, 48, 45, 52, 56,
46, 54, 28, 52, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 32, 21, 62, 43, 55,
56, 61, 53, 22, 64, 45, 54, 47, 38] 
 
df = pd.DataFrame ({"heights" : heights, "weights" : weights, "ages" : ages})
#print (df)

print (df.loc[0:2])
print (df.loc[42:])