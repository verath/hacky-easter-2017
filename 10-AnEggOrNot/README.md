# 10 - An egg or not ...

> ... an egg, that's the question!
> 
> Are you able to answer this question and find the (real) egg?
> 
> ![egg_orig](aneggornot_orig.png)

(note: the images provided for the challenge are the .svg files, the .png files
are used only so github displays the eggs)

The background image already has white center, so seems odd for
there to be a bunch of white pixels in the .svg file. Changing the 
`#w` and `#b` to `fill-opacity:0.5`, we indeed see some overlap. 
After some testing, it turns out that reversing the order of the
`<use ...>` tags produces the correct egg.

![egg](aneggornot_reversed.png)
