# demo-wheel

3D rotating carousel with 5 slides

If you want to add or remove slides, then add/remove them to/from #spinner div as .slider class. 
Change the rotating angle in the JS file as "angle = angle +/- (360 / number of slides)".
In CSS add/remove :nthChild(n) and the deg has to decreased from the first deg (0) with (360 / number of slides).
At the end you can play with perspective to get the best looking wheel. 

The whole building is a bit instabil, but works.
Not too responsive. The reason is the different size of picture what I used. 
