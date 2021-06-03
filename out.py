float a;
float b;
float s;
float c;
a = 0;
while(a<1):
	print("Enter number of scores: \n")
	if(0 == scanf("%f", &a)) {
a = 0;
scanf("%*s");
}
b = 0;
s = 0;
print("Enter one value at a time: \n")
while(b<a):
	if(0 == scanf("%f", &c)) {
c = 0;
scanf("%*s");
}
	s = s+c;
	b = b+1;
printf("%.2f\n", (float)(s/a));
