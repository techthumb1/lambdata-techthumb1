If __name__=='__main__':
#y = int(input("Choose a number: "))
# print(enlarge(y))


raw_data = load_wine()
df = pd.DataFrame(data=raw_data['data'], columns=raw_data['feature_names'])
df['target'] = raw_data['target']
breakpoint()

print(df.shape)

X_train, x_val, X_test, y_train, y_val, y_test = train_validation_test_split(df[['ash', 'hue']])