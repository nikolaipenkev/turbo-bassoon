import pandas as pd
import re

def correct_dataset(df):
    df = df.copy()

    # 1. Fix negative PurchaseAmount (set to abs value)
    df['PurchaseAmount'] = df['PurchaseAmount'].apply(lambda x: abs(x) if x < 0 else x)

    # 2. Fix unusual ages (<18 or >100) - set to None
    df['Age'] = df['Age'].apply(lambda x: x if 18 <= x <= 100 else None)

    # 3. Round PurchaseQuantity to nearest integer
    df['PurchaseQuantity'] = df['PurchaseQuantity'].round().astype(int)

    # 4. Replace odd product names (len<3) with 'Unknown'
    df['Product'] = df['Product'].apply(lambda x: x if isinstance(x, str) and len(x) >= 3 else 'Unknown')

    # 5. Truncate long country names to 30 chars
    df['Country'] = df['Country'].apply(lambda x: x[:30] if isinstance(x, str) and len(x) > 30 else x)

    # 6. Fix email format (simple lower-case)
    df['Email'] = df['Email'].apply(lambda x: x.lower() if isinstance(x, str) else x)

    # 7. Remove quotes from company field
    df['Company'] = df['Company'].apply(lambda x: x.strip('"') if isinstance(x, str) else x)

    return df