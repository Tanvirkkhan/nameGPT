# %% [markdown]
# 1. makemore is a model that will make more **more names** like the one we train it on using the 36000 names of `names.txt`
# 2. The NEW names will be unique and generated
#
# Character level
#

# %%
import matplotlib.pyplot as plt
import torch
words = open('names.txt', 'r').read().splitlines()

# %%
words[:10]

# %%
len(words)

# %%
min(len(w) for w in words)

# %%
max(len(w) for w in words)

# %%
b = {}
for w in words:
    # add <S> and <E> to the beginning and end of the word
    chs = ['<S>'] + list(w) + ['<E>']
    for ch1, ch2 in zip(chs, chs[1:]):
        bigram = (ch1, ch2)  # tuple of two characters
        # increment the count of the bigram by 1
        b[bigram] = b.get(bigram, 0) + 1

# %%
sorted(b.items(), key=lambda kv: -kv[1])
# sort the bigrams by their counts in descending order
# key=lambda x: x[1] means sort by the second element of the tuple
# lambda is a function that takes one argument and returns its value
# kv is a tuple of two elements, the first is the bigram, the second is its count
# kv[1] is the count of the bigram
# kv[0] is the bigram
# key is a function that takes a tuple and returns the second element of the tuple
# lambda returns the second element of the tuple

# %%

# %%
# 2D array/tensor for the bigrams
N = torch.zeros((28, 28), dtype=torch.int32)

# %%
chars = sorted(list(set(''.join(words))))
stoi = {s: i+1 for i, s in enumerate(chars)}
stoi['.'] = 0
itos = {i: s for s, i in stoi.items()}

# %%
itos

# %%
for w in words:
    chs = ['.'] + list(w) + ['.']
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        N[ix1, ix2] += 1

plt.figure(figsize=(16, 16))
plt.imshow(N, cmap='Blues')
for i in range(27):
    for j in range(27):
        chstr = itos[i] + itos[j]
        plt.text(j, i, chstr, ha='center', va='bottom', color='gray')
        plt.text(j, i, N[i, j].item(), ha='center', va='top', color='gray')
plt.axis('off')


# %%
N[0, :]

# %%
p = N[0].float()
p = p / p.sum()  # normalize the probabilities
p

# %%
g = torch.Generator().manual_seed(2147483647)
# sample one character from the distribution p
ix = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()
itos[ix]  # convert the index to a character


# %%
# sample one character from the distribution p
torch.multinomial(p, num_samples=100, replacement=True, generator=g)

# %%
g = torch.Generator().manual_seed(2147483647)

for i in range(10):
    out = []
    ix = 0
    while True:
        p = N[ix].float()
        p = p / p.sum()  # normalize the probabilities
        # sample one character from the distribution
        ix = torch.multinomial(
            p, num_samples=1, replacement=True, generator=g).item()
        out.append(itos[ix])
        if ix == 0:
            break

    print(''.join(out))

# %%
P = N.float()
# normalize the probabilities by the row (sum of the row is 1)
P /= P.sum(1, keepdim=True)
P[0], P[0].sum(), P

# %%
g = torch.Generator().manual_seed(2147483647)

for i in range(5):

    out = []
    ix = 0
    while True:
        p = P[ix]
        ix = torch.multinomial(
            p, num_samples=1, replacement=True, generator=g).item()
        out.append(itos[ix])
        if ix == 0:
            break
    print(''.join(out))

# %%
