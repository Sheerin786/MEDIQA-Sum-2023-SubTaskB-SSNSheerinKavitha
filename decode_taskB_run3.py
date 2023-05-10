from transformers import pipeline From pdfminer.high_level import extract_text 
import docx2txt
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
def text_ext(file):
	if file.endswith(".csv"):
		return extract_text(file)
	else:
		resume_text = doc2txt.process(file)
	if resume_text:
		return resume_text.replace('\t',' ')
	return None
texts=pd.read_csv(r'TaskB-TestSet.csv')
text_extracted = text_ext('texts')
z=[]
file = open('run3.csv', 'w+', newline ='')
with file:  
	write = csv.writer(file)
	i = 0
	for text in texts['dialogue']:
		summary = summarizer(text, max_length =250, min length = 30, do_sample = False)
		print("The summary extracted is:", summary)
		write.writerow([i,text])
		i+=1




