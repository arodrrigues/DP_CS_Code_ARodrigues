

x1 = 2
y1 = 4
x2 = 4
y2 = 8

r = Math.pow((y2 - y1)*(y2 - y1) + (x2 - x1)*(x2-x1),1/2)

a = 3.1415*r*r
/*
a = a*1000
a = Math.round(a)
a = a/1000
*/
a = a.toPrecision(3)
console.log(a)

