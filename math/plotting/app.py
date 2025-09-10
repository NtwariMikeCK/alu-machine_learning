import pandas as pd
import matplotlib.pyplot as plt

# Example DataFrame
df = pd.DataFrame({
    'flag': [True, False, True, True, False, False, True, False, True]
})

# Count True/False occurrences
counts = df['flag'].value_counts()

# Plot bar graph
counts.plot(kind='bar')

plt.xlabel("Flag")
plt.ylabel("Count")
plt.title("Counts of True and False")
plt.show()
