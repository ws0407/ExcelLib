import numpy as np
import pandas as pd


df = pd.DataFrame({
        'Index': list(range(1, 13)),
        'A': ['one', 'one', 'two', 'three'] * 3,
        'B': ['A', 'B', 'C'] * 4,
        'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
        'D': np.random.randint(low=10, high=20, size=12, dtype='int'),
        'E': np.random.randn(12)
    })
print(df)


new_df = df[df['A'] == 'one']
print(new_df)