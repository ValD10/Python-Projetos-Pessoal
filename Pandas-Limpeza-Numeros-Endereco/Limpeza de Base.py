import pandas as pd
import re

tecban = pd.read_excel("Base.xlsx")

checkpoint = 0

for index, row in tecban.iterrows():
    try:
        num = row["NÚMERO"]
        rgnums = r"\d+"
        encontrado = re.findall(rgnums, num)
        tecban.at[index, "TRATADO"] = encontrado
        checkpoint = checkpoint+1
        print(checkpoint)
    except:
        pass

tecban.to_excel("Lojas_Tecban_Tratado.xlsx", index = False)