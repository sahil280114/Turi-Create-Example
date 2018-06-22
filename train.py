import turicreate as tc 


data = tc.SFrame('turi.sframe')

train_data , test_data = data.random_split(0.8)

model = tc.image_classifier.create(train_data,target="hero-name")

predictions = model.predict(test_data)

metrics = model.evaluate(test_data)

print(metrics['accuracy'])

model.export_coreml('JusticeLeagueModel')