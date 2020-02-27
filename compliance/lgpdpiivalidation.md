### This file is concepted to test the basics Personally identifiable information (PII) using Regular Expressions (ReGex) into Splunk Enterprise in a Search Time to validate my personal Proof of Concept (PoC).

** Test a valid e-mail address: **

> rex field=_raw "(?<email>[a-zA-Z0-9_+&*-]+(?:\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,7})
  
```
182098102983 akssdlksja EMAIL@GMAIL.COM 123 jadlka nkjda908a0dun sadsd
maldj ajoj20 810 jlkjd ajas hsakl fvskddfh021371293c teste@hotmail.com lkj098231
asdja u2po3u1298 yn sb alj JONAS@EMAIL.COM.br qwd,ja kjsd
a slkjka çdkasçdl ka81273 o iajd81239@aol.com.br aslkdjad 09
asdjao d7b12 984 qfugldkcuc-0 m2442 =-=--021 alguamasdlj_12&@mgaicla.com.br asjkdkhas 812 hjkn
1297129837 98k jla  a 0 091" 8sjdklja =-= trulyemail@email.com.br 01982309128
1297129837 98k jla  a 0 091" l1237 n =-= trulyemail@email.eu 09182391723c
1297129837 98k jla  a 0 091" laoa=-=12222_0=-&trulyemail@email.com.br 72398173981
```

** Test a credit card | cartao de credito string: **

> (?<creditcardIncidence>(cart.o.de.cr.dito|cart.credit|card_credit|[cC]{2}))
  
```
cartão de crédito
cartao_de_credito
cartão_de_credito
cc asdasda
CCasdasd
cart_credit
card_credit
card_credito
cart_credito
```
