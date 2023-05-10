import pandas as pd
import csv
from transformers import AutoTokenizer
from transformers import TFAutoModelForSeq2SeqLM
texts=pd.read_csv(r'TaskB-TestSet.csv')
tokenizer = AutoTokenizer.from_pretrained("stevhliu/my_awesome_billsum_model")
model = TFAutoModelForSeq2SeqLM.from_pretrained("stevhliu/my_awesome_billsum_model", from_pt=True)
z=[]
file = open('run1.csv', 'w+', newline ='')
with file:  
	write = csv.writer(file)
	i = 0
	for text in texts['dialogue']:
		inputs = tokenizer(text, return_tensors="tf").input_ids
		outputs = model.generate(inputs, max_new_tokens=100, do_sample=False)
		tokenizer.decode(outputs[0], skip_special_tokens=True)
		z=tokenizer.decode(outputs[0], skip_special_tokens=True)
		print(tokenizer.decode(outputs[0], skip_special_tokens=True))
		print(len(tokenizer.decode(outputs[0], skip_special_tokens=True)))
		write.writerow([i,text])
		i+=1


