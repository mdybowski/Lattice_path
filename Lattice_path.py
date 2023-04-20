import random

N = 20
n = 7


def find_path(L_paths, N, i, k, n, path_list):
    if k == n:
        return path_list, True
    if k+1 in L_paths[(i, 0)] and not (i, k+1) in path_list:
        plist = path_list.copy()
        path_list.append((i, k+1))
        f = find_path(L_paths, N, i, k+1, n, path_list)
        if f[1]:
            return f[0], True
        else:
            path_list = plist
    if i+1 <= N and k+1 in L_paths[(i+1, 0)] and not (i+1, k+1) in path_list:
        plist = path_list.copy()
        path_list.append((i+1, k+1))
        f = find_path(L_paths, N, i+1, k + 1, n, path_list)
        if f[1]:
            return f[0], True
        else:
            path_list = plist
    if i > 0 and k+1 in L_paths[(i-1, 0)] and not (i-1, k+1) in path_list:
        plist = path_list.copy()
        path_list.append((i-1, k+1))
        f = find_path(L_paths, N, i - 1, k + 1, n, path_list)
        if f[1]:
            return f[0], True
        else:
            path_list = plist
    if k-1 in L_paths[(i, 0)] and not (i, k-1) in path_list:
        plist = path_list.copy()
        path_list.append((i, k-1))
        f = find_path(L_paths, N, i, k - 1, n, path_list)
        if f[1]:
            return f[0], True
        else:
            path_list = plist
    if i+1 <= N and k-1 in L_paths[(i+1, 0)] and not (i+1, k-1) in path_list:
        plist = path_list.copy()
        path_list.append((i+1, k-1))
        f = find_path(L_paths, N, i+1, k - 1, n, path_list)
        if f[1]:
            return f[0], True
        else:
            path_list = plist
    if i > 0 and k-1 in L_paths[(i-1, 0)] and not (i-1, k-1) in path_list:
        plist = path_list.copy()
        path_list.append((i-1, k-1))
        f = find_path(L_paths, N, i-1, k - 1, n, path_list)
        if f[1]:
            return f[0], True
        else:
            path_list = plist
    if i+1 <= N and k in L_paths[(i + 1, 0)] and not (i+1, k) in path_list:
        plist = path_list.copy()
        path_list.append((i+1, k))
        f = find_path(L_paths, N, i+1, k, n, path_list)
        if f[1]:
            return f[0], True
        else:
            path_list = plist
    if i > 0 and k in L_paths[(i - 1, 0)] and not (i-1, k) in path_list:
        plist = path_list.copy()
        path_list.append((i-1, k))
        f = find_path(L_paths, N, i-1, k, n, path_list)
        if f[1]:
            return f[0], True
        else:
            path_list = plist
    return [], False


def final_path(L_paths, N, n):
    ones = []
    for i in range(N+1):
        if 1 in L_paths[(i, 0)]:
            ones.append(i)
    for one in ones:
        w = find_path(L_paths, N, one, 1, n, [(one, 1)])
        if w[1]:
            return w[0]
    return []


L = []
for i in range(N+1):
    for j in [1, 0, -1]:
        L.append((i, j))

L_paths = dict()
for item in L:
    L_paths[item] = []


for k in range(1, n+1):

    pos = (0, -1)

    L_paths[pos].append(k)

    for i in range(1, N):

        if pos[1] == 1:
            if k-1 in L_paths[(pos[0] + 1, -1)] and k > 1:
                r = -1
            else:
                r = random.choice([-1, 0])
        elif pos[1] == -1:
            if i == N-1:
                r = 1
            else:
                if k-1 in L_paths[(pos[0] + 1, 1)] and k > 1:
                    r = 1
                else:
                    r = random.choice([0, 1])
        else:
            if i == N-1:
                r = random.choice([0, 1])
            else:
                if k-1 in L_paths[(pos[0] + 1, -1)] and k > 1:
                    r = random.choice([-1, 0])
                elif k-1 in L_paths[(pos[0] + 1, 1)] and k > 1:
                    r = random.choice([0, 1])
                else:
                    r = random.choice([-1, 0, 1])

        pos = (pos[0] + 1, pos[1] + r)

        L_paths[pos].append(k)

    L_paths[(N, 1)].append(k)

Q_path = final_path(L_paths, N, n)

w1 = ''
w0 = ''
w_m = ''
for i in range(N+1):
    k1 = '({}, 1):   {}'.format(i, L_paths[(i, 1)])
    k0 = '({}, 0):   {}'.format(i, L_paths[(i, 0)])
    k_m = '({}, -1):  {}'.format(i, L_paths[(i, -1)])

    w1 = w1 + k1
    w0 = w0 + k0
    w_m = w_m + k_m

    max_len = max([len(k1), len(k0), len(k_m)])

    w1 = w1 + ' ' * (max_len - len(k1) + 2)
    w0 = w0 + ' ' * (max_len - len(k0) + 2)
    w_m = w_m + ' ' * (max_len - len(k_m) + 2)

print('The lattice L with all paths (N = {}, n = {}):'.format(N, n))
print(' ')
print(w1)
print(w0)
print(w_m)
print(' ')
print('Sample sequence Q:')
print(Q_path)
