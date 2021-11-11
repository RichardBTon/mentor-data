def total_inntekt(df):
    total = 0
    for i, row in df.iterrows():
        total += row["INN PÅ KONTO"]

    return total
