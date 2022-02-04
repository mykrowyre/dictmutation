This is a short script I wrote to mutate a dictionary file using only the character substitutions provided in the character substitution file.  

Of course the purpose is to brute force passwords.<br>
<br>
Wrote this in memory of old times with Dr. Delam, Zibby, Phantom Dialer, Intrepid Traveller, Trouble, Kaleidox, and others. (maldoror)<br>
<BR>
Example chars.txt:<br>
<br>
aA4<br>
eE3<br>
tT+<br>
iI1<br>
<br>
Example words.txt:
<br>
test<br>
<br>
Example output:<br>
<br>
test<br>
tesT<br>
tes+<br>
tEst<br>
tEsT<br>
tEs+<br>
t3st<br>
t3sT<br>
t3s+<br>
Test<br>
TesT<br>
Tes+<br>
TEst<br>
TEsT<br>
TEs+<br>
T3st<br>
T3sT<br>
T3s+<br>
+est<br>
+esT<br>
+es+<br>
+Est<br>
+EsT<br>
+Es+<br>
+3st<br>
+3sT<br>
+3s+<br>


