# 10 - An egg or not ...

> ... an egg, that's the question!
> 
> Are you able to answer this question and find the (real) egg?
> 
> ![egg](aneggornot_orig.svg)

The background image already has white center, so seems odd for
there to be a bunch of white pixels in the .svg file. Changing the 
`#w` and `#b` to `fill-opacity:0.5`, we indeed see some overlap. 
After some testing, it turns out that reversing the order of the
`<use ...>` tags produces the correct egg.
