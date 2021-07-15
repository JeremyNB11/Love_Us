def inplace_quick_sort(S, a, b):
    if a >= b:
        return
    pivot = S[a]
    i = a + 1
    j = b

    while i <= j:
        while i <= j and S[j] > pivot:
            j -= 1
        while i <= j and S[i] < pivot:
            i += 1
        if i <= j:
            S[i], S[j] = S[j], S[i]
            i, j = i + 1, j - 1  # shrink range   有相同元素时他就有用了

    S[a], S[j] = S[j], S[a]  # i!=j 因为后动的i会指过头

    inplace_quick_sort(S, a, j - 1)
    inplace_quick_sort(S, j + 1, b)


A = [5, 1, 1, 2, 0, 0]
print(A)
inplace_quick_sort(A, 0, len(A) - 1)
print(A)

B = [4, 5, 7, 6, 3, 2, 9, 8, 1]
print(B)
inplace_quick_sort(B, 0, len(B) - 1)
print(B)
