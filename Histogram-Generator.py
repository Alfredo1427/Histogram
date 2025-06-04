import pandas as pd
import matplotlib.pyplot as plt
import io
from google.colab import files

#Uploader
uploaded = files.upload()
data = pd.read_csv(io.BytesIO(uploaded['1.csv']))

df = pd.DataFrame(data, columns=['Burner','Inlet Bed','PRESSURE'])

# Convert the 'Pressure' column to numeric, coercing errors to NaN
df2 = df.apply(pd.to_numeric, errors='coerce')

df2.describe()
df2.columns

print(df2.describe())
print("Shape:", df2.shape)
print("\nData Types:\n", df2.dtypes)
print("\nMissing Values:\n", df2.isnull().sum())
print("\nSummary Statistics:\n", df2.describe(include='all'))

df3 = pd.DataFrame(df2, columns=['Burner'])
x = df3
plt.hist(x,bins=10)

#plt.plot(label=Day 1)
plt.xlabel("Temperature ° C")
plt.ylabel("Count")
plt.title("Chart Title")
plt.legend()

plt.show()

#df2 = pd.DataFrame(data, columns=['DATE'])
#print(df2.iloc[0])
