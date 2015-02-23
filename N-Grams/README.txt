Version : Python 2.7.9

Download and store NGrams.py in desired folder.

1. Running the python code :
python <File Name>
python NGrams.py

2. Input Specification :
Enter the filename and the two input test sentences upon prompt

Enter file name : /Users/tanvi/Box Sync/Projects/NLP/N-Grams/src/NLPCorpusTreebank2Parts.txt
Enter sentence 1 : The company chairman said he will increase the profit next year .
Enter sentence 2 : The president said he believes the last year profit were good .

3. Output:
The output shows the bigram count matrices of input sentences, Probability matrices and the total probability for bigram, bigram with laplace smoothing and bigram with good turing.
The final probabilities are negative because I am summing up the log of the probabilities instead of multiplying the probabilities, to avoid underflow.

Bigram count matrix for sentence 1 :  
{'will increase': 1, 'company chairman': 1, 'year .': 1, 'said he': 1, 'chairman said': 1, 'profit next': 1, 'increase the': 1, 'the profit': 1, 'the company': 1, 'he will': 1, 'next year': 1}
Bigram count matrix for sentence 2 :  
{'year profit': 1, 'said he': 1, 'were good': 1, 'believes the': 1, 'good .': 1, 'the president': 1, 'profit were': 1, 'he believes': 1, 'president said': 1, 'last year': 1, 'the last': 1}
Probability Matrix for sentence 1 :  
{'will increase': 0.0, 'company chairman': 0.0, 'year .': 0.125, 'said he': 0.07473309608540925, 'chairman said': 0.012302284710017574, 'profit next': 0.0, 'increase the': 0.0, 'the profit': 0.0, 'the company': 0.05815423514538559, 'he will': 0.05785123966942149, 'next year': 0.2857142857142857}
Probability Matrix for sentence 2 :  
{'year profit': 0.0, 'said he': 0.07473309608540925, 'were good': 0.0, 'believes the': 1.0, 'good .': 0.0, 'the president': 0.0025284450063211127, 'profit were': 0.0, 'he believes': 0.008264462809917356, 'president said': 0.0, 'last year': 0.12121212121212122, 'the last': 0.0025284450063211127}
Probability of sentence 1 :  -16.0185439947
Probability of sentence 2 :  -21.460137552
Sentence 1 has more probability.

With Laplace Smoothing
Bigram count matrix for sentence 1 :  
{'will increase': 1, 'company chairman': 1, 'year .': 1, 'said he': 1, 'chairman said': 1, 'profit next': 1, 'increase the': 1, 'the profit': 1, 'the company': 1, 'he will': 1, 'next year': 1}
Bigram count matrix for sentence 2 :  
{'year profit': 1, 'said he': 1, 'were good': 1, 'believes the': 1, 'good .': 1, 'the president': 1, 'profit were': 1, 'he believes': 1, 'president said': 1, 'last year': 1, 'the last': 1}
Probability Matrix for sentence 1 :  
{'will increase': 0.00018635855385762206, 'company chairman': 0.0001852537977028529, 'year .': 0.0009464319515426841, 'said he': 0.0039768618944323935, 'chairman said': 0.0013745704467353953, 'profit next': 0.00019007793195210037, 'increase the': 0.0001901863826550019, 'the profit': 0.00014634860237084735, 'the company': 0.013610420020488805, 'he will': 0.0014892032762472078, 'next year': 0.0013277693474962064}
Probability Matrix for sentence 2 :  
{'year profit': 0.0001892863903085368, 'said he': 0.0039768618944323935, 'were good': 0.0001887148518588413, 'believes the': 0.0003808073115003808, 'good .': 0.00019029495718363463, 'the president': 0.0007317430118542368, 'profit were': 0.00019007793195210037, 'he believes': 0.00037230081906180194, 'president said': 0.0001870207593042828, 'last year': 0.0009462528387585163, 'the last': 0.0007317430118542368}
Probability of sentence 1 :  -79.6570995943
Probability of sentence 2 :  -85.5662762089
Sentence 1 has more probability.

With Good Turing
Bigram count matrix for sentence 1 :  
{'will increase': 1, 'company chairman': 1, 'year .': 1, 'said he': 1, 'chairman said': 1, 'profit next': 1, 'increase the': 1, 'the profit': 1, 'the company': 1, 'he will': 1, 'next year': 1}
Bigram count matrix for sentence 2 :  
{'year profit': 1, 'said he': 1, 'were good': 1, 'believes the': 1, 'good .': 1, 'the president': 1, 'profit were': 1, 'he believes': 1, 'president said': 1, 'last year': 1, 'the last': 1}
Probability Matrix for sentence 1 :  
{'will increase': 0.503768115942029, 'company chairman': 0.503768115942029, 'year .': 9.686161725729033e-05, 'said he': 0.0004501278772378516, 'chairman said': 0.00016994395762581584, 'profit next': 0.503768115942029, 'increase the': 0.503768115942029, 'the profit': 0.503768115942029, 'the company': 0.0015856777493606139, 'he will': 0.00016994395762581584, 'next year': 0.00016178838685232546}
Probability Matrix for sentence 2 :  
{'year profit': 0.503768115942029, 'said he': 0.0004501278772378516, 'were good': 0.503768115942029, 'believes the': 7.529692454651463e-06, 'good .': 0.503768115942029, 'the president': 9.686161725729033e-05, 'profit were': 0.503768115942029, 'he believes': 7.529692454651463e-06, 'president said': 0.503768115942029, 'last year': 9.686161725729033e-05, 'the last': 9.686161725729033e-05}
Probability of sentence 1 :  -52.9124504533
Probability of sentence 2 :  -62.4541692571
Sentence 1 has more probability.
