# 20 - Spaghetti Hash

> Lazy Larry needs to improve the security of his password hashing implementation. 
> He decides to use SHA-512 as a new hashing algorithm in order to be super secure. 
> Unfortunately, the database column for the hash can only hold 128 bit. As Bob is 
> too lazy to extend the column and all the code related to it, he decides to shrink 
> the output of the SHA-512 operation, to 128 bit. For this purpose he picks certain 
> characters from the SHA-512 output for producing the new value.
> 
> You got hold of four password hashes, calculated with Bob's new implementation. 
> Can you find the corresponding passwords?
> 
>   hash 1: 87017a3ffc7bdd5dc5d5c9c348ca21c5
>   hash 2: ff17891414f7d15aa4719689c44ea039
>   hash 3: 5b9ea4569ad68b85c7230321ecda3780
>   hash 4: 6ad211c3f933df6e5569adf21d261637
>
> Lucky you, you know that the following web service is calculating Bob's algorithm.
> However, the web service only accepts strings of length 4 or less - brute-forcing 
> a password list thus is no option, since the passwords you are looking for are 
> all longer.
> 
>   https://hackyeaster.hacking-lab.com/hackyeaster/hash?string=abcd

The hard part of this level is detereming what parts of the sha-512 output that
Bob uses. To do so, the [spaghetti_hash.py](spaghetti_hash.py) script queries
the provided web service until it can determine what indices are kept, and what their
positions in the new hash is.

Once that is know, a simple bruteforce is run using the rockyou password list.

```
>  python ./spaghetti_hash.py
Determening pattern...
Testing: 0
Testing: 1
Testing: 2
Index pattern found!
65 -> 0, 17 -> 1, 115 -> 2, 31 -> 3, 45 -> 4, 11 -> 5, 67 -> 6, 92 -> 7, 0 -> 8, 7 -> 9, 123 -> 10, 37 -> 11, 5 -> 12, 22 -> 13, 87 -> 14, 124 -> 15, 25 -> 16, 89 -> 17, 38 -> 18, 61 -> 19, 90 -> 20, 109 -> 21, 63 -> 22, 28 -> 23, 102 -> 24, 12 -> 25, 47 -> 26, 59 -> 27, 110 -> 28, 86 -> 29, 24 -> 30, 18 -> 31
Cracking passwords...
6ad211c3f933df6e5569adf21d261637 == 12345678
ff17891414f7d15aa4719689c44ea039 == Cleveland
87017a3ffc7bdd5dc5d5c9c348ca21c5 == Prodigy
5b9ea4569ad68b85c7230321ecda3780 == benchmark
```
