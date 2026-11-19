import pandas as pd

df = pd.read_excel(
    "fake_loanlist.xlsx",
    dtype={
        "Mobile": str
    }
    )

print(df.head())
print(df.columns)
df.info()