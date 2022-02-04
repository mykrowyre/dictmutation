This is a short script I wrote to mutate a dictionary file using only the 
character substitutions provided in the character substitution file.  Of course the purpose
is to brute force passwords.

Example chars.txt:

aA4
eE3
tT+
iI1

Example words.txt:

test

Example output:

test
tesT
tes+
tEst
tEsT
tEs+
t3st
t3sT
t3s+
Test
TesT
Tes+
TEst
TEsT
TEs+
T3st
T3sT
T3s+
+est
+esT
+es+
+Est
+EsT
+Es+
+3st
+3sT
+3s+


