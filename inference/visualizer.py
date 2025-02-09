import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

csv_file = './dataset/urgency_data.csv'  
df = pd.read_csv(csv_file)

print("Dataset Overview:")
print(df.info())
print("\nLabel Distribution:")
print(df['label'].value_counts())

plt.figure(figsize=(8, 5))
sns.countplot(x='label', data=df, palette='coolwarm')
plt.title('Label Distribution')
plt.xlabel('Label')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

df['conversation_length'] = df['conversation'].apply(lambda x: len(str(x).split())) # word count in each conversation
print(df['conversation_length'])
plt.figure(figsize=(8, 5))
sns.histplot(df['conversation_length'], bins=20, kde=True, color='blue')
plt.title('Conversation Length Distribution')
plt.xlabel('Number of Words')
plt.ylabel('Frequency')
plt.show()

text = ' '.join(df['conversation'].astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Word Cloud of Conversations')
plt.show()
