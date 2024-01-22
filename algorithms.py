
from BoyerMoore import  boyer_moore_algo
from kmp import KMPSearch
from naive import naive
from suffixAarrays import suffixAarrays
from kmer import find_valid_pairs,compute_suffix_array


def chooseAlgorithm(p,t,option,k = 2):
    if option==0:
         result = naive(p,t)
    elif option==1:
         result=boyer_moore_algo(p,t) 
    elif option==2:
        result=suffixAarrays(t)
    elif option==3:
         suffix_arr = compute_suffix_array(t)
         result =find_valid_pairs(suffix_arr, k)
    elif option==4:
        result=KMPSearch(p,t)
    return result

