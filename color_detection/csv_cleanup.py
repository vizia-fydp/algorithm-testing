import pandas as pd

colors = pd.read_csv("colors.csv")

# Prepare output data frame
d = {"Name": [], "Hex": [], "R" : [], "G" : [], "B" : []}
column_order = ["Name", "Hex", "R", "G", "B"]
output_df = pd.DataFrame(data = d, columns=column_order)

for _, row in colors.iterrows():
    output_df = output_df.append(
        {
            "Name" : row["Name"],
            "Hex": row["Hex"],
            "R" : int(row["R"]),
            "G" : int(row["G"]),
            "B": int(row["B"])
        },
        ignore_index = True
    )

m = (output_df.dtypes=='float')
output_df.loc[:,m] = output_df.loc[:,m].astype(int)
output_df.to_csv("colors_fix.csv", index=False)
