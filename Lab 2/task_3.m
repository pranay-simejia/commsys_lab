unique_chars = {'P','R','A','N','Y',' ','S','I','M','J','E'};
prob = [1/15,1/15,3/15,1/15,2/15,1/15,1/15,2/15,1/15,1/15,1/15];
dict = huffmandict(unique_chars,prob);
name="PRANAY SIMEJIYA";
code=huffmanenco(name,dict);
decode=huffmandeco(code,dict);
