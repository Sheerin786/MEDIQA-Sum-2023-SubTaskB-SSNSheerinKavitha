#text = "Google Workspace[1] (formerly known as Google Apps and later G Suite) is a collection of cloud computing, productivity and collaboration tools, software and products developed and marketed by Google. It consists of Gmail, Contacts, Calendar, Meet and Chat for communication; Currents for employee engagement; Drive for storage; and the Google Docs Editors suite for content creation. An Admin Panel is provided for managing users and services.[2][3] Depending on edition Google Workspace may also include the digital interactive whiteboard Jamboard and an option to purchase such add-ons as the telephony service Voice. The education edition adds a learning platform Google Classroom and today has the name Workspace for Education.[4]"
#text ="When did your pain begin?  Ive had low back pain for about eight years now. Is there any injury?   Yeah, it started when I fell in an A B C store. How old are you now?  Im twenty six.    What kind of treatments have you had for this low back pain?   Yeah, I got referred to P T, and I went, but only once or twice, um, and if I remember right, they only did the electrical stimulation, and heat.  I see, how has your pain progressed over the last eight years?  Its been pretty continuous, but its been at varying degrees, sometimes are better than others.  Do you have any children?  Yes, I had my son in August of two thousand eight, and Ive had back pain since giving birth.  Have you had any falls since the initial one?  Yes, I fell four or five days ago while I was mopping the floor.  Did you land on your lower back again? Yes, right onto my tailbone.  Did that make the low back pain worse?  Yes.  Have you seen any other doctors for this issue?  Yes, I saw Doctor X on January tenth two thousand nine, and I have a follow up appointment scheduled for February tenth two thousand nine."
import spacy
from heapq import nlargest
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')
z=[]
file = open('run1.csv', 'w+', newline ='')
with file:  
	write = csv.writer(file)
	i = 0
	for text in texts['dialogue']:
		doc = nlp(text)
		tokens = [token.text for token in doc]
		print(tokens)
		print(punctuation)
		punctuation = punctuation + '\n'
		word_frequencies ={}
		for word in doc:
			if word.text.lower() not in stopwords:
				if word.text.lower() not in punctuation:
					if word.text not in word_frequencies.keys():
						word_frequencies[word.text]=1
					else:
						word_frequencies[word.text]+=1
		print(word_frequencies)


		max_frequency = max(word_frequencies.values())
		for word in word_frequencies.keys():
			word_frequencies[word] = word_frequencies[word]/max_frequency
		sentence_tokens = [sent for sent in doc.sents]
		sentence_scores = {}
		for sent in sentence_tokens:
			for word in sent:
				if word.text.lower() in word_frequencies.keys():
					if sent not in sentence_scores.keys():
						sentence_scores[sent]=word_frequencies[word.text.lower()]
					else:
						sentence_scores[sent]+=word_frequencies[word.text.lower()]

		select_length = int(len(sentence_tokens)*0.3)
		summary=nlargest(select_length, sentence_scores, key =sentence_scores.get)
		#print(summary)

		final_summary=[word.text for word in summary]
		summary = ':'.join(final_summary)
		print(text)
		print(len(text))
		print(len(summary))

		write.writerow([i,text])
		i+=1


